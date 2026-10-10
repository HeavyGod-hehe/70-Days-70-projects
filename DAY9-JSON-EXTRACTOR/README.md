# AI JSON Extractor

Turn messy, human-written text into clean, validated, structured data using an LLM (Gemini) and plain Python.

Part of my **70 Days, 70 AI Projects** series. Written by hand, with an AI mentor guiding me step by step instead of writing the code for me.

---

## What this project does

You type (or paste) a messy description of a used phone, the way a seller would write it on WhatsApp or OLX:

```
iphone 13 pro, 185000 rupees, PTA approved, 256gb, blue, battery 87%, Faisalabad, box and charger included
```

The program:

1. Sends the text to Gemini with a strict extraction prompt and a fixed schema
2. Cleans the reply (removes the ```` ```json ```` fences the model likes to add)
3. Parses the cleaned text into a real Python dictionary
4. Validates that required fields exist and that every value has the right type
5. Prints the result, or a clear error message if something is wrong

Example of the kind of result (illustrative):

```python
{
  "phone_model": "iPhone 13 Pro",
  "storage_in_gb": 256,
  "color": "blue",
  "battery_health": 87,
  "accessories": ["box", "charger"],
  "pta_status": True,
  "used_for_months": None,
  "price": 185000,
  "location": "Faisalabad"
}
```

### The schema

| Field | Type | Required? |
|---|---|---|
| `phone_model` | str | Yes |
| `price` | int | Yes |
| `pta_status` | bool | Yes |
| `storage_in_gb` | int or None | No |
| `color` | str or None | No |
| `battery_health` | int or None | No |
| `accessories` | list or None | No |
| `used_for_months` | float or None | No |
| `location` | str or None | No |

Missing information must come back as `null` (`None`), never guessed.

---

## Project structure

```
ai_service.py   -> talks to Gemini (prompt + API call)
clean.py        -> clean_output() and parse_output()
validation.py   -> validate_data() and validate_types()
main.py         -> runs the whole pipeline
```

Pipeline flow:

```
user text -> extract_json -> clean_output -> parse_output -> validate_data -> validate_types -> result
```

One file, one job. Each step takes the output of the previous step.

---

## How to run

```bash
pip install google-genai python-dotenv
```

Create a `.env` file in the project folder:

```
GOOGLE_API_KEY=your_key_here
```

Run:

```bash
python main.py
```

---

## What I learned from this project

**Concepts**
- **Extract vs generate.** At first I thought I should ask Gemini to "give me iPhone data". The real job is to give it *my* text and make it pull the data out of it. Extraction works on input; generation invents.
- **LLM output is just a string.** `result["price"]` fails on a string. The model's reply has to be cleaned and parsed before it is usable data.
- **LLMs are not predictable.** Sometimes the reply has code fences, sometimes not, sometimes the JSON is broken. That is why cleaning, parsing and validation exist as separate steps, even if it "works" once.
- **Strings are immutable.** `.replace()` and `.strip()` return a new string. If you don't store it, nothing changes.
- **`.get("key")` vs `["key"]`.** `.get` gives `None` for a missing key, `[]` raises `KeyError`. I tested both myself to see the difference.
- **`return` vs just checking.** A validation function that only raises errors is different from a function that returns data. Knowing which one a function does decides how `main.py` uses it.
- **`bool` is a subclass of `int` in Python.** `isinstance(True, int)` is `True`. I spotted this myself while writing type checks.
- **Required vs optional is a design decision.** I chose which fields must exist (`phone_model`, `price`, `pta_status`) and which can be `None`.
- **Why separate functions at all.** Even when the code "already works", small reusable functions are easier to test, fix and reuse.
- **Reading tracebacks.** I fixed `data.get[...]` and `data.get([...])` mistakes by reading the error instead of asking for the answer.
- **Splitting code into files** and importing between them, including fixing an `ImportError` on my own.

**Skills used**
- Wrote prompts with a schema, strict rules and "return null if missing"
- `try/except` for `JSONDecodeError` and `ValueError`
- Wrote a mini test with a fake fenced string to check the cleaner

---

## What I did NOT fully learn yet (honest list)

- Syntax still slips: brackets vs parentheses, calling a function after defining it, variable names that shadow each other
- Variable scope: knowing which function has access to which data
- I needed help writing parts of `validate_data` and the `pta_status` check
- Return value vs side effect is clearer now but not automatic yet
- I have not rebuilt this project from memory yet

## Known limitations of the current code

- `validate_types` only checks `price`, `storage_in_gb` and `pta_status`. The other fields (`battery_health`, `used_for_months`, `color`, `accessories`, `location`) are not type-checked yet
- `price` and `storage_in_gb` accept `True`/`False` because `bool` passes the `int` check. A stricter check should reject `bool` first
- If the model returns valid JSON that is not a dictionary (for example a list), `.get()` would crash with an error that is not caught
- API errors (network, quota, key problems) are not handled in `ai_service.py`
- The model can still misread messy text. Validation checks the *shape* of data, not whether it is *true*

---

## What previous projects I reused

| From | What I reused here |
|---|---|
| **Summarizer (Day 1)** | Gemini API setup, `.env` for the API key, the `ai_service.py` pattern for the LLM call |
| **Chatbot (Day 2)** | Handling model replies as text and passing user input to the model |
| **Data Analyzer (Day 5)** | Keeping `ai_service.py` for the LLM and doing the data work in a separate part of the project |
| **Text Classifier (Day 7)** | Cleaning model output before using it, separate cleaning file, `main.py` as the controller |
| **Python basics** | Dictionaries, lists, `isinstance`, f-strings, functions, `try/except` |

---

## What I'm aiming to learn in the next projects

1. **FastAPI + LLM (AI API Service).** Turn this kind of pipeline into an API endpoint other apps can call
2. **Pydantic.** Replace my hand-written `validate_data` and `validate_types` with schema models that validate automatically. Doing it manually first means I now understand what Pydantic does for me
3. **Structured output from the model itself.** Ask the API to return JSON in a given schema instead of cleaning fences from plain text
4. **Better error handling.** Catch API errors, bad JSON shapes and retry when the model fails
5. **Writing code without help.** Build the next function from memory first, then check, instead of asking for code when I'm stuck or tired
6. **Testing.** Move from manual test strings to simple automated tests

---

## Tech

- Python
- Google Gemini via `google-genai`
- `python-dotenv`

---

*Day 9 of my 70 Days, 70 AI Projects journey. Built in public, mistakes included.*
