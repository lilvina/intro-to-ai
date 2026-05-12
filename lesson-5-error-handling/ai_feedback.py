from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_prompt(student_prompt):
    feedback_prompt = f"""
    You are an AI curriculum assistant.

    Evaluate this student's AI prompt.

    Student Prompt:
    {student_prompt}

    Provide:
    1. Two strengths
    2. One improvement suggestion
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=feedback_prompt
    )

    return response.output_text

if __name__=="__main__":
    prompt = input("Enter your prompt: ")
    feedback = evaluate_prompt(prompt)

    print("\nAI Feedback:\n")
    print(feedback)