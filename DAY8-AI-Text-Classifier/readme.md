🏷️ AI Text Classifier (Day 8 / 70)

Part of my 70 Days, 70 Projects AI engineering roadmap.

A terminal tool that reads customer messages written in English, Urdu or Roman Urdu, uses Gemini to classify each one into a fixed label, and lets you browse the results by label.

Labels
Label	Meaning
complaint	Unhappy customer, broken or bad product
order_query	Price, availability, delivery or order questions
payment_issue	Payment failed, charged twice, money not received
praise	Customer is happy and appreciating us
promotional	PR, collaboration or networking offers
misc	Anything unclear (fallback)
error	The API call failed (not a real category, just a signal)
How it works
message -> classify_text() -> raw Gemini output -> clean_label() -> stored result -> menu
File	Job
ai_service.py	Builds the prompt, calls Gemini (temperature 0.1), returns the raw label or None if the API fails
cleaning.py	Turns messy model output ("Complaint.", "  praise\n", "**order_query**") into a valid label, falls back to misc / error
main.py	Classifies 10 sample messages, counts labels, shows an interactive menu
Setup
bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-genai python-dotenv

Create a .env file (and keep it in .gitignore):

GOOGLE_API_KEY=your_key_here

Run:

bash
python main.py
Example output
Bhai 3 din pehle order kiya th -> complaint
Aoa, mera order #45892 kab tak -> order_query
I was charged twice for my sub -> payment_issue
Zabardast quality! Packing bhi -> praise
Exclusive Weekend Sale! Get fl -> promotional

--- MENU ---
1 : complaint (2)
2 : praise (2)
3 : order_query (3)
...
0 : Exit
What I learned
The prompt is the product. Fixed labels, a clear output rule and few-shot examples matter more than any code trick.
Model output is untrusted text. Even with "return only the label", it can come back with punctuation, spaces or markdown. Always clean and validate against an allowed list.
Always have a fallback. Anything that is not an allowed label becomes misc.
Failures need their own signal. A failed API call must not look like misc, so it gets its own error label.
Low temperature for classification. Same input should give the same answer.
Small bugs hide big problems. One label spelled two ways (promotional vs promotional_message) would have silently sent every promo message to misc.
<!-- TODO (Abdul, in your own words): one thing you understood today that you could not explain a week ago -->
Known limitations
Only 10 sample messages, so accuracy is not measured yet.
The prompt has no misc example, so the model rarely uses misc. One test message ("OTW... order chai ☕") was labelled order_query.
"Order is late" can be either complaint or order_query. That is a business decision the prompt does not make yet.
Messages are classified one by one (slow for large batches).
Next steps
Add a misc example and decide the "late order" rule
Build a small labelled test set and measure accuracy
Read messages from a CSV instead of a hardcoded list

Built with AI assistance as a learning aid, with the code written and debugged by me.