
from openai import OpenAI

client = OpenAI(api_key='sk-proj-gyZEl33ElA6XqtDPEbDMT3BlbkFJtIQcpeElYHxohzNuXeGz')

response = client.chat.completions.create(
    model="gpt-4",  # Specify the model here, GPT-4 in this case
    messages=[{"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}],
    max_tokens=60
)

print(response.choices[0].message.content)