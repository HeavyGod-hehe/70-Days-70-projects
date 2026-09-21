from google import genai
from dotenv import load_dotenv
import os




load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)


def summarize(text):
    prompt = "Summarize The following document \n "
    data = client.interactions.create(
        model="gemini-3.8-flash",
        input = prompt+text
    )
    return data