from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Securely load API keys via environment variables
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogInput(BaseModel):
    log_text: str

@app.post("/api/analyze")
async def analyze_logs(request: LogInput):
    system_prompt = """
    You are an expert DevOps AI assistant analyzing server logs, Kubernetes crashes, and database connection failures.
    You must strictly output your response as a valid JSON object. Do not include markdown formatting or conversational text.
    Use this exact schema:
    {
      "error_type": "string",
      "severity": "High/Medium/Low",
      "root_cause": "string",
      "fix_commands": ["string"]
    }
    """
    
    try:
        # Using the supported model from your key's list
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=request.log_text,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json", # <--- ADD THIS LINE
            )
        )
        
        try:
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            parsed_data = json.loads(clean_text)
            return parsed_data
        except json.JSONDecodeError:
            return {"error": "The AI failed to generate valid structured data. Please try again."}
            
    except Exception as e:
        # This prevents a 500 error and forces React to display the crash details on your screen
        return {"error": f"BACKEND CRASH: {str(e)}"}