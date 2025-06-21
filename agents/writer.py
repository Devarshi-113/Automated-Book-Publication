import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_spin(text):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content(f"Rewrite the following creatively but keep the meaning. Ignore all HTML tags and any reference to the web:\n\n{text}")
    return response.text
