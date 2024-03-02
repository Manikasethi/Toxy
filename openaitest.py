import openai
import os

# Set your OpenAI API key
api_key = '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'

# Initialize the OpenAI client with your API key
openai.api_key = api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write an email to my boss for resignation?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''{
  "id": "chatcmpl-8IDa1EYoAtIGhaR5FvwlNYZV8CUVA",
  "object": "chat.completion",
  "created": 1699352797,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Resignation Letter\n\nDear [Boss's Name],\n\nI hope this email finds you well. I am writing to inform you that after careful consideration, I have made the difficult decision to resign from my position at [Company Name], effective [last working day - usually two weeks from the date of the email, but can be adjusted based on your company's notice period].\n\nI have thoroughly enjoyed my time at [Company Name] and feel privileged to have had the opportunity to work alongside such remarkable colleagues and under your mentorship. I have learned a great deal and grown both personally and professionally during my tenure here.\n\nI would like to express my gratitude for the support, guidance, and opportunities provided to me throughout my time at the company. Working with you and the team has been a truly enriching experience, and I will cherish the memories and relationships I have built here.\n\nPlease let me know how I can assist during this transitional period. I am more than willing to help ensure a smooth handover of my responsibilities to a colleague or support in any other way deemed necessary by the company.\n\nI have prepared a comprehensive handover document outlining the ongoing tasks and projects I have been involved in, which I will present to you and my successor before my departure. Additionally, I will"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 16,
    "completion_tokens": 256,
    "total_tokens": 272
  }
}'''