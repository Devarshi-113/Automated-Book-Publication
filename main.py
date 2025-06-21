from utils.scraper import scrape_chapter
from agents.writer import generate_spin
from agents.reviewer import review_text
from agents.editor import final_edit
from embeddings.embedder import get_embedding
from storage.chroma_client import store_version
from utils.file_io import save_raw_html, save_screenshot
import os
import json


import json
import os

def convert_json_to_txt(json_path):
    import json, os
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    content = []
    for key, value in data.items():
        content.append(f"{key.upper()}:\n{value.strip()}\n")

    txt_path = json_path.replace(".json", ".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"Converted to text: {txt_path}")



def run_pipeline(url):
    html_path, screenshot_path = scrape_chapter(url)
    with open(html_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # save_raw_html(url, raw_text)
    # save_screenshot(url)

    spun = generate_spin(raw_text)
    reviewed = review_text(spun)
    final = final_edit(reviewed)

    # Save final version to JSON
    chapter_name = "Chapter_1"
    output_path = os.path.join("data", "versions", f"{chapter_name}.json")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "chapter": chapter_name,
            "original": raw_text,
            "spun": spun,
            "reviewed": reviewed,
            "final": final
        }, f, indent=2, ensure_ascii=False)

    print(f"Pipeline Completed. Final version saved to {output_path}")

    # ✅ Add this line to convert JSON to TXT
    convert_json_to_txt(output_path)

# def run_pipeline(url):
#     html_path, screenshot_path = scrape_chapter(url)
#     with open(html_path, "r", encoding="utf-8") as f:
#         raw_text = f.read()

#     spun = generate_spin(raw_text)
#     reviewed = review_text(spun)
#     final = final_edit(reviewed)

#     embedding = get_embedding(final)
#     store_version(final, version="1.0", role="Editor", embedding=embedding)

#     print("Pipeline completed. Final version stored.")

if __name__ == "__main__":
    chapter_url = "https://en.wikipedia.org/wiki/The_Gates_of_Morning"
    run_pipeline(chapter_url)
