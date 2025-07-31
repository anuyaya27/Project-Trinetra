import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def decode_clue(clue: str):
    system_prompt = "You are a Sanskrit cryptographer decoding ancient riddles for law enforcement."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": clue}
        ]
    )
    return {"interpretation": response['choices'][0]['message']['content']}