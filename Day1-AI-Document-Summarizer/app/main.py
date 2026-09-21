from ai_service import summarize








def selection():
    while True:
        choice = input("What you want to summarize \n 1 : Sample or \n 2 : Enter Text  or \n 3 : Exit : : ")
        if choice == "1":
            file_path = input("Enter the path of your document: ")
            try:
                with open(file_path,"r") as file:
                    content = file.read()
                    return content
            except FileNotFoundError:
                print("Please Choose the Correct Path  ")
        elif choice == "2":
            user_text = input("type your question here : ")
            return user_text
        elif choice == "3":
            exit()
        else:
            print("Select a Valid Option")

        
result = summarize(selection())
print(result.output_text)
