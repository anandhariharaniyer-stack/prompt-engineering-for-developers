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


pn = import_module("panel")  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ""
    print("*"*50,"\n")
    print(prompt)
    print("*"*50,"\n")
    context.append({"role": "user", "content": prompt})
    response = get_completion_from_messages(context)
    context.append({"role": "assistant", "content": response})

    panels.append(pn.Row("User:", pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row("Assistant:", pn.pane.Markdown(response, width=600))
    )
    return pn.Column(*panels)


interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard.servable()

if __name__ == "__main__":
    dashboard.show()
