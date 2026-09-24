from google import genai
from dotenv import load_dotenv
import os
import json



load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)


def clean_text(text):
    prompt = f"""
    clean the text inside <user_text> tags.
    Fix the Spelling,grammar,casing,spacing and unnecessary filler words and Preserve the Meanings 
    facts and Tone 
    separate complete thoughts should be joined with a conjunction or separated with a period.
    Dont add Information or Rewrite more then Needed Preserve the Uncertain words rather then guess 
    example:
    <user_text> umm i think we should,like,send it tomorrow</user_text>
    {{"cleaned_text" : "I think we should send it tomorrow",
    "changes_made" : ["Removed the filler word 'umm'.",
     "corrected spelling and captalization"]}}
    now clean this text:
    <user_text>{text}</user_text>
    Return only Valid JSON only. Dont Return Any Tags in The Return Response \n """
    data = client.interactions.create(
        model="gemini-3.8-flash",
        input = prompt
    )
    output = data.output_text
    return json.loads(output)




