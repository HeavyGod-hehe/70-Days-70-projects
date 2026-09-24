from ai_service import clean_text



text = input("Type Your Text : ")
result = clean_text(text)
print(result["cleaned_text"])
for changes in result["changes_made"]:
    print(changes)