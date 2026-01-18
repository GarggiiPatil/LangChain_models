from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    temperature=0.3,
    max_new_tokens=128
)

result = llm.invoke("What is the capital of India?")
print(result)
