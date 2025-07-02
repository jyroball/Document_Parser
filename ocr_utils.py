from PIL import Image
import pytesseract      #OCR library for extracting text
import fitz             #Parser for PDF

#Function to getimage from text
def extract_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text
