import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def final_edit(text: str) -> str:
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    prompt = (
        "You are a book editor. Refine the following for publication: correct grammar, improve flow, remove awkward phrasing, and preserve tone. Ignore HTML tags and any reference to the web:\n\n"f"{text}"

    )
    response = model.generate_content(prompt)
    return response.text
