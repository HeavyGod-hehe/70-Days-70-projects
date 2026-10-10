def validate_data(data):
    for field in ["phone_model", "price", "pta_status"]:
        if data.get(field) is None:
            raise ValueError(f"{field} missing hai")

def validate_types(data):
       if not isinstance(data["price"],int):
              raise ValueError(f"{data['price']} is not Valid")
       if data.get("storage_in_gb")is not None and not isinstance(data.get("storage_in_gb"),int):
              raise ValueError(f"storage_in_gb {data.get('storage_in_gb')} should be an integer")
       if not isinstance(data["pta_status"], bool):
        raise ValueError(f"pta_status {data['pta_status']} should be True or False")