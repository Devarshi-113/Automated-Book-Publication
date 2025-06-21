# Automated Book Publication Workflow

This project is an end-to-end system to scrape book content, refine it with AI, and generate publish-ready chapters. It combines web scraping, AI rewriting, reviewing, editing, and content versioning — all orchestrated through a modular pipeline or a simple web UI.

---

## Features

- Scrape chapters from book URLs (Wikisource, etc.)
- Rewrite chapters with AI ("Spinning" via LLM)
- Review and enhance text using an AI reviewer
- Final editing for publication
- Human-in-the-loop interface (Streamlit)
- Version-controlled storage (`.json` + `.txt`)
- Full-page screenshots of original chapters

---

## Project Structure


Root/
│
├── main.py # CLI pipeline runner
├── ui/
│ └── app.py # Streamlit interface
├── agents/ # AI logic
│ ├── writer.py
│ ├── reviewer.py
│ └── editor.py
├── utils/
│ ├── scraper.py # Web scraper using Playwright
│ └── file_io.py # Save/load helper functions
├── data/ # Outputs
│ ├── raw_html/
│ ├── screenshots/
│ └── versions/
│── json_to_text.py
│── requirements.txt
│── README.md




## Environment Setup
Set your Google Gemini API Key as an environment variable:

- Linux / macOS
    export GOOGLE_API_KEY=your-gemini-api-key

- Windows CMD
    set GOOGLE_API_KEY=your-gemini-api-key

- PowerShell
    $env:GOOGLE_API_KEY="your-gemini-api-key"

Get your Gemini API key from: https://makersuite.google.com/app/apikey



## Running the Project

- Option 1: Run via CLI
    python main.py
    
- Option 2: Use the Web Interface
    streamlit run ui/app.py


## API Key

- paste your api key in .env file
