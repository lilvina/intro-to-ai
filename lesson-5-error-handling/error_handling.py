from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def safe_ai_call(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"Error occurred: {e}"
    
if __name__=="__main__":
    result = safe_ai_call("Explain APIs")
    print(result)