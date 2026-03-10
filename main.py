from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os, json

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ReviewRequest(BaseModel):
    diff: str
    language: str = "auto"

SYSTEM_PROMPT = """
You are a senior software engineer reviewing a pull request.
Analyze the given code diff and return ONLY a JSON object with this exact structure:
{
  "issues": [
    {
      "category": "Security|Performance|Readability|Convention",
      "severity": "High|Medium|Low",
      "line_hint": "brief location description",
      "problem": "clear explanation of what is wrong",
      "original_code": "the problematic code snippet",
      "fixed_code": "the corrected version"
    }
  ],
  "summary": "2-3 sentence overall review summary",
  "score": <integer 0-100>,
  "score_breakdown": {
    "security": <integer 0-25>,
    "performance": <integer 0-25>,
    "readability": <integer 0-25>,
    "convention": <integer 0-25>
  },
  "positive_notes": ["one thing done well", "another good practice noticed"]
}
Scoring: start at 100, deduct High=15pts, Medium=8pts, Low=3pts per issue. Min score is 5.
Return ONLY valid JSON. No markdown, no extra text.
"""

@app.post("/review")
async def review_code(request: ReviewRequest):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Language: {request.language}\n\nCode diff:\n{request.diff}"}
        ],
        max_tokens=2000,
        temperature=0.2
    )
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())

@app.get("/health")
async def health():
    return {"status": "ok"}