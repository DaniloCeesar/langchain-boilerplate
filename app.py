import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama


load_dotenv()

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL"), base_url=os.getenv("OLLAMA_BASE_URL"))


def generate_sync_response(city: str):
    template = "How’s the weather in {city}?"

    prompt = ChatPromptTemplate.from_template(template=template)
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"city": city})

    return response


response = generate_sync_response("Brasília")
print(response)
