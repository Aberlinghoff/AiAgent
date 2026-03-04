import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if api_key is None:
    raise RuntimeError("Environment variable was not found")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages
)

metadata = response.usage_metadata
if response.usage_metadata is not None:
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

else:
    # Handle the case where metadata is missing
    raise RuntimeError("No usage metadata available")
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(response.text)
else:
    print(response.text)


def main():
    print("Hello from jarvis!")


if __name__ == "__main__":
    main()
