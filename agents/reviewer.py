import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def review_text(text):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content(f"Act as a professional editor. Improve the following text. Ignore all HTML tags and any reference to the web:\n\n{text}")
    return response.text
