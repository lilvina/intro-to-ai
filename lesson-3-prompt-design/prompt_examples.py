from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_prompts():
    weak_prompt = "Explain Python"
    strong_prompt = "Explain Python to a beginner in 3 buller points with examples"

    print("Weak Prompt:\n")
    print(client.responses.create(
        model="gpt-4.1-mini",
        input=weak_prompt
    ).output_text)

    print("\nStrong Prompt:\n")
    print(client.responses.create(
        model="gpt-4.1-mini",
        input=strong_prompt
    ).output_text)

if __name__=="__main__":
    test_prompts()