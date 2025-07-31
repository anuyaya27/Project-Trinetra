import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_killer_response(prompt: str):
    system_prompt = "You are a mythological serial killer inspired by Ketu and ancient Vedic symbolism. Respond cryptically but with layers of meaning."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return {"response": response['choices'][0]['message']['content']}