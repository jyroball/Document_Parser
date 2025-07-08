import os
import json     #read data from classifier
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()                               #load data from .env
openai_key = os.getenv("OPENAI_API_KEY")    #Get api key for openai

#Initialize LLM from langchain chat model
llm = ChatOpenAI(temperature = 0.0, model = "gpt-3.5-turbo", openai_api_key = openai_key)

def document_assistant(user_quesiton):
    #try to read the json file if it exists
    try:
        with open("documents.json", "r", encoding = "utf-8") as f:
            document_data = json.load(f)
    except FileNotFoundError:
        return "File Not Found" #should not get here tbh
    
    #save data from json
    document_type = document_data["type"]
    document_content = document_data["text"]

    #structure of llm input
    messages = [
        #prompt for behavior
        SystemMessage(content = "You are an expert between different government type documents, you are to assist the user with any question they have regarding the document they provide. Specifically you are to answer what they can do with the document, what its contents are, and how they can fill it out if it is a form."),
        #prompt for question to llm
        HumanMessage(content = f"Given the {document_type} document that the user has provided:\n\n{document_content}\n\n Please assist the user with this question: {user_quesiton} \n\n Please respond to the user in a helpful accurate way, where they can know how to use, or what they can do with the document provided.")
    ]

    #sends prompt qeustions to llm using langcahin
    response = llm(messages)

    #return content of llm response
    return response.content.strip()