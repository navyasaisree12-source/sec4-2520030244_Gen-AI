
import os
from dotenv import load_dotenv
from llm_client import LLMClient, GeminiProvider, OllamaProvider

load_dotenv(override=True)

provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

if provider_name == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing in .env")

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":
    provider = OllamaProvider("llama3.2")

else:
    raise ValueError("Invalid provider. Choose gemini or ollama.")

client = LLMClient(provider)

prompt = input("Enter your prompt: ")
answer = client.generate(prompt)

print("\nAI Response:")
print(answer)
