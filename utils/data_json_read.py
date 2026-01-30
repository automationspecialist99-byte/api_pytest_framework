import json
def json_data_read(path):
    with  open("data"+"/"+path) as file:
        payload=json.load(file)
    return payload
