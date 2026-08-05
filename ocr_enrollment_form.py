from pathlib import Path
import pytesseract
from PIL import Image

root = Path("sample_documents")
scan_pdf_path = root / "enrollment_form_scan.pdf"
scan_png_path = root / "enrollment_form_scan.png"

try:
    from pdf2image import convert_from_path
    use_pdf = True
except ImportError:
    use_pdf = False

if use_pdf:
    print(f"Attempting PDF conversion from: {scan_pdf_path}")
    try:
        images = convert_from_path(str(scan_pdf_path), dpi=200)
    except Exception as exc:
        print(f"Warning: PDF conversion failed: {exc}")
        use_pdf = False

if not use_pdf:
    print(f"Falling back to PNG OCR from: {scan_png_path}")
    if not scan_png_path.exists():
        raise FileNotFoundError(f"Fallback PNG not found: {scan_png_path}")
    images = [Image.open(scan_png_path)]

for page_num, image in enumerate(images, start=1):
    print(f"\n--- Page {page_num} ---")
    try:
        text = pytesseract.image_to_string(image)
    except Exception as exc:
        raise RuntimeError(f"OCR failed on page {page_num}: {exc}")
    print(text)

print("\nOCR note: This source form is synthetic, with printed text and form lines only.")
print("Handwriting or checkbox marks would likely reduce OCR accuracy, and Tesseract may not reliably capture handwritten entries or filled checkboxes.")
