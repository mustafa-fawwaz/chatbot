import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("🔍 Asking Google for your allowed models...")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    models = data.get('models', [])
    
    print("\n✅ SUCCESS! Your API key is authorized to use these models:")
    for m in models:
        # We only care about models that can generate text
        if 'generateContent' in m.get('supportedGenerationMethods', []):
            # Strip the 'models/' prefix to get the exact string you need
            clean_name = m['name'].replace('models/', '')
            print(f"  - {clean_name}")
else:
    print(f"\n❌ FAILED TO FETCH MODELS.")
    print(f"Error {response.status_code}: {response.text}")