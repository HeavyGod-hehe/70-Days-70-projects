from ai_service import get_ai_reply












chat_history = []

while True:
    user_message = input("Work With GOSHUGPT : ").strip()
    if user_message.lower() == "exit":
        print("GoodBye from GoshuGpt!")
        break


    if user_message.lower() == "clear":
        chat_history.clear()
        print("conversation memeory cleared")
        continue    


    message = {
        "role" : "user",
        "content" : user_message
    }


    chat_history.append(message)

    reply = get_ai_reply(chat_history)

    print("GOSHUGPT", reply)

    model_message = {
        "role":"model",
        "content" : reply
    }

    chat_history.append(model_message)