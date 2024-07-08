from flask import json


def Message(code, message):
    msgtxt = "{\"status\":\"" + \
        str.lower(str(code)) + "\", \"message\":\"" + message + "\"}"
    return json.jsonify(msgtxt)
