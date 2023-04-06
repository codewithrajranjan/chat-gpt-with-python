import os

import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def callChatGpt(prompt) :
    try:
        openai_result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature = 0.8
        )
        result = openai_result.choices[0].message.content
        print(result)
    except Exception as e:
        print("exception ocurred {}".format(e))



if __name__=="__main__":
    callChatGpt("how to learn chatgpt")

