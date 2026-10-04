# Day 7: AI Web Page Analyzer

A terminal app that takes a URL, scrapes the page, and uses Gemini to produce a short summary, the main topics, and the purpose of the page.

```
URL -> requests fetches HTML -> BeautifulSoup extracts title, headings, text
    -> trim text -> Gemini (AI_service.py) -> summary printed
```

## What this program does

You give it a web page address. It downloads the page, pulls out the important parts (title, headings and main text), cleans and shortens that text, and asks Gemini to analyze it. You get back a short summary, the main topics, and the purpose of the page, so you can understand a long page in seconds without reading it all.

It runs in a loop, so you can analyze one page after another. If a URL is wrong, a site blocks the request, or the AI service is busy, it shows a message and asks for the next URL instead of crashing. It stops only when you type `exit`.

## Why this project mattered for practice

This project was built as practice for my Python automation and AI application roadmap (Day 7 of my 70 Days, 70 Projects challenge). It was useful because it put several real-world skills into one small app:

- **HTTP + scraping + LLM in one pipeline.** This is the same pattern behind many real tools: get data from the web, clean it, and hand it to an AI model.
- **Reusing earlier work.** The Gemini service (`AI_service.py`) builds on my earlier days, which showed me how to write code that can be reused.
- **Handling things that go wrong.** Real websites and APIs fail all the time (404, blocked requests, timeouts, 502/503). Learning to guard against `None` and keep the program running is the difference between a script and a usable tool.
- **Splitting code into small files.** Fetching, extracting, AI and the main loop each have their own file, which makes bugs easier to find.
- **Writing prompts as part of the code.** The prompt tells the model its task and keeps the page content as data only.
- **Practice I can build on.** The same skills apply to later projects such as automation tools, client work and freelancing.

## Features

- Fetches any public web page with a timeout and a browser-style User-Agent
- Extracts the title, headings and body text with BeautifulSoup
- Trims long pages (`MAX_CHARS`) before sending them to the model
- Sends the content to Gemini with a prompt that treats the page as data, not instructions
- Keeps running until you type `exit`, and recovers from bad URLs and API errors without crashing

## Project structure

| File | Job |
|------|-----|
| `fetcher.py` | `fetch_page(url)`: HTTP request, status check, error handling |
| `extractor.py` | `extract_title`, `extract_headings`, `extract_text`, `trim_text` |
| `AI_service.py` | `Analyze(title, headings, text)`: builds the prompt, calls Gemini, handles API errors |
| `main.py` | The input loop that connects everything |

## Setup

```bash
pip install requests beautifulsoup4 google-genai python-dotenv
```

Create a `.env` file in the project folder:

```
GOOGLE_API_KEY=your_key_here
```

Make sure `.env` is listed in `.gitignore` so your key never reaches GitHub.

## Run

```bash
python main.py
```

Paste a URL and press Enter. Type `exit` (any capitalization) to quit.

## What I learned

**Web scraping**
- `requests.get()` returns a response with a `status_code` and `.text`; always check it before using the HTML.
- `timeout` stops the program from hanging forever, and a `User-Agent` header stops many sites from rejecting the request.
- `raise_for_status()` turns 404/403/500 into errors I can catch instead of analyzing an error page.
- `BeautifulSoup(html, "html.parser")` makes HTML searchable, and `.find()` / `.find_all()` pull out specific tags.
- `soup.title` is `None` when a page has no title, so calling `.text` on it crashes. Every `None` needs a guard.

**Working with an LLM API**
- A function that does not `return` gives back `None` silently, so `main.py` receives nothing.
- A prompt needs a task, not just a role. Labels on separate lines make the data clearer.
- Library errors are library-specific: `requests` exceptions do not catch `google-genai` errors (`errors.APIError`), and I still need a general `except Exception` for network failures.
- 5xx errors (502/503) are temporary server-side problems, not bugs in my code.
- Trimming is a trade-off between speed, cost and focus, not a fixed rule. `MAX_CHARS` lives in one constant so it is easy to tune.

**Python habits**
- Keyword arguments (`Analyze(title=title, headings=headings, text=text)`) prevent mixed-up argument order, which was a real bug I had.
- `break` ends the whole loop; `continue` skips only the current round.
- `if not url: continue` stops an empty input from travelling through the whole pipeline.
- `.strip().lower()` makes the exit check work for "Exit", "EXIT" and " exit ".
- Do not name a file or variable after a built-in module (`html` clashed with Python's own `html`).

## How I used AI to build this

I used Claude as a tutor, not as a code generator.

- It explained each concept first, then I wrote the code myself, step by step.
- I wrote `main.py` and the loop logic on my own, then pasted my code and output for review.
- Claude pointed out bugs and asked me to design the fix (for example, which guard goes first and what a function should return on failure) instead of handing over the answer.
- When I did not understand something (why trim, why `continue`, how to decide what goes where), I asked until it made sense instead of copying it.
- I used AI help for the error handling pass, and the rest I wrote myself.
- The project itself uses Gemini as the analysis engine, so this is also my first "scraping + LLM" pipeline.

## Next improvements

- Retry once or twice on 5xx errors before giving up
- Fix the output format in the prompt (short summary, 4-5 bullets, one-line purpose)
- Cut the trimmed text at a sentence boundary instead of mid-sentence
- Handle pages with no extractable text (JavaScript-heavy sites)