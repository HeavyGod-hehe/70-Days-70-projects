def read_csv(file_path):
    try:
        with open(file_path,"r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return (f"Please Choose the Correct Path {file_path} not found ")
