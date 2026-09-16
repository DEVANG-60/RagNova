from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Extract text from every page of a PDF.
    Keeps document name and page number as metadata.
    """

    reader = PdfReader(pdf_file)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            documents.append({
                "text": text.strip(),
                "page": page_number,
                "source": pdf_file.name
            })

    return documents