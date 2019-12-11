import json


def is_json(json_data):
    print("Validating json data: " + str(json_data))
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid