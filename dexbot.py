OPENAI_API_KEY = "YOUR_API_KEY"

import requests
import json


def get_chat_gpt_response(prompt):
  """Gets a response from ChatGPT."""

  # Create the URL.
  url = "https://api.openai.com/v1/engines/chat/completions"

  # Create the payload.
  payload = {
    "prompt": prompt,
    "temperature": 0.7,
    "max_tokens": 100,
    "no_repeat_ngrams": 1,
    "do_sample": True,
    "include_prompt": False
  }

  # Make the request.
  response = requests.post(url, json=payload)

  # Get the response data.
  response_data = json.loads(response.content)

  # Return the response.
  return response_data["choices"][0]["text"]


def main():
  """The main function."""

  # Get the user's prompt.
  prompt = input("What would you like to talk to Dexter about? ")

  # Get the response from ChatGPT.
  response = get_chat_gpt_response(prompt)

  # Print the response.
  print(response)


if __name__ == "__main__":
  main()
