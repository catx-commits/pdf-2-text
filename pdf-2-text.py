#!/usr/bin/env python3
"""
pdf-2-text.py

Batch extracts text from PDF files matching an input glob pattern or directory
and saves them as plain text files into an output directory.

Usage:
    python pdf-2-text.py --INPUT "source/*.pdf" --OUTPUT pdf_text
"""

import argparse
import glob
from pathlib import Path
import pypdf


def extract_pdf_to_text(pdf_path: Path) -> str:
    """Extracts text page-by-page from a PDF file."""
    text_content = []
    try:
        reader = pypdf.PdfReader(str(pdf_path))
        for page_idx, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text_content.append(f"--- PAGE {page_idx + 1} ---\n{page_text}")
        return "\n\n".join(text_content)
    except Exception as e:
        print(f"Error reading PDF {pdf_path.name}: {e}")
        return ""


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF files into text documents."
    )
    parser.add_argument(
        "--INPUT", "-i", required=True, help="Input PDF file path or glob pattern (e.g. 'source/*.pdf')."
    )
    parser.add_argument(
        "--OUTPUT", "-o", required=True, help="Output directory path for text files."
    )

    args = parser.parse_args()

    input_pattern = args.INPUT
    output_dir = Path(args.OUTPUT)
    output_dir.mkdir(parents=True, exist_ok=True)

    matching_files = glob.glob(input_pattern)
    if not matching_files:
        print(f"No PDF files found matching pattern: {input_pattern}")
        return

    print(f"Found {len(matching_files)} PDF file(s) to process.")

    for file_path_str in matching_files:
        file_path = Path(file_path_str)
        if not file_path.is_file():
            continue

        print(f"Extracting text from: {file_path.name}...")
        extracted_text = extract_pdf_to_text(file_path)

        if not extracted_text.strip():
            print(f"Warning: No text extracted from {file_path.name} (it may be scanned/image-based).")
            continue

        output_file_path = output_dir / f"{file_path.stem}.txt"
        output_file_path.write_text(extracted_text, encoding="utf-8")
        print(f"Saved text to: {output_file_path}")


if __name__ == "__main__":
    main()