from ai_service import classify_text
from cleaning import clean_label,ALLOWED_LABELS


messages = [
    "Bhai 3 din pehle order kiya tha abhi tak dispatch nahi hua, bohot buri service hai aapki.",
    "I received a damaged item today. The box was crushed and the screen is completely broken.",
    "Aoa, mera order #45892 kab tak deliver hoga? Tracking link update nahi ho raha.",
    "Hello, can you please confirm if size M is available for this blue denim jacket?",
    "Mera account se paise kat gaye hain lekin checkout par payment failed ka error aa raha hai.",
    "I was charged twice for my subscription this month. Please refund the duplicate payment.",
    "Zabardast quality! Packing bhi bohot acchi thi aur delivery bhi 2 din mein ho gayi. Thank you!",
    "Exceptional customer support! Sarah helped resolve my issue within five minutes.",
    "OTW 🚗💨 | system_status: `delayed` | 15 mins mein pohanch raha hoon, order chai! ☕",
    "Exclusive Weekend Sale! Get flat 50% OFF on all winter wear. Use code SAVE50 at checkout."
]

classified_result = []

for message in messages:
     text = classify_text(message)
     clean_text = clean_label(text)
     print(message[:30], "->", clean_text)
     saved_data = {
          "text":message,
          "label":clean_text
     }
     classified_result.append(saved_data)
counts = {}
for item in classified_result:
    label = item["label"]
    counts[label] = counts.get(label, 0) + 1



menu_labels = ALLOWED_LABELS + ["error"]

while True:
    print("\n--- MENU ---")
    for i, label in enumerate(menu_labels, 1):
        print(f"{i} : {label} ({counts.get(label, 0)})")
    print("0 : Exit")

    choice = input("Konsa label dekhna hai? ")

    if choice == "0":
        print("Allah Hafiz!")
        break

    try:
        number = int(choice)
    except ValueError:
        print("Galat choice, number likho")
        continue

    if number < 1 or number > len(menu_labels):
        print("Galat choice, menu me se number chuno")
        continue

    selected_label = menu_labels[number - 1]
    matches = [item for item in classified_result if item["label"] == selected_label]

    print(f"\n{selected_label}: {len(matches)} messages")
    for item in matches:
        print("-", item["text"])