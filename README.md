# Prompt Engineering for Developers

A small Python learning repo for practicing prompt-engineering patterns with the OpenAI API.

The examples focus on writing clearer prompts, structuring model output, using delimiters, checking conditions, summarizing text, inferring sentiment and topics, transforming text, expanding short inputs into longer responses, and building simple chatbot flows.

## Repository Structure

```text
.
├── basics-01/
│   ├── basic_prompt.py
│   ├── basic_prompt_structure_check_conditions.py
│   ├── basic_prompt_structure_few_shot_technique.py
│   ├── basic_prompt_structure_model_incorrect_solution.py
│   ├── basic_prompt_structure_model_think.py
│   └── basic_prompt_structure_output.py
├── iterative-02/
│   └── iterative-prompt.py
├── summarize-03/
│   └── summarize-prompt.py
├── inference-04/
│   └── inference-prompt.py
├── transform-05/
│   └── transform-prompt.py
├── expanding-06/
│   └── expand-prompt.py
├── chatbot-07/
│   ├── chatbot-app.py
│   └── orderbot-app.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10 or newer
- An OpenAI-compatible API key

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_optional_openai_compatible_base_url
```

`OPENAI_BASE_URL` is optional. Omit it if you are using OpenAI's default API endpoint.

## Running Examples

Run any script directly from the repository root:

```bash
python basics-01/basic_prompt.py
```

Other lesson scripts:

```bash
python basics-01/basic_prompt_structure_output.py
python basics-01/basic_prompt_structure_check_conditions.py
python basics-01/basic_prompt_structure_few_shot_technique.py
python basics-01/basic_prompt_structure_model_think.py
python basics-01/basic_prompt_structure_model_incorrect_solution.py
python iterative-02/iterative-prompt.py
python summarize-03/summarize-prompt.py
python inference-04/inference-prompt.py
python transform-05/transform-prompt.py
python expanding-06/expand-prompt.py
python chatbot-07/chatbot-app.py
```

Run the Panel order bot UI:

```bash
python chatbot-07/orderbot-app.py
```

You can also serve it with Panel:

```bash
panel serve chatbot-07/orderbot-app.py --show
```

## Lessons Covered

- `basics-01/`: Prompt structure, delimiters, output formatting, condition checking, few-shot prompting, and reasoning before grading.
- `iterative-02/`: Improve prompts through iteration by changing audience, length, structure, and output format.
- `summarize-03/`: Summarize reviews and product text with different focus areas.
- `inference-04/`: Infer sentiment, emotions, product metadata, and topics from text.
- `transform-05/`: Translate, transform tone, convert formats, proofread, and compare edited text.
- `expanding-06/`: Generate customer-service replies from review sentiment and source details.
- `chatbot-07/`: Build chat-style interactions and a simple pizza ordering bot with Panel.

## Notes

- Keep `.env` local and do not commit API keys.
- The scripts default to `gpt-5`; update the `model` argument in `get_completion()` if you want to use a different model.
- Some scripts print the raw API response before printing the final message content, which is useful while learning the response structure.
- `chatbot-07/orderbot-app.py` starts a local Panel app when run directly.
