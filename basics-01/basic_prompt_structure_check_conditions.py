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
Making a cup of tea is easy! First, you need to get some
water boiling. While that's happening, 
grab a cup and put a tea bag in it. Once the water is 
hot enough, just pour it over the tea bag. 
Let it sit for a bit so the tea can steep. After a  
few minutes, take out the tea bag. If you 
like, you can add some sugar or milk to taste.  
And that's it! You've got yourself a delicious 
cup of tea to enjoy.
"""

prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions,
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions,
then simply write \"No steps provided.\"

\"\"\"{text}\"\"\"
"""

print(get_completion(prompt))

text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the \ 
trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. \ 
Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a \ 
perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""

prompt_2 = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions,
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, then simply write \"No steps provided.\"

\"\"\"{text_2}\"\"\"
"""

print(get_completion(prompt_2))