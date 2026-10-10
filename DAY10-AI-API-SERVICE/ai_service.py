from dotenv import load_dotenv
from google import genai
import os
from google.genai import errors
import json



load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)


def parse_output(clean_text):
        try:
                return json.loads(clean_text)
        except json.JSONDecodeError:
                raise ValueError("The Data is not JSON")

def goshugpt(text):
    prompt = f"""{text} Return the Response in the JSON Format
{{

  "question": "What is 2 + 2?",
  "answer": "4"
}}

       this type of JSON results i want you to return """
    data = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input = prompt)
    text =  data.output_text
    json_convert = parse_output(clean_text=text)
    return json_convert
