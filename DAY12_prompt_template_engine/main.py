from template_engine import checker,template
from ai_service import message_writer_ai



customers = [
    {"name": "Ahmed", "amount": 15000, "day": "Friday", "mood": "polite"},
    {"name": "Bilal", "amount": None, "day": "Monday", "mood": "strict"},
    {"name": "Sana", "amount": 7500, "day": "Sunday", "mood": "friendly"},
    {"name": "Usman", "amount": 22000, "day": "Wednesday", "mood": "polite"},
    {"name": "Hina", "amount": None, "day": "Tuesday", "mood": "friendly"},
]
def run_reminders(customers):
    for customer in customers:
        result = checker(customer["name"],customer["amount"])
        if result is not  None:
            print(result)
            continue
        prompt = template(customer["name"],customer["amount"],customer["day"],customer["mood"])
        reply = message_writer_ai(prompt)
        print(reply)




if __name__ == "__main__":
    run_reminders(customers)