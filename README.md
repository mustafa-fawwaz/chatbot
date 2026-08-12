# DevOps Log Error Analyzer

This is a full-stack web application that solves the problem of deciphering confusing infrastructure logs, Kubernetes crashes, and database connection failures. It uses an advanced system prompt to force a Large Language Model (LLM) to output a structured JSON analysis of the root cause and suggested fixes.

## Project Structure

- **Backend:** Python, FastAPI, Google GenAI SDK (`gemini-flash-latest`)
- **Frontend:** React.js (Vite)

## Prerequisites

- Node.js installed
- Python 3.10+ installed
- A valid Google Gemini API Key

---

## 1. Backend Setup (FastAPI)

1. Open a terminal and navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   Install the required dependencies:
   ```
4. Environment Variables:
   - Locate the .env.example file in the backend folder.
   - Create a new file named exactly .env in the same directory.
   - Copy the contents of .env.example into .env and replace insert_your_api_key_here with your actual Google Gemini API key.

5. Start the backend server:
   ```
   uvicorn main:app --reload
   ```
   The backend will now be running on http://127.0.0.1:8000

## 2. Backend Setup (FastAPI)

1. Open a new, separate terminal and navigate to the frontend folder:

   ```
   cd frontend
   ```

2. Install the required Node modules:

   ```
   npm install
   ```

3. Start the Vite development server:
   ```
   npm run dev
   ```
   The frontend will typically run on http://localhost:5173

## 3. Backend Setup (FastAPI)

1. Ensure both the backend and frontend servers are running simultaneously.

2. Open the frontend URL in your browser.
3. Paste a raw server log, Kubernetes error, or Docker crash into the text area.
4. Click Analyze Log. The frontend will display a loading state while the FastAPI backend securely communicates with the LLM and parses the strict JSON response.
5. The structured data (Error Type, Severity, Root Cause, and Fix Commands) will render dynamically on the screen.
