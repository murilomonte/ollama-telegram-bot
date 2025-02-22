## https://medium.com/@mdbaraujo/descubra-como-criar-seu-primeiro-chatbot-poderoso-usando-ollama-c784ae55c13b

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template: str = """
Answer in English

Here's what we've already said: {context}

Question: {question}

Answer:
"""
model: OllamaLLM = OllamaLLM(model="qwen2.5:0.5b")
# model: OllamaLLM = OllamaLLM(model="deepseek-r1:7b")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


def get_response(msg):
    result = chain.invoke(
        {
            "context": "",
            "question": msg,
        }
    )
    return result
