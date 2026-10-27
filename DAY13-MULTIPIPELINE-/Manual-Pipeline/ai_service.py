from google import genai
from dotenv import load_dotenv
import os
from google.genai import errors
import json



load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)



def ask_llm(prompt):
            data = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input = prompt) 
            return data.output_text

