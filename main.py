import openai
from config import apikey  # Ensure config.py contains apikey

client = openai.OpenAI(api_key=apikey)  # Use the new client-based API

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

# Extract and print the response correctly
print(response.choices[0].message.content)
