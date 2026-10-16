def checker(name,amount):
    if amount is None:
        return(f"{name} Payment Amount is Missing")

def template(name,amount,day,mood):
    role = "You are a message Writer"
    task = """write(not send) One payment reminder message for the Customer Below
     Use Rupees instead of (₹) Symbol
    write in the roman urdu matching the base message
    keep it in 2 to 3 sentences 
    Write only in Roman Urdu using English letters, no Urdu script.
    make sure the output is only the message text with no headings labels or markdowns"""
    base_message = "Hello {name}, Apka {amount} rupay ka udhaar pending hai kindly Repay Before {day}"
    tone = "tone: {mood}"
    prompt = "\n".join([role, task, base_message, tone])
    return prompt.format(name=name, amount=amount,day=day,mood=mood)

def message(name,amount,day,mood):
    checking = checker(name,amount)
    if checking is not None:
        return checking
    text = template(name,amount,day,mood)
    return text
