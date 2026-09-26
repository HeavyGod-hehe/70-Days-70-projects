from google import genai
from dotenv import load_dotenv
import os
from schemas import EmailOutput
from google.genai import types


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)

def Email(Text):
    prompt = f""" Write an Email Base on These Instructions {Text} and Return the Data in JSON format
 """
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents = prompt,
        config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=EmailOutput
          ))
    return response.parsed