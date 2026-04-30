import json

def parse_plan(text):
    try:
        return json.loads(text)
    except:
        return {"task": text}
