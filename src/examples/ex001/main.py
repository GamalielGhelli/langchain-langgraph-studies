from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model('openai:gpt-4o-mini', temperature=0.2)
response = llm.invoke('What is the capital of France?')
print(response) 