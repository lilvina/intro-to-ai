from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_input):
    prompt = f"""
    You are a helpful assistant.

    Task:
    Respond clearly and concisely.

    User Input:
    {user_input}
    """

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"Error: {e}"
    
def main():
    print("AI Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = generate_response(user_input)
        print("\nAI:", response, "\n")

if __name__=="__main__":
    main()