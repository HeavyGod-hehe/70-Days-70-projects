from ai_service import ask_llm
import json




def extract_order(message):
    prompt = f"""Hey You are an expert to extract data from messages 
    For Example : 
Example 1:
Message: "bhai 20 bori atta bhejdo payment parso kardunga"
Output: {{"product": "atta", "quantity": 20, "payment_promise": "parso"}}

Example 2:
Message: "bhai maida bhejdena payment 3 din baad karunga"
Output: {{"product": "maida", "quantity": null, "payment_promise": "3 din baad"}}

Example 3:
Message: "salam, rate kya chal raha hai?"
Output: {{"product": null, "quantity": null, "payment_promise": null}}
    Now Extract from this \n "{message}"\n
    Strictly Avoid Writing Extra Stuff or Text And Fill This Data Only 
    Dont Add Any Stuff from yourside if the You find Nothing then just return the answer as null
    Return The Data in JSON Format No Explaination no code fences 
    """
    return ask_llm(prompt)



def parse_output(raw_text):

        data = raw_text.replace("```", "")
        data = data.strip()
        data = data.removeprefix("json")
        data = data.strip()
        try:
            return json.loads(data)
            
        except json.JSONDecodeError:
                return None

        



def check_order(data):
    if data is None:
        return False, "message samajh nahi aaya"

    if (data.get("product") is None
            and data.get("quantity") is None
            and data.get("payment_promise") is None):
        return False, "ye order nahi hai"

    if data.get("product") is None:
        return False, "product missing"

    if data.get("quantity") is None:
        return False, "quantity missing"

    if data.get("payment_promise") is None:
        return True, "payment ka zikr nahi hai"

    return True, None



def write_reply(message,data,ok,reason):
    prompt = f"""Customer ka message: {message}
Extracted data: {data}
Order theek hai: {ok}
Masla: {reason}
you are a message writer with polite tone in roman urdu 
Agar Masla "product missing" hai: sirf product poochho, quantity dobara mat poochho
“payment ka zikr nahi hai”: confirm karo aur poocho payment kab tak karenge
“quantity missing”: sirf quantity poocho
“ye order nahi hai”: order ki baat mat karo, kaho ki sawal owner ko pahuncha dete hain
dont promise any commitments like kal deliver kardenge or anything like that 
when Masla is None then confirm the order product, quantity repeat
only give Reply Output no extra stuff no explaination


"""
    return ask_llm(prompt)