"""Inferring.
In this lesson, you will infer sentiment and topics from product reviews and news articles.
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

    lamp_review = """
    Needed a nice lamp for my bedroom, and this one had \
    additional storage and not too high of a price point. \
    Got it fast. The string to our lamp broke during the \
    transit and the company happily sent over a new one. \
    Came within a few days as well. It was easy to put \
    together. I had a missing part, so I contacted their \
    support and they very quickly got me the missing piece! \
    Lumina seems to me to be a great company that cares \
    about their customers and products!!
    """

    # 
    # 1. Product review Sentiment
    #_______________________________________
    # prompt = f"""
    # What is the sentiment of the following product review, 
    # which is delimited with triple backticks?

    # Review text: '''{lamp_review}'''
    # """

    # 
    # 2. Product review Sentiment: (negative/positive)
    #_______________________________________
    # prompt = f"""
    # What is the sentiment of the following product review, 
    # which is delimited with triple backticks?

    # Give your answer as a single word, either "positive" \
    # or "negative".

    # Review text: '''{lamp_review}'''
    # """

    # 
    # 3. Identify types of emotions.
    #_______________________________________

    # prompt = f"""
    # Identify a list of emotions that the writer of the \
    # following review is expressing. Include no more than \
    # five items in the list. Format your answer as a list of \
    # lower-case words separated by commas.

    # Review text: '''{lamp_review}'''
    # """

    # 
    # 4. Identify anger
    #_______________________________________
    # prompt = f"""
    # Is the writer of the following review expressing anger?\
    # The review is delimited with triple backticks. \
    # Give your answer as either yes or no.

    # Review text: '''{lamp_review}'''
    # """

    # 
    # 5. Extract product and company name from customer reviews
    #_______________________________________
    # prompt = f"""
    # Identify the following items from the review text: 
    # - Item purchased by reviewer
    # - Company that made the item

    # The review is delimited with triple backticks. \
    # Format your response as a JSON object with \
    # "Item" and "Brand" as the keys. 
    # If the information isn't present, use "unknown" \
    # as the value.
    # Make your response as short as possible.
    
    # Review text: '''{lamp_review}'''
    # """

    #
    # 6. Doing multiple tasks at once
    #_______________________________________
    prompt = f"""
    Identify the following items from the review text: 
    - Sentiment (positive or negative)
    - Is the reviewer expressing anger? (true or false)
    - Item purchased by reviewer
    - Company that made the item

    The review is delimited with triple backticks. \
    Format your response as a JSON object with \
    "Sentiment", "Anger", "Item" and "Brand" as the keys.
    If the information isn't present, use "unknown" \
    as the value.
    Make your response as short as possible.
    Format the Anger value as a boolean.

    Review text: '''{lamp_review}'''
    """

    # 7. Inferring topics
    #_______________________________________
    response = get_completion(prompt)
    print("Completion: \n")
    print(response)
