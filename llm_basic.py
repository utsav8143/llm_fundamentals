import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# result=client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[{"role":"user", "content":"What is the square root of 16?"}]
# )

# print(result.choices[0].message.content)


result=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role":"system" , "content":"You are a helpful assistant that makes jokes."},
        {"role":"user", "content":"What is the square root of 49?"}],
    temperature=0.7,
    max_tokens=100
)

print(result.choices[0].message.content)
print(f"Input Tokens:{result.usage.prompt_tokens}")
print(f"Output Tokens:{result.usage.completion_tokens}")
print(f"Total Tokens:{result.usage.total_tokens}")