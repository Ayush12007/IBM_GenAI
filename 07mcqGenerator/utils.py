import json
import re

def extract_mcqs_from_response(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Try to extract the list manually
        match = re.search(r"\[.*\]", content, re.DOTALL)
        if match:
            json_text = match.group(0)
            try:
                return json.loads(json_text)
            except:
                return None
    return None
