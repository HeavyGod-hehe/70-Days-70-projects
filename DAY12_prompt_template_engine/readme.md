# Day 12 — Prompt Template Engine

Part of my 70 Days 70 Projects AI Engineering challenge.

## What this does

Generates personalized payment reminder messages for a list of customers using Gemini, with validation to make sure incomplete customer data never reaches the AI.

## The problem it solves

Writing a one-off AI prompt works for one customer. It doesn't scale to 100 customers with different names, amounts, and due dates. This project turns one well-written prompt into a reusable template with blanks, filled in automatically for each customer, with a validation check before any AI call is made.

## Files

- **template_engine.py** — `checker()` validates a customer has a payment amount; `template()` fills a 4-part prompt (role, task, base message, tone) with that customer's details.
- **ai_service.py** — `message_writer_ai()`, a single function that sends a finished prompt to Gemini and returns just the reply text.
- **main.py** — holds the customer data and `run_reminders()`, which loops through customers, checks each one, and either prints an AI-written reminder or flags a missing amount.

## How it works

1. For each customer, `checker()` runs first. If their amount is missing, it returns an error message and that customer is skipped — no AI call happens.
2. If the amount is present, `template()` fills the prompt's blanks (`{name}`, `{amount}`, `{day}`, `{mood}`) with that customer's real values.
3. The filled prompt is sent to Gemini via `message_writer_ai()`, which returns a clean, ready-to-send reminder message in that customer's tone.

## Example

**Input customer:** Ahmed, 15,000 rupees, due Friday, polite tone

**Output:**
> Hello Ahmed, apka 15000 rupay ka balance pending hai, agar mumkin ho toh kindly Friday tak repayment kar dein. Shukriya.

**Input customer:** Bilal, amount missing

**Output:**
> Bilal Payment Amount is Missing *(no AI call made)*

## How to run

\`\`\`
python main.py
\`\`\`

Requires a `.env` file with `GOOGLE_API_KEY` set.

## What I learned

- Why `f-strings` fill blanks immediately, while a plain string left for `.format()` stays reusable
- Separating validation, templating, and the AI call into their own functions makes each one easy to debug alone
- A prompt's wording directly controls output format — strict formatting rules in the `task` string were needed to stop the AI from adding labels and markdown