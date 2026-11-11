
import os
from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient

load_dotenv(override=True)

print("=== Provider Agnostic LLM Client ===")
print("1. Gemini (Cloud)")
print("2. Ollama (Local)")

choice = input("Choose provider (gemini/ollama): ").strip().lower()

if choice == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY is missing in .env file.")
        exit()

    provider = GeminiProvider(api_key)

elif choice == "ollama":
    provider = OllamaProvider("llama3.2")

else:
    print("Invalid provider choice.")
    exit()

client = LLMClient(provider)

prompt = input("\nEnter your question: ")

try:
    answer = client.generate(prompt)
    print("\nAI Response:")
    print(answer)

except Exception as error:
    print("\nError:", error)
