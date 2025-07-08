#OCR Parser
from ocr_utils import extract_image, extract_pdf
#OpenAI Document identifier agent
from classify import classify_document
#OpenAI Document identifier number 2 to make sure it is correct
#NEED TO ADD
#One More Agent to have covo with to ask contents of the document and what is possible to do with this
from assistant import document_assistant

#add json for classification output
import json

def main():
    #get file for now
    path = input("Enter path to your document (PDF or JPG): ").strip()

    #check file extension to use different function
    if path.lower().endswith(".pdf"):
        parsed_text = extract_pdf(path)
    elif path.lower().endswith((".jpg", ".jpeg", ".png")):
        parsed_text = extract_image(path)
    else:
        print("Unsupported file type.")
        return

    #Show parsed document in text form for debugg
    print("\nParsed Text: \n")
    print(parsed_text[:1000])  # Just print the first 1000 chars for now

    #get what the document type is from langchain
    doc_type = classify_document(parsed_text)
    #output doc type for debug
    print(f"Document Type: {doc_type}")

    #save document as a json with type of document and parsed value
    document_data = {
        #just have document type and content for now, maybe add an ID later?
        #so we can differentiate between different documents from diff users?
        #also maybe so we can add to a DB like postgres later?
        "type": doc_type,
        "text": parsed_text
    }

    #create a json file to store data in
    with open("documents.json", "w", encoding = "utf-8") as f:
            json.dump(document_data, f, indent = 2)

    #before asking maybe make another agent to make sure the classifier was correct?

    #after storing we can ask another agent what we can do




if __name__ == "__main__":
    main()