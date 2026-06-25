from openai import OpenAI
from importlib import import_module
import os 

from dotenv import load_dotenv

# Load API credentials and optional base URL from the local .env file.
load_dotenv()

try:
    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY"),
        base_url = os.getenv("OPENAI_BASE_URL")
    )
    print("OpenAI client initialized succesfully.")
except Exception as e:
    print("Error initializing OpenAI Client:", e) 


def get_completion(prompt, model="gpt-5", temperature=0):
        # Wrap the user prompt in a chat-style message payload for the model.
        messages = [
              {
                "role": "system",
                "content": "You are a helpful assistant designed to respond in json format."
            },
            {"role": "user", "content":prompt}]
        response = client.chat.completions.create(
            model=model, 
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content


def get_completion_from_messages(messages, model="gpt-5", temperature=0):
        response = client.chat.completions.create(
            model=model, 
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content


messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]

print("*"*50,"\n")
response = get_completion_from_messages(messages, temperature=1)
print(response)
print("*"*50,"\n")

# lets ask chatbot to remember the user's name
messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Hi, my name is Isa'}  ]
print("*"*50,"\n")
response = get_completion_from_messages(messages, temperature=1)
print(response)
print("*"*50,"\n")

# test if the chatbot can remember the user's name
messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
print("*"*50,"\n")
response = get_completion_from_messages(messages, temperature=1)
print(response)
print("*"*50,"\n")

# test if the chatbot can remember the user's name - by feeding the chatbot the entire message history
messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Isa'},
{'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
print("*"*50,"\n")
response = get_completion_from_messages(messages, temperature=1)
print(response)
print("*"*50,"\n")