from google import genai
from dotenv import load_dotenv
import os
from google.genai import errors

PROMPT_TEMPLATE ="""
Hey LLM you are Customer Messages Classifier 
Your Role is to Classify The Data into Specific Categories 
complaint 
order_query 
payment_issue 
praise 
misc
promotional 
For Example if You get a text like 
Message:Hey i dont like your product there is some sort of issue in this
Label:complaint  
Defination:Customer Didnt liked the Product or Product is broken or Customer Have Any Issue
Message:hey what is the price of x product
Label:order_query
Defination:Customer Ask for Product avaibility,price or Any Question About Us 
Message: Assalam o alaikum Mujhe Meri Payment Receive Nahi hui
Label: payment_issue
Defination:Any Customer Payment Issues From our Side or Their Side
Message:Mujhe Apki Products Bohat Achi Lagti hai I love it 
Label:praise
Defination:Customers liked us or Our products Praising us
Message: Mere saath Collabration Karlein Please Hamari promotion hojayegi 
Label: promotional
Defination: Anyone Intrested in Doing promotional Things Like PR,Collabrations or Networking with us 
If you cant Understand Anything add that into misc 
Languages: English,Urdu,Roman Urdu 
You can receive Text in Any Language But Return The English labels options i have given above 
If you cant Figure about anything Then Label it to Misc Fallback to Misc 
Dont Return Anything excepts the Labels No Explainations About Anything 
Return label in lowercase exactly as written above
Message: {user_text}
Label: 

"""


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")



client = genai.Client(api_key = api_key)






def classify_text(user_text):
        try:
            prompt = PROMPT_TEMPLATE.format(user_text=user_text)
            generation_config={
                "temperature":0.1
            }
            data = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input = prompt,
            generation_config=generation_config)
            return data.output_text
        except errors.APIError as e:
            reason = e.code
            if reason == 504:
                print("TimeoutError")
                return None
            elif reason == 429:
                print("Rate Limit")
                return None
            elif reason == 400:
                print("General Request Issue")
                return None
            elif 500 <= reason < 600:
                print("Gemini is Busy Sabar Karun")
                return None
            else:
                print(f"{e.code} Unknown Error Occured")
                return None
            
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return None



if __name__ == "__main__":
    print(repr(classify_text("meri order 5 din se nahi aayi")))
    print(repr(classify_text("Mujhe apki product bohat pasand hai")))
    print(repr(classify_text("asdfgh 123")))
    print(repr(classify_text("Hey Lets Collabrate Together and Grow together")))
    