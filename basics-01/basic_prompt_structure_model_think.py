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
In a charming village, siblings Jack and Jill set out on 
a quest to fetch water from a hilltop  
well. As they climbed, singing joyfully, misfortune  
struck—Jack tripped on a stone and tumbled  
down the hill, with Jill following suit.  
Though slightly battered, the pair returned home to  
comforting embraces. Despite the mishap,  
their adventurous spirits remained undimmed, and they  
continued exploring with delight.
"""
# example 1
prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple 
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following 
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""
print(get_completion(prompt))


prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
response = get_completion(prompt_2)
print("\nCompletion for prompt 2:")
print(response)
