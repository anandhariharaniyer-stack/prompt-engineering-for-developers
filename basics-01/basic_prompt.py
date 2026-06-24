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
You should express what you want a model to do by  
providing instructions that are as clear and  
specific as you can possibly make them.  
This will guide the model towards the desired output,  
and reduce the chances of receiving irrelevant  
or incorrect responses. Don't confuse writing a  
clear prompt with writing a short prompt.  
In many cases, longer prompts provide more clarity  
and context for the model, which can lead to  
more detailed and relevant outputs.
"""

prompt = f"""
Summarize the text delimited by triple backticks
into a single sentence.
```{text}```
"""

print(get_completion(prompt))
