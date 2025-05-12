import os
from openai import OpenAI
from utils import extract_mcqs_from_response

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

client = OpenAI(api_key=api_key)

def generate_mcqs(topic, num=5):
    prompt = (
        f"Generate {num} multiple choice questions on the topic '{topic}'. "
        "Each question should have four options (A, B, C, D) and provide the correct answer. "
        "Respond in JSON format as a list of objects with keys: 'question', 'options', 'answer'."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert MCQ generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return extract_mcqs_from_response(content)
    except Exception as e:
        print("OpenAI Error:", e)
        return None
