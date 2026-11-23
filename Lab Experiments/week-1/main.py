
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found. Check your .env file.")

# Initialize Gemini client
import time

client = genai.Client(api_key=api_key)

prompt = "What is Artificial Intelligence? Explain in simple words."

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        print("\nLLM Response:")
        print(response.text)
        break

    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")

        if attempt < 2:
            print("Retrying in 10 seconds...")
            time.sleep(10)
        else:
            print("Gemini is still unavailable. Please try again later.")