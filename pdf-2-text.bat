@echo off
pip install pypdf
python pdf-2-text.py --INPUT "source/*.pdf" --OUTPUT pdf_text
pause