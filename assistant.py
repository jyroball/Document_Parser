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
    #use classify function for now as a base

    #structure of llm input
    messages = [
        #prompt for behavior
        SystemMessage(content = "You are document classifier that can distinguish between different government type documents."),
        #prompt for question to llm
        HumanMessage(content = f"Given this document:\n\n{text}\n\n Can you tell me what type of government type document this is? I would like to keep the response simple, respond with a specific form name like 'W-2', 'I-130', 'DS-11', 'Passport' etc. or say 'Unknown'.")
    ]

    #sends prompt qeustions to llm using langcahin
    response = llm(messages)

    #return content of llm response
    return response.content.strip()