from openai import OpenAI
import os 

from dotenv import load_dotenv

load_dotenv()

try:
    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY"),
        base_url = os.getenv("OPENAI_BASE_URL")
    )
    print("OpenAI client initialized succesfully.")
except Exception as e:
    print("Error initializing OpenAI Client:", e) 


def get_completion(prompt, model="gpt-5"):
        messages = [
              {
                "role": "system",
                "content": "You are a helpful assistant designed to respond in json format."
            },
            {"role": "user", "content":prompt}]
        response = client.chat.completions.create(
            model=model, 
            messages=messages,
            temperature=0
        )
        print("\n Response: ", response, "\n")
        return response.choices[0].message.content

text = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest 
valley flows from a modest spring; the
grandest symphony originates from a single note; 
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""

prompt = f"""
```{text}```
"""
print(get_completion(prompt))

