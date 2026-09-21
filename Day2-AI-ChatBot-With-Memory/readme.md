# Day 2 — AI Chatbot With Memory

A terminal-based chatbot powered by Gemini that remembers the conversation while the program is running.

## What it does

The chatbot allows a user to have a multi-message conversation with GOSHUGPT.

It supports:

- Normal messages — sends the message to Gemini and returns a reply
- `clear` — removes the current conversation memory
- `exit` — closes the chatbot

## How it works

```text
User message
    ↓
Store message in chat_history
    ↓
Send the complete conversation history to Gemini
    ↓
Receive Gemini's reply
    ↓
Display reply
    ↓
Store Gemini's reply in chat_history
    ↓
Repeat
```

The conversation memory only lasts while the program is running. When the program closes, the list is cleared.

## Project structure

```text
Day2-AI-ChatBot-With-Memory/
├── main.py
├── ai_service.py
└── README.md
```

## What I learned

- How multi-turn AI conversations work
- The difference between a one-time AI request and a conversation with memory
- How to store messages in a Python list
- How to use dictionaries to organize each message with a `role` and `content`
- Why user messages and AI replies must both be saved
- How a `for` loop can process every item in a conversation history
- How to send conversation context to Gemini
- How to use `while True` for a continuously running terminal application
- How `break` and `continue` control the chatbot flow
- Why separating `main.py` and `ai_service.py` makes an application easier to understand

## How I built it

I first created an empty `chat_history` list.

Each user message is saved as a dictionary with:

```text
role: user
content: the user's message
```

Gemini's reply is also saved in the same list with the `model` role.

Before Gemini answers, the application turns the stored messages into readable conversation context. This lets Gemini use earlier messages when answering a new one.

## How AI helped me learn

I built this project step by step instead of copying a complete application.

AI helped me:

- Understand the difference between `while` loops and `for` loops
- Understand why chat history needs a list of dictionaries
- Fix errors such as missing function arguments
- Learn why `main.py` should pass data to `ai_service.py`
- Avoid circular imports
- Understand why Gemini needs the previous conversation as context
- Test the application gradually before connecting the real Gemini API

## Example conversation

```text
Work With GOSHUGPT: My name is Abdulrehman
GOSHUGPT: Nice to meet you, Abdulrehman!

Work With GOSHUGPT: What is my name?
GOSHUGPT: Your name is Abdulrehman.

Work With GOSHUGPT: clear
Conversation memory cleared.

Work With GOSHUGPT: exit
Goodbye from GOSHUGPT!
```

## Tech used

- Python
- Gemini API
- `google-genai`
- `python-dotenv`
- Environment variables for API-key security

## Next step

Day 3 will introduce another AI-engineering concept and build on the foundations from Days 1 and 2.