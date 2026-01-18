from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not loaded"

llm = OpenAI(model ="gpt-3.5-turbo-instruct")
result = llm.invoke("What is the capital of India?")

print(result)