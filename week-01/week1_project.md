Week 1 — Project: First LLM Interaction Script

Objective

Build a simple Python script that interacts with a Large Language Model (LLM) via API and allows you to experiment with:

- Temperature
- System prompt
- Prompt quality

The goal is to understand how small input changes affect model output.

----------------------------------------

Requirements

- Python 3.10+
- An API key from an LLM provider (e.g. OpenAI)
- Basic terminal usage

----------------------------------------

Setup

1. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  (macOS/Linux)
venv\Scripts\activate     (Windows)

2. Install dependencies

pip install openai python-dotenv

3. Configure environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

----------------------------------------

Base Implementation

Create a Python script that:

- Loads the API key from .env
- Sends a prompt to the LLM
- Prints the response

----------------------------------------

Functional Requirements

Your script must:

- Accept user input from the terminal
- Allow changing the temperature
- Allow customizing the system prompt
- Print the response clearly

----------------------------------------

Example Features

You should be able to do things like:

- Ask the same question with different temperatures
- Change the tone of the assistant via system prompt
- Compare weak vs strong prompts

----------------------------------------

Experiments (Mandatory)

1. Temperature test
Compare outputs with:
- temperature = 0
- temperature = 0.7
- temperature = 1.5

Write down what changes.

2. System prompt test

Try different system prompts:
- You are a strict and technical professor
- You are a sarcastic comedian

Observe how behavior changes.

3. Prompt quality test

Weak prompt:
tell me about AI

Strong prompt:
Explain what a Large Language Model is in 3 paragraphs with one real-world example

----------------------------------------

Expected Learning Outcomes

By the end of this project, you should understand:

- What temperature does
- How system prompts influence behavior
- Why prompt quality matters
- Why LLM outputs are not always deterministic

----------------------------------------

Deliverables

- Working Python script
- At least 3 experiment observations written in comments or a separate file
- Code committed to your repository

----------------------------------------

Bonus (Optional)

- Add input validation
- Format output (colors, spacing, etc.)
- Log responses to a file

----------------------------------------

Suggested Commit Message

feat: week 1 - basic LLM interaction script with experiments