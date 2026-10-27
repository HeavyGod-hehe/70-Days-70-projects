# Mini AI Assistant (CSV Reader Agent)

Ek chhota AI assistant jo khud decide karta hai ki jawab dene ke liye file padhni hai ya nahi. Gemini LLM + ek Python tool + chat history se bana hai.

**Example:** "Who Owns Me Money" poochho, assistant `mill_sales.csv` khud padhta hai aur batata hai kis customer ka udhaar baaki hai.

## Chatbot vs Assistant
- **Chatbot:** sirf baat karta hai (dimaag).
- **Assistant:** baat + kaam karta hai (dimaag + haath, yaani tools).

## Kaise kaam karta hai (flow)
1. User sawal poochta hai.
2. Sawal `chat_history` mein jaata hai aur Gemini ko bheja jaata hai.
3. Gemini ya to seedha jawab deta hai, ya **tool maangta hai** (`CSV_reader` + `file_path`).
4. main.py tool chalata hai (`read_csv`) aur file ka text history mein jodta hai.
5. Gemini ko dobara bulaya jaata hai, ab usko data dikhta hai.
6. Final jawab print hota hai aur history mein save hota hai (taaki agla sawal yaad rahe).

## Files ka breakdown

| File | Kaam |
|------|------|
| `read.py` | Tool. File ka path leta hai, poora text string mein wapas deta hai. File na mile to crash nahi hota, saaf message return karta hai jisme file ka naam hota hai. |
| `ai_service.py` | Gemini se baat. Isme tool ka **declaration** hai (naam, kaam, input) aur `get_ai_reply` jo history ko prompt banakar Gemini ko bhejta hai aur poora jawab (`data`) wapas deta hai. |
| `main.py` | Dimaag ka controller. User se sawal leta hai, Gemini ka jawab check karta hai (`function_call` step hai ya nahi), tool chalata hai, history sambhalta hai. |
| `mill_sales.csv` | Sample data: mill ki sales, customer, kg, rate, Paid (Yes/No). |
| `.env` | API key (`GOOGLE_API_KEY`). **GitHub par kabhi push nahi karni.** |

## Zaroori concepts

- **Tool declaration:** LLM code nahi dekh sakta, sirf tool ka description dekhta hai (name, description, parameters). Jitna saaf description, utna sahi tool use.
- **Nested dictionary (parameters):** tool ka "form" hai. Har input ek alag line hai `properties` mein, kisi doosre input ke andar nahi.
- **Tool ka input = sirf path**, kyunki LLM file nahi, sirf text bhej sakta hai.
- **LLM tool khud nahi chalata.** Woh sirf maangta hai (`function_call`), asli kaam hamari script karti hai.
- **`steps` list:** Gemini ke jawab mein kai steps hote hain (`thought`, `function_call`). Sirf `function_call` wala step tool maangta hai.
- **Chat history = yaad.** LLM ko har baar naya dimaag milta hai, isliye sawal, tool ka result aur apna jawab sab history mein bhejna padta hai.
- **Error ko return karo, print nahi.** LLM tak message `return` se pahunchta hai, `print` se nahi.

## Chalane ka tareeka
1. `pip install google-genai python-dotenv`
2. `.env` file banao: `GOOGLE_API_KEY=your_key`
3. `mill_sales.csv` ko `main.py` ke saath rakho.
4. `python main.py`
5. Poocho: "Who Owns Me Money", phir "Sabse bada udhaar kis ka hai?"

## Baaki kaam (next steps)
- Loop ki **5 tries limit** (tool baar-baar maangta rahe to ruk jaye).
- API error handling (`try/except`).
- Kai tools (jaise udhaar total nikalne wala tool).
- `previous_interaction_id` se Gemini ka khud yaad rakhna seekhna.
- `.gitignore` mein `.env` aur `.venv` daalna.
