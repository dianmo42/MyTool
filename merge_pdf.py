## This is a script to merge multiple PDF files into one PDF file.
## Required libraries: os, PyPDF2

import os
from PyPDF2 import PdfMerger

pdf_files = sorted([f for f in os.listdir() if f.lower().endswith('.pdf')])

if not pdf_files:
    print("No PDF files found")
else:
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
        print(f"PDF added: {pdf}")
    merger.write("merged.pdf")
    merger.close()