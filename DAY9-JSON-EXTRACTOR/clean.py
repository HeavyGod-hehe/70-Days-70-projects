import json



def clean_output(raw):
        if not raw :
                raise ValueError("Value is Empty")
        data = raw.replace("```", "")
        data = data.strip()
        data = data.removeprefix("json")
        data = data.strip()
        return data


def parse_output(clean_text):
        try:
                return json.loads(clean_text)
        except json.JSONDecodeError:
                raise ValueError("The Data is not JSON")