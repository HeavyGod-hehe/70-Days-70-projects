# Day 3 — AI Text Cleaner

## Project overview

The AI Text Cleaner is a small terminal app that sends messy text to a Gemini model and asks it to clean the text while preserving its meaning and tone. The model returns a JSON response, and Python parses that response so the app can display the cleaned text and a list of changes.

This project is about more than making an API request. It practices writing precise prompts and turning an AI response into data a program can use.

## Why I built it

Text from quick notes or chat messages can contain spelling mistakes, inconsistent casing, missing punctuation, and unnecessary filler words. A cleaner can make that text easier to read while preserving what the writer meant.

The project also demonstrates a common AI application flow:

```text
User text → prompt instructions → model response → JSON parsing → useful program output
```

## What the app does

1. Reads text typed into the terminal.
2. Sends the text to the Gemini model with cleaning rules and an example.
3. Asks the model to return a JSON object with `cleaned_text` and `changes_made`.
4. Uses Python's `json.loads()` to parse the JSON text into a dictionary.
5. Displays the cleaned text and each reported change.

The intended response shape is:

```json
{
  "cleaned_text": "I think we should send it tomorrow.",
  "changes_made": [
    "Removed the filler word 'umm'.",
    "Corrected spelling and capitalization."
  ]
}
```

## Prompt rules

The prompt asks the model to:

- Fix spelling, grammar, casing, spacing, and punctuation.
- Remove unnecessary filler words.
- Preserve meaning, facts, and tone.
- Avoid adding information or rewriting more than needed.
- Preserve uncertain words rather than guessing.
- Return only valid JSON, with no tags or extra explanation.

The prompt uses `<user_text>` tags to show where the supplied text begins and ends. It also includes a few-shot example: a messy sentence paired with the desired cleaned result and JSON format.

## Project structure

```text
Day3-AI-Text-Cleaner/
├── ai_service.py   # Prompt, Gemini request, and JSON parsing
├── main.py         # Terminal input and display
└── .env            # API key; keep this private and out of version control
```

## What I built myself

- Reused the Gemini client setup from my earlier project.
- Adapted the AI service from summarization to text cleaning.
- Wrote and refined the cleaning instructions in the prompt.
- Added input boundary tags and a few-shot example.
- Changed the requested response from plain text to structured JSON.
- Stored the model's `output_text` and parsed it with `json.loads()`.
- Updated the terminal program to display `cleaned_text` and loop through `changes_made`.
- Ran the app with mixed casing, misspellings, and uncertain words, then used the output to refine the prompt.

## What I learned

### Prompt engineering

- A vague request such as “clean this text” can lead to inconsistent rewrites.
- Clear rules help set the transformation's scope and boundaries.
- Few-shot examples demonstrate the desired behavior and response format.
- Delimiters make it clearer which text is the user's input.
- Prompt changes should be tested against varied examples, including ambiguous words and mixed-language text.
- A prompt guides the model but does not guarantee that every response will follow the rules perfectly.

### Structured processing

- An SDK response object is different from the model's text output.
- The model's `output_text` contains JSON text; it is still a string at that point.
- `json.loads()` converts valid JSON text into Python data—in this project, a dictionary containing a string and a list.
- Python can then access `cleaned_text` and iterate through `changes_made` separately.
- JSON must be valid for parsing: keys and string values need double quotes, and list items need correct commas and brackets.

### Python and application flow

- The AI service belongs in `ai_service.py`; terminal input and presentation belong in `main.py`.
- A function's returned value must be stored and used by its caller; calling a function alone does not display its return value.
- A returned dictionary can be accessed by its keys, and its list values can be processed in a loop.
- API errors, such as rate limits, can happen before the model returns a response. They are separate from prompt and JSON parsing errors.

## What I asked and clarified

During the build, I asked how to:

- Mark the boundary around the input text and add a few-shot example.
- Return the model's `output_text` instead of the entire SDK response.
- Decide whether response handling belongs in `ai_service.py` or `main.py`.
- Ask for JSON with `cleaned_text` and `changes_made` fields.
- Parse the returned JSON and display each field in the terminal app.
- Understand a free-tier rate-limit error.

These questions helped clarify the difference between prompting the model, handling the API response, parsing data, and presenting the result.

## What I should focus on next

- **Protect meaning more carefully:** the model may infer missing words or remove content it considers redundant. Greetings and meaningful phrases should be preserved unless the user asks to remove them.
- **Handle ambiguity:** preserving an uncertain word is a useful rule, but the model may still interpret unfamiliar spellings differently. Test ambiguous examples explicitly.
- **Validate the response:** check that parsed JSON contains both expected keys and that `cleaned_text` is a string and `changes_made` is a list.
- **Handle failures gracefully:** catch API errors such as rate limits and malformed JSON so the app can show a short, useful message instead of a traceback.
- **Separate deterministic cleanup from AI judgment:** Python can reliably normalize some spacing or validate fields; the model is useful for context-sensitive grammar and rewriting.
- **Test the latest prompt revision:** the last punctuation refinement could not be verified because the API request hit the free-tier rate limit. An earlier version completed the full request, parsing, and display flow.

## How to run

From the project folder, activate the virtual environment, make sure the required packages are installed, and set `GOOGLE_API_KEY` in a private `.env` file. Then run:

```bash
python main.py
```

Do not commit or share the `.env` file or API key.

## Key takeaway

An AI feature becomes useful when its output fits the rest of the program. This project combined a carefully scoped prompt with JSON parsing and ordinary Python processing, while showing why model output still needs validation and testing.
