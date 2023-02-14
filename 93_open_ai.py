import os
import openai

###openai.api_key = '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'
prompt = input("Enter your Command: ")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

text = response.get('choices')[0].get('text')

print(text)
