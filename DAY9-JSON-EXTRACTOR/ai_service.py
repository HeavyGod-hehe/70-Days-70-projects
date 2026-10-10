from google import genai
from dotenv import load_dotenv
import os
from google.genai import errors
import json



load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)



def extract_json(text):
            prompt = f"""Hey You are an expert Data Extraction Tool i want you to Extract This Data From this  \n {text} \n Extract The Data According to These Schemas
            phone_model : str or None \n
            storage_in_gb : int or None \n
            color : str or None \n
            battery_health : int or None \n
            accessories : list or None \n
            pta_status : boolean or None \n
            used_for_months : float or None \n 
            price : int or None \n Return the Price in Full numerical Notation \n
            location:str or None \n
              Strictly Avoid Writing Extra Stuff or Text And Fill This Data Only 
              Dont Add Any Stuff from yourside if the You find Nothing then just return the answer as null
              Return The Data in JSON Format 
              """
            data = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input = prompt) 
            return data.output_text

