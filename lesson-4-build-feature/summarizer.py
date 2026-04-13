from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    prompt = f"Summarize this in 3 bullet points:\n{text}"

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text

if __name__=="__main__":
    text = input("Enter text to summarize: ")
    summary = summarize_text(text)
    print("\nSummary\n", summary)