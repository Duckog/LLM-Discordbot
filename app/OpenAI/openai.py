import os
import openai
from dotenv import load_dotenv
import tiktoken

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


def token_counter(prompt, model):
    "Calculates and returns the number of tokens in a conversation"

    encoding = tiktoken.encoding_for_model(model)

    conversation_string = ' '.join([f"{msg['role']}: {msg['content']}" for msg in prompt])

    token_count = len(encoding.encode(conversation_string))

    return token_count

def trim_prompt(prompt, requested_tokens, chosen_model):
    "Trims down a conversation to not exceed token limit"
    trimmed_prompt = prompt.copy()
    while token_counter(trimmed_prompt, chosen_model) + requested_tokens >= 4096:
        trimmed_prompt.pop(1)
    return trimmed_prompt

def gpt_response(prompt, chosen_model):
    "Returns a response from the chosen GPT-model based on the prompt"
    requested_tokens = 512
    trimmed = trim_prompt(prompt, requested_tokens, chosen_model)
    answer = openai.ChatCompletion.create(
        model = chosen_model,
        messages = trimmed,
        temperature = 0.8,
        max_tokens = requested_tokens
    )

    response = answer.choices[-1].message.content

    return response