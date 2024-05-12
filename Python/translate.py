import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'sk-proj-gyZEl33ElA6XqtDPEbDMT3BlbkFJtIQcpeElYHxohzNuXeGz'

response = openai.Completion.create(
  engine="gpt-4",  # Or another model like "gpt-3.5-turbo", "gpt-4", etc.
  prompt="Translate the following English text to French: 'Hello, how are you?'",
  max_tokens=60
)

print(response.choices[0].text.strip())
