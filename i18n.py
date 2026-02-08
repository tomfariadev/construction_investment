import json
import os

def get_translations(lang="en"):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "locales", f"{lang}.json")

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
