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
    """Ask for a structured output
    """
    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """

    response = get_completion(prompt)
    return response


def tactic_3_text_1():
    """Ask the model to check whether conditions are satisfied
    """
    text_1 = """
    Making a cup of tea is easy! First, you need to get some \ 
    water boiling. While that's happening, \ 
    grab a cup and put a tea bag in it. Once the water is \ 
    hot enough, just pour it over the tea bag. \ 
    Let it sit for a bit so the tea can steep. After a \ 
    few minutes, take out the tea bag. If you \ 
    like, you can add some sugar or milk to taste. \ 
    And that's it! You've got yourself a delicious \ 
    cup of tea to enjoy.
    """

    prompt = f"""   
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - ...
    …
    Step N - ...

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"
    \"\"\"{text_1}\"\"\"
    """

    respsonse = get_completion(prompt)
    return respsonse


def tactic_3_text_2():
    """Ask the model to check whether conditions are satisfied
    """
    text_2 = f"""
    The sun is shining brightly today, and the birds are \
    singing. It's a beautiful day to go for a \ 
    walk in the park. The flowers are blooming, and the \ 
    trees are swaying gently in the breeze. People \ 
    are out and about, enjoying the lovely weather. \ 
    Some are having picnics, while others are playing \ 
    games or simply relaxing on the grass. It's a \ 
    perfect day to spend time outdoors and appreciate the \ 
    beauty of nature.
    """

    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - ...
    ....
    Step N - ...

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_2}\"\"\"
    """
    response = get_completion(prompt)
    return response

def tactic_4(): 
    """Few-shot prompting"""
    prompt = f"""
    Your task is to answer in a consistent style.

    <child>: Teach me about patience.

    <grandparent>: The river that carves the deepest \ 
    valley flows from a modest spring; the \ 
    grandest symphony originates from a single note; \ 
    the most intricate tapestry begins with a solitary thread.

    <child>: Teach me about resilience.
    """
    response = get_completion(prompt)
    return response


if __name__ == "__main__":
    ### Tactic 3 - text 1: Ask the model to check whether conditions are satisfied
    # tactic_3_text = tactic_3_text_1()
    # print("Completion for Text 1:")
    # print(tactic_3_text)

    ### Tactic 3 - text 2: Ask the model to check whether conditions are satisfied
    # text_2 = tactic_3_text_2()
    # print("Completion for Text 2:")
    # print(text_2)
    
    ### Tactic 4: 'Few-shot' prompting
    print("Completion for: 'Few-shot' prompting:")
    tactic_4_text = tactic_4()
    print(tactic_4_text)