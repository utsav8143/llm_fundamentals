import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

result=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role":"user", "content":"What is the square root of 16?"}]
)

print(result.choices[0].message.content)
