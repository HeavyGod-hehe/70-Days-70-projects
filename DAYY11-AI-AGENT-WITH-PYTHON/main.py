from ai_service import get_ai_reply
from read import read_csv



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
    tool_used = False
    for step in reply.steps:
        if step.type == "function_call":
            tool_used = True
            file_path = step.arguments["file_path"]
            file_text = read_csv(file_path)
            chat_history.append({"role": "user", "content": f"Data from {file_path}:\n{file_text}"})
            final_reply = get_ai_reply(chat_history)
            print(final_reply.output_text)
            chat_history.append({"role": "model", "content": final_reply.output_text})

    if not tool_used:
        print(reply.output_text)
        chat_history.append({"role": "model", "content": reply.output_text})

            


    model_message = {
        "role":"model",
        "content" : reply
    }