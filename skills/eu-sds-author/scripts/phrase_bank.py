"""Index unchanged CSV/XLSX phrases and insert exact text by ID."""

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

TOKEN = re.compile(r"\[\[PHRASE:(P-[0-9a-f]{64})\]\]")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def phrase_id(wording):
    return "P-" + digest(wording.encode("utf-8"))


def csv_rows(data, delimiter):
    source = data.decode("utf-8-sig")
    if delimiter is None:
        try:
            delimiter = csv.Sniffer().sniff(source[:65536], delimiters=",;\t|").delimiter
        except csv.Error:
            delimiter = ","
    for number, row in enumerate(
        csv.reader(io.StringIO(source, newline=""), delimiter=delimiter, strict=True), 1
    ):
        yield f"CSV record {number}", tuple(row)


def xlsx_rows(data, sheet_name):
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise ValueError("XLSX needs openpyxl. Use a CSV export or retrieve source cells directly.") from exc
    workbook = load_workbook(io.BytesIO(data), read_only=True, data_only=False)
    try:
        if sheet_name is None and len(workbook.sheetnames) != 1:
            raise ValueError(f"Choose --sheet from {', '.join(workbook.sheetnames)}.")
        sheet = workbook[sheet_name or workbook.sheetnames[0]]
        for number, row in enumerate(sheet.iter_rows(), 1):
            cells = tuple(cell if cell.data_type in {"f", "e"} else cell.value for cell in row)
            yield f"{sheet.title}!row {number}", cells
    finally:
        workbook.close()


def make_index(args):
    data = args.source.read_bytes()
    suffix = args.source.suffix.lower()
    if suffix == ".csv":
        if args.sheet is not None:
            raise ValueError("--sheet applies only to XLSX.")
        rows = csv_rows(data, args.delimiter)
    elif suffix == ".xlsx":
        if args.delimiter is not None:
            raise ValueError("--delimiter applies only to CSV.")
        rows = xlsx_rows(data, args.sheet)
    else:
        raise ValueError("Use a UTF-8 CSV or XLSX file.")

    if args.header:
        next(rows, None)
    column = args.column
    phrases = {}
    for locator, row in rows:
        occupied = [n for n, value in enumerate(row, 1) if value is not None and value != ""]
        if args.column is None and occupied:
            if len(occupied) != 1 or (column is not None and column != occupied[0]):
                raise ValueError("Several columns contain data. Specify --column.")
            column = occupied[0]
        if column is None or column > len(row):
            continue
        wording = row[column - 1]
        if wording is None or wording == "":
            continue
        if not isinstance(wording, str):
            raise ValueError(f"{locator}, column {column} is not a plain text phrase.")
        if not wording.strip():
            continue
        identifier = phrase_id(wording)
        entry = phrases.setdefault(identifier, {"id": identifier, "wording": wording, "locations": []})
        entry["locations"].append(f"{locator}, column {column}")

    if not phrases:
        raise ValueError("No phrases found in the selected column.")
    return {"source": args.source.name, "source_sha256": digest(data), "phrases": list(phrases.values())}


def render(index, template):
    phrases = {}
    for entry in index["phrases"]:
        identifier = entry["id"]
        wording = entry["wording"]
        if identifier != phrase_id(wording) or identifier in phrases:
            raise ValueError(f"Invalid or repeated phrase ID: {identifier}")
        phrases[identifier] = wording
    if "[[PHRASE:" in TOKEN.sub("", template):
        raise ValueError("Draft template contains a malformed phrase token.")

    def insert(match):
        identifier = match.group(1)
        if identifier not in phrases:
            raise ValueError(f"Phrase ID is absent from index: {identifier}")
        return phrases[identifier]

    return TOKEN.sub(insert, template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    index = commands.add_parser("index")
    index.add_argument("source", type=Path)
    index.add_argument("output", type=Path)
    index.add_argument("--sheet")
    index.add_argument("--column", type=int)
    index.add_argument("--delimiter", choices=[",", ";", "\t", "|"])
    index.add_argument("--header", action="store_true")
    assembly = commands.add_parser("render")
    assembly.add_argument("index_file", type=Path)
    assembly.add_argument("template", type=Path)
    assembly.add_argument("output", type=Path)
    args = parser.parse_args()

    if args.command == "index" and args.column is not None and args.column < 1:
        parser.error("--column must be at least 1.")
    try:
        inputs = [args.source] if args.command == "index" else [args.index_file, args.template]
        if args.output.exists():
            raise ValueError("Choose a new output path to preserve existing files.")
        if args.output.resolve() in [path.resolve() for path in inputs]:
            raise ValueError("Choose an output path separate from the inputs.")
        if args.command == "index":
            result = json.dumps(make_index(args), ensure_ascii=False, indent=2) + "\n"
        else:
            index_data = json.loads(args.index_file.read_bytes().decode("utf-8"))
            result = render(index_data, args.template.read_bytes().decode("utf-8"))
        with args.output.open("xb") as output:
            output.write(result.encode("utf-8"))
    except (OSError, ValueError, csv.Error, KeyError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
