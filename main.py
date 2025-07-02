from ocr_utils import extract_text_from_image, extract_text_from_pdf

def main():
    #get file for now
    path = input("Enter path to your document (PDF or JPG): ").strip()

    #check file extension to use different function
    if path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path.lower().endswith((".jpg", ".jpeg", ".png")):
        text = extract_text_from_image(path)
    else:
        print("Unsupported file type.")
        return

    print("\nText: \n")
    print(text[:1000])  # Just print the first 1000 chars for now

if __name__ == "__main__":
    main()