from ai_service import extract_json
from clean import clean_output,parse_output
from validation import validate_data,validate_types




text = input("Write The Details of your Phone \n Model,price,pta status,storage,color,batteryhealth,location,accessories:")
def main():
    try:
        data_extract = extract_json(text=text)
        cleaned_data = clean_output(data_extract)
        dict_data = parse_output(cleaned_data)
        validate_data(dict_data)
        validate_types(dict_data)
        print(dict_data)
    except ValueError as e:
        print("Error",e)




main()

