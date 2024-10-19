"""Summarizing
In this lesson, you will summarize text with a focus on specific topics.
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


if __name__ == "__main__":
    # Text to summarize
    prod_review = """
    Got this panda plush toy for my daughter's birthday, \
    who loves it and takes it everywhere. It's soft and \ 
    super cute, and its face has a friendly look. It's \ 
    a bit small for what I paid though. I think there \ 
    might be other options that are bigger for the \ 
    same price. It arrived a day earlier than expected, \ 
    so I got to play with it myself before I gave it \ 
    to her.
    """

    # 1. Summarize with a word/sentence/character limit
    # ___________________________________________________

    # prompt = f"""
    # Your task is to generate a short summary of a product \
    # review from an ecommerce site.

    # Summarize the review below, delimited by triple
    # backticks, in at most 30 words.

    # Review: ```{prod_review}```
    # """

    # 2. Summarize with a focus on shipping and delivery
    # ___________________________________________________

    # prompt = f"""
    # Your task is to generate a short summary of a product \
    # review from an ecommerce site to give feedback to the \
    # Shipping deparmtment.

    # Summarize the review below, delimited by triple
    # backticks, in at most 30 words, and focusing on any aspects \
    # that mention shipping and delivery of the product.

    # Review: ```{prod_review}```
    # """

    # 3. Try "extract" instead of "summarize"
    # ___________________________________________________

    # prompt = f"""
    # Your task is to extract relevant information from \ 
    # a product review from an ecommerce site to give \
    # feedback to the Shipping department. 

    # From the review below, delimited by triple quotes \
    # extract the information relevant to shipping and \ 
    # delivery. Limit to 30 words. 

    # Review: ```{prod_review}```
    # """

    response = get_completion(prompt)
    print(response)
