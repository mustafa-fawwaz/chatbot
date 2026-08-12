import os
from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

# Securely grab the key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: No API key found. Check your .env file.")
else:
    print(f"✅ API Key loaded successfully (starts with {api_key[:5]}...)")

# Initialize client
client = genai.Client(api_key=api_key)

try:
    print("⏳ Connecting to Google's Gemini servers...")
    
    # We will test the most universally stable model string
    response = client.models.generate_content(
        model='gemini-1.5-pro', 
        contents="Please respond with the exact word 'SUCCESS' if you receive this."
    )
    
    print("\n🎉 CONNECTION SUCCESSFUL!")
    print(f"AI Response: {response.text}")

except Exception as e:
    print(f"\n❌ CONNECTION FAILED.")
    print(f"Exact Error: {str(e)}")