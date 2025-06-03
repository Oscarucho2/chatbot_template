import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_gpt_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "Eres un asistente de atención al cliente."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"