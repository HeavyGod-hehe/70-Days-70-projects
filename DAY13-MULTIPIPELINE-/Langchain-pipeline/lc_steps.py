from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import Optional
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

class OrderExtraction(BaseModel):
    product : Optional[str] = Field(None,description="Product name like atta or maida")
    quantity : Optional[int] = Field(None,description="Product Quantity like 20 bori or 10 bags")
    payment_promise : Optional[str] = Field(None,description="Payment Return Time Like Kal payment krwa dunga or ill pay after 2 days")

structured_llm = llm.with_structured_output(OrderExtraction)

def extract_order(message):
    return structured_llm.invoke(message)

    

def check_order(data):
    if data is None:
        return False, "message samajh nahi aaya"

    if (data.product is None
            and data.quantity is None
            and data.payment_promise is None):
        return False, "ye order nahi hai"

    if data.product is None:
        return False, "product missing"

    if data.quantity is None:
        return False, "quantity missing"

    if data.payment_promise is None:
        return True, "payment ka zikr nahi hai"

    return True, None






reply_prompt = ChatPromptTemplate.from_template("""You write short, polite replies for a flour mill in Roman Urdu.

Customer message: {message}
Extracted data: {data}
Order ok: {ok}
Problem: {reason}

Rules:
- If Problem is None: confirm the order and repeat the product and quantity (say "bori").
- If Problem is "payment ka zikr nahi hai": confirm the order and ask when they will pay.
- If Problem is "product missing": ask only for the product.
- If Problem is "quantity missing": ask only for the quantity.
- If Problem is "ye order nahi hai": do not mention any order, say the question will be passed to the owner.
- Never promise delivery times or anything on behalf of the owner.
- Reply in 1 or 2 short lines. Output only the reply.
""")

reply_chain = reply_prompt | llm | StrOutputParser()


def write_reply(message, data, ok, reason):
    return reply_chain.invoke({
        "message": message,
        "data": data,
        "ok": ok,
        "reason": reason,
    })