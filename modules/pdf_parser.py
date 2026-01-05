import fitz

def parse_pdf_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            pages.append({
                "page": i + 1,
                "text": text
            })
    return pages
