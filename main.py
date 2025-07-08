#OCR Parser
from ocr_utils import extract_image, extract_pdf
#OpenAI Document identifier agent
from classify import classify_document
#OpenAI Document identifier number 2 to make sure it is correct
#NEED TO ADD
#One More Agent to have covo with to ask contents of the document and what is possible to do with this
#need to add

#add json for classification output
import json

def main():
    #get file for now
    path = input("Enter path to your document (PDF or JPG): ").strip()

    #check file extension to use different function
    if path.lower().endswith(".pdf"):
        text = extract_pdf(path)
    elif path.lower().endswith((".jpg", ".jpeg", ".png")):
        text = extract_image(path)
    else:
        print("Unsupported file type.")
        return

    print("\nText: \n")
    print(text[:1000])  # Just print the first 1000 chars for now

if __name__ == "__main__":
    main()