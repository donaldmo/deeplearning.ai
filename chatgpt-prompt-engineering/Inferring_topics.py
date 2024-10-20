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

    story = """
    In a recent survey conducted by the government, \
    public sector employees were asked to rate their level \
    of satisfaction with the department they work at. 
    The results revealed that NASA was the most popular \
    department with a satisfaction rating of 95%.

    One NASA employee, John Smith, commented on the findings, \
    stating, "I'm not surprised that NASA came out on top. 
    It's a great place to work with amazing people and \
    incredible opportunities. I'm proud to be a part of \
    such an innovative organization."

    The results were also welcomed by NASA's management team, \
    with Director Tom Johnson stating, "We are thrilled to \
    hear that our employees are satisfied with their work at NASA. 
    We have a talented and dedicated team who work tirelessly \
    to achieve our goals, and it's fantastic to see that their \
    hard work is paying off."

    The survey also revealed that the \
    Social Security Administration had the lowest satisfaction \
    rating, with only 45% of employees indicating they were \
    satisfied with their job. The government has pledged to \
    address the concerns raised by employees in the survey and \
    work towards improving job satisfaction across all departments.
    """

    # 1. Infer 5 topics
    # __________________________________________________

    # prompt = f"""
    # Determine five topics that are being discussed in the \
    # following text, which is delimited by triple backticks.

    # Make each item one or two words long. 

    # Format your response as a list of items separated by commas.

    # Text sample: '''{story}'''
    # """
    # response = get_completion(prompt)
    # print(response)

    # 2. Make a news alert for certain topic
    # __________________________________________________

    topic_list = [
        "nasa", "local government", "engineering",
        "employee satisfaction", "federal government"
    ]

    prompt = f"""
    Determine whether each item in the following list of \
    topics is a topic in the text below, which
    is delimited with triple backticks.

    Give your answer as follows:
    item from the list: 0 or 1

    List of topics: {", ".join(topic_list)}

    Text sample: '''{story}'''
    """
    response = get_completion(prompt)
    print(response)

    topic_dict = {i.split(': ')[0]: int(i.split(': ')[1]) for i in response.split(sep='\n')}
    if topic_dict['nasa'] == 1:
        print("ALERT: New NASA story!")
