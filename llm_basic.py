
import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

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


# result=client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[{"role":"system" , "content":"You are a helpful assistant that makes jokes."},
#         {"role":"user", "content":"What is the square root of 49?"}],
#     temperature=0.7,
#     max_tokens=100
# )

# print(result.choices[0].message.content)
# print(f"Input Tokens:{result.usage.prompt_tokens}")
# print(f"Output Tokens:{result.usage.completion_tokens}")
# print(f"Total Tokens:{result.usage.total_tokens}")


#  --Streaming Text--
# stream=client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[
#         {"role":"system", "content":"youa are a helpful assistant"},
#         {"role":"user", "content":"Tell me a short story about a robot."}
#     ],
#     max_tokens=500,
#     stream=True
# )

# for chunks in stream:
#     if chunks.choices and chunks.choices[0].delta.content:
#         print(chunks.choices[0].delta.content, end="", flush=True)
    
# print()


# --Structured Output with Pydantic--

class Person(BaseModel):
    name:str
    age:int
    city:int
    
result=client.chat.completions.parse(
    model="openai/gpt-oss-20b",
    messages=[
        {"role":"system", "content":"You are a helpful assistant"},
        {"role":"user", "content":"Give me the name, age and city of a fictional person"}
    ],
    response_format=Person
)

person=result.choices[0].message.parsed
print(person)
print(person.name)
print(person.age)
print(person.city)
