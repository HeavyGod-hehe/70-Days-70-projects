from google import genai
from dotenv import load_dotenv
import os




load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)


def message_writer_ai(prompt):
    data = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input = prompt
    )
    return data.output_text



if __name__ == "__main__":
    print(message_writer_ai("Say hello in Urdu"))