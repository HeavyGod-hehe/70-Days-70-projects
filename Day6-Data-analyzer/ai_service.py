from google import genai
from dotenv import load_dotenv
import os




load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)

def analyize_Data(summary_text , question):
    prompt = f"""
you are a Data Analyst Here is a Summary Of A Sales DataSet:
{summary_text}

answer This Question about the Data, in Simple Plain Language:
{question}
"""
    response = client.models.generate_content(
        model = "gemini-3.8-flash",
        contents=prompt
)
    return response.text