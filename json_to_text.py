import os
import json

def convert_json_to_txt(json_path):
    if not os.path.exists(json_path):
        print(f"❌ File not found: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Get a flat string version of all values
    content = []
    for key, value in data.items():
        content.append(f"{key.upper()}:\n{value.strip()}\n")

    txt_path = json_path.replace(".json", ".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"✅ Converted to TXT: {txt_path}")


# Example usage
convert_json_to_txt("data/versions/Chapter_1.json")
