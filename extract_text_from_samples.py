from pathlib import Path
import pdfplumber
from docx import Document

root = Path("sample_documents")
benefits_pdf = root / "summary_of_benefits_and_coverage.pdf"
claims_docx = root / "claims_process.docx"

print(f"Reading PDF: {benefits_pdf}")
with pdfplumber.open(benefits_pdf) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        text = page.extract_text() or ""
        print(f"\n--- Page {i} ---\n")
        print(text)

print(f"\nReading Word document: {claims_docx}")
doc = Document(claims_docx)
for i, para in enumerate(doc.paragraphs, start=1):
    print(f"\n[{i}] {para.text}")
