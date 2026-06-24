# Prompt Engineering for Developers

A small Python learning repo for practicing prompt-engineering patterns with the OpenAI API.

The examples focus on writing clearer prompts, structuring model output, using delimiters, checking conditions, providing few-shot examples, and asking the model to reason through a solution before judging an answer.

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

Other examples:

```bash
python basics-01/basic_prompt_structure_output.py
python basics-01/basic_prompt_structure_check_conditions.py
python basics-01/basic_prompt_structure_few_shot_technique.py
python basics-01/basic_prompt_structure_model_think.py
python basics-01/basic_prompt_structure_model_incorrect_solution.py
```

## Lessons Covered

- `basic_prompt.py`: Summarize text with a clear instruction.
- `basic_prompt_structure_output.py`: Request structured JSON output.
- `basic_prompt_structure_check_conditions.py`: Check whether input meets a condition before responding.
- `basic_prompt_structure_few_shot_technique.py`: Use examples to guide response style.
- `basic_prompt_structure_model_think.py`: Ask the model to complete a multi-step task in a specified format.
- `basic_prompt_structure_model_incorrect_solution.py`: Have the model solve a problem independently before grading a student's solution.

## Notes

- Keep `.env` local and do not commit API keys.
- The scripts default to `gpt-5`; update the `model` argument in `get_completion()` if you want to use a different model.
- Most scripts print the raw API response before printing the final message content, which is useful while learning the response structure.
