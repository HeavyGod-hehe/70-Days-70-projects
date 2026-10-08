ALLOWED_LABELS = ["complaint","praise","order_query","payment_issue","misc","promotional"]
def clean_label(raw_output):
    if raw_output is None:
        return "error"
    clean_text = raw_output.strip("\n * . , ' $")
    text =clean_text.lower()
    if text in ALLOWED_LABELS:
        return text
    else:
        return "misc"



if __name__ == "__main__":
    print(clean_label("Complaint."))
    print(clean_label("  praise\n"))
    print(clean_label("**order_query**"))
    print(clean_label("promotional"))
    print(clean_label(None))
    print(clean_label("I think it is a complaint"))