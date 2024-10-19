"""
Guidelines for Prompting

In this lesson you'll proactice two pompting principles and
thier realated tactics in order to write effective prompts for
large language models
"""

import os
import openai
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


def tactic_1():
    text = f"""
    You should express what you want a model to do by \ 
    providing instructions that are as clear and \ 
    specific as you can possibly make them. \ 
    This will guide the model towards the desired output, \ 
    and reduce the chances of receiving irrelevant \ 
    or incorrect responses. Don't confuse writing a \ 
    clear prompt with writing a short prompt. \ 
    In many cases, longer prompts provide more clarity \ 
    and context for the model, which can lead to \ 
    more detailed and relevant outputs.
    """

    prompt = f"""
    Summarize the text delimited by tripple backtics /
    into a single sentense.
    ```{text}```
    """

    response = get_completion(prompt)
    return response


def tectic_2():
    '''Ask for a structured output'''

    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres.
    provide them in JSON format with the following keys:
    book_title, title, author, genre.
    """

    response = get_completion(prompt)
    return response


if __name__ == "__main__":
    print(tectic_2())
