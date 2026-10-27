from google import genai
from dotenv import load_dotenv
import os




load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)


tool_csv_reader = {
    "name":"CSV_reader",
    "description":"Take the File path and return data in string",
    "type":"function",
    "parameters":{
        "type":"object",
        "properties":{
            "file_path": {
                "type":"string",
                "description":"Exact name of the CSV file to read, for example mill_sales.csv "
            }
        },
        "required":["file_path"]
    }
}


def get_ai_reply(chat_history):
    conversation_text = ""
    for message in chat_history:
        conversation_text +=(
            f"{message['role']}: {message['content']} \n"
        )
    prompt = "You are GOSHUGPT , A Helpful AI Assistant Reply Naturally to the user using the conversation history below \n"+conversation_text
    data = client.interactions.create(
        model="gemini-3.8-flash",
        input = prompt,
        tools=[tool_csv_reader]
    )

            
    return data
