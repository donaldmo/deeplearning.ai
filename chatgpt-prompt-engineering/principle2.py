"""
Guidelines for Prompting

In this lesson you'll proactice two pompting principles and
thier realated tactics in order to write effective prompts for
large language models.

Principle 2:
Give the model time to think.
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
    """Specify the steps required to complete a task    
    """
    text = f"""
    In a charming village, siblings Jack and Jill set out on \
    a quest to fetch water from a hilltop \
    well. As they climbed, singing joyfully, misfortune \
    struck—Jack tripped on a stone and tumbled \
    down the hill, with Jill following suit. \
    Though slightly battered, the pair returned home to \
    comforting embraces. Despite the mishap, \
    their adventurous spirits remained undimmed, and they \
    continued exploring with delight.
    """

    prompt = f"""
    Perform the following actions: 
    1 - Summarize the following text delimited by triple \
    backticks with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the following \
    keys: french_summary, num_names.

    Separate your answers with line breaks.

    Text:
    ```{text}```
    """

    response = get_completion(prompt)
    return response


def tactic_1_2():
    """Ask for output in a specified format
    """
    text = f"""
    In a charming village, siblings Jack and Jill set out on \
    a quest to fetch water from a hilltop \
    well. As they climbed, singing joyfully, misfortune \
    struck—Jack tripped on a stone and tumbled \
    down the hill, with Jill following suit. \
    Though slightly battered, the pair returned home to \
    comforting embraces. Despite the mishap, \
    their adventurous spirits remained undimmed, and they \
    continued exploring with delight.
    """

    prompt_2 = f"""
    Your task is to perform the following actions: 
    1 - Summarize the following text delimited by 
    <> with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the 
    following keys: french_summary, num_names.

    Use the following format:
    Text: <text to summarize>
    Summary: <summary>
    Translation: <summary translation>
    Names: <list of names in summary>
    Output JSON: <json with summary and num_names>

    Text: <{text}>
    """

    response = get_completion(prompt_2)
    return (response)

def tactic_2(): 
    """Instruct the model to work out its own solution before rushing to a conclusion
    """
    prompt = f"""
    Determine if the student's solution is correct or not.

    Question:
    I'm building a solar power installation and I need \
    help working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations \
    as a function of the number of square feet.

    Student's Solution:
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    """

    response = get_completion(prompt)
    return response

def tactic_2_2():
    """Tactic 2.2: Instruct the model to work out its own solution before rushing to a conclusion
    """
    prompt = f"""
    Your task is to determine if the student's solution \
    is correct or not.
    To solve the problem do the following:
    - First, work out your own solution to the problem including the final total. 
    - Then compare your solution to the student's solution \ 
    and evaluate if the student's solution is correct or not. 
    Don't decide if the student's solution is correct until 
    you have done the problem yourself.

    Use the following format:
    Question:
    ```
    question here
    ```
    Student's solution:
    ```
    student's solution here
    ```
    Actual solution:
    ```
    steps to work out the solution and your solution here
    ```
    Is the student's solution the same as actual solution \
    just calculated:
    ```
    yes or no
    ```
    Student grade:
    ```
    correct or incorrect
    ```

    Question:
    ```
    I'm building a solar power installation and I need help \
    working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations \
    as a function of the number of square feet.
    ``` 
    Student's solution:
    ```
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    ```
    Actual solution:
    """
    response = get_completion(prompt)
    print(response)


if __name__ == "__main__":
    """Tactic 1: Specify the steps required to complete a task."""
    # tactic_1_res = tactic_1()
    # print("Completion for prompt 1:")
    # print(tactic_1_res)

    """Tacktic 1.2: Ask for output in a specific format."""
    # response = tactic_1_2()
    # print("\n Completion for prompt 2:")
    # print(response)

    """Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion
    - Note that the student's solution is actually not correct.
    - We can fix this by instructing the model to work out its own solution first.
    """
    # response = tactic_2()
    # print("\n Completion for Tactic 2:")
    # print(response)

    """Tactic 2.2: Instruct the model to work out its own solution before rushing to a conclusion"""
    response = tactic_2_2()
    print(response)


