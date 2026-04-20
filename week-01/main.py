import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def ask(prompt, temperature=0.7, max_tokens=150, system_prompt="You are a helpful assistant."):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
            ],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask an LLM a question")
    parser.add_argument("prompt", help="The question to ask")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature (0-2, default: 0.7)")
    parser.add_argument("--system_prompt", default="You are a helpful assistant.", help="System prompt")
    parser.add_argument("--max-tokens", type=int, default=150, help="Max tokens in response (default: 150)")
    
    args = parser.parse_args()

    answer = ask(args.prompt, temperature=args.temperature, max_tokens=args.max_tokens, system_prompt=args.system_prompt)
    print("Answer:", answer)