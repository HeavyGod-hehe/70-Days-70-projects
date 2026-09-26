from ai_service import Email


U_input = input("Type What you want to Write in the mail and who to send : ")

result = Email(U_input)
# print(result.text)
print(f"Hey Here is your Email \n Subject {result.subject} \n {result.body} \n {result.tone} \n {result.category} ")