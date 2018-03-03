import json


def is_json(string):
    try:
        jsonobj = json.loads(string)
    except ValueError:
        return False
    return True