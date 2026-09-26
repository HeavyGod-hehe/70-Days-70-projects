AI Email Assistant — Day 4 (70 Days 70 Projects)
What This Tool Does

You type a rough instruction — like "tell HR I'm not feeling well today" — and the tool returns a complete, professional email as structured data: a subject, body, tone, and category, each accessible as its own field, not buried in a wall of text.

Example:

Input:  "send this mail to HR saying that i am not feeling good today, my wife's birthday is today"

Output:
  subject:  Absence Notification - Taking Leave Today
  body:     Dear HR Team, Please accept this email as notification...
  tone:     Professional
  category: Leave Notification
Why We Built It

This is Day 4 of a 70-day AI Engineering roadmap. Days 1–3 taught prompting, chat memory, and text cleaning — all cases where the AI's reply was just text a human reads. Day 4's whole point was learning to treat an AI's output as data your code can depend on, not prose a human has to parse by eye. That shift — free text → structured, validated data — is the foundation for almost every real AI product built later in the roadmap (APIs, agents, RAG systems).

How It Was Built

Stack: Python, google-genai SDK (Gemini), Pydantic, python-dotenv

Structure:

Day5-AI-Email-Assistant/
├── main.py        # takes user input, calls the AI service, prints the result
├── ai_service.py  # connects to Gemini, sends the prompt, enforces structured output
├── schemas.py     # defines the exact shape of the output (Pydantic model)
└── .env           # GOOGLE_API_KEY (not committed)

How it works:

schemas.py defines EmailOutput, a Pydantic model with subject, body, tone, category — this is the contract for what a valid response looks like.
ai_service.py builds a prompt from the user's raw input and calls client.models.generate_content() with config=GenerateContentConfig(response_mime_type="application/json", response_schema=EmailOutput) — this forces Gemini to return JSON matching that exact schema.
The SDK auto-validates and parses the response into a real EmailOutput object (response.parsed) — no manual JSON parsing needed.
main.py prints each field individually, proving the output is genuinely structured, not just JSON-shaped text.
What We Learned
Structured output enforcement — forcing an LLM to return data matching a fixed schema instead of free-form prose (new skill this project)
Pydantic BaseModel vs BaseSettings — BaseModel validates data shapes flowing through the app; BaseSettings is for config/env variables. Easy to confuse, different jobs entirely.
Reading tracebacks as information, not noise — a 503 error (server overloaded) and a 404 error (deprecated model) look similar in a stack trace but mean completely different things; the actual fix is at the bottom line, not the top.
The Interactions API exists — Google recently introduced a newer client.interactions.create() API alongside the older client.models.generate_content(). Both work; generate_content() with a current model name was what actually shipped this version.
Don't trust any single source blindly — including AI explanations. Partway through this project, Claude confidently told Abdul that client.interactions.create() wasn't a real method. Abdul pushed back based on his own testing, and it turned out Claude was working from outdated knowledge — the method is real. Verifying against actual error messages and real runs settled it, not confidence in tone.
How Much AI Help Was Used

Heavy guidance throughout — this was a guided build, not a solo build. Claude explained concepts (structured output, Pydantic model types, the config pattern), pointed out bugs without handing over full solutions, and asked leading questions to make Abdul write the actual code himself. Abdul wrote every line of the final code, ran it, read the errors, and fixed most issues based on those questions — including catching a real mistake Claude made along the way.

Self-Assessment — Where Abdul Is Right Now

Rating: Advanced Beginner, trending upward.

What went well:

Actually ran the code and pasted real tracebacks instead of guessing — this is a habit many beginners skip, and it's the single most useful debugging skill there is
Caught and questioned an incorrect claim from Claude instead of accepting it — this is not typical beginner behavior; it shows genuine engagement with what the code is actually doing, not just following instructions
Reused working patterns from Day 1 correctly (API key setup, client connection) without needing to re-learn them

What's still developing:

Mixed up BaseModel/BaseSettings and input=/contents= — both understandable, both fixed once explained, but these are recall gaps rather than conceptual ones (the "recall build" stage of the learning loop will help close these)
Initial prompt for this project accidentally reused last project's instructions (text-cleaning language instead of email-writing language) — a sign of copy-adjacent building rather than building from a clear mental model of this task's goal. Worth double-checking "what am I actually asking the AI to do" before writing the prompt, next time.

Compared to the habit-tracker project (where the note was "harder without ChatGPT breaking it down"), this run shows more independent debugging and more willingness to question given answers — that's real forward movement, not just more repetitions of the same pattern.