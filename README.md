# PR Whisperer

PR Whisperer is a *prototype AI-powered code review assistant* designed to help developers who are coding *individually without access to senior reviewers*. The goal of PR Whisperer is to give developers the experience of a *senior-level code review in seconds* before they submit a pull request.

## Problem

Many developers — especially *students, solo developers, and junior engineers* — often build projects without mentorship or a proper code review process.

Some key challenges:

•⁠  ⁠Many developers ship code *without sufficient code review*
•⁠  ⁠Linters and static tools catch *syntax issues but not contextual problems*
•⁠  ⁠Developers frequently receive *vague feedback* or discover issues only after deployment

Without proper feedback:

•⁠  ⁠Security vulnerabilities may reach production
•⁠  ⁠Inefficient code patterns persist
•⁠  ⁠Learning and growth slow down

PR Whisperer attempts to address this gap by acting as an *AI senior reviewer for individual developers*.


## Solution Overview

Paste your git diff or changed code and get instant feedback across four dimensions:
- **Security** — detects SQL injection, hardcoded secrets, insecure patterns
- **Performance** — flags inefficient loops, N+1 queries, memory issues
- **Readability** — reviews naming, complexity, comment quality
- **Convention** — checks best practices like DRY, SOLID principles

Each issue comes with a **Before/After inline fix** and a **PR Readiness Score (0–100)**.

## Tech Stack

- Frontend: HTML, CSS, JavaScript (no frameworks)
- Backend: Python FastAPI + Uvicorn
- AI Model: LLaMA 3.3-70B via Groq API
- Protocol: REST/JSON

## How to run locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/pr-whisperer.git
cd pr-whisperer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the backend
```bash
uvicorn main:app --reload --port 8000
```

### 5. Open the frontend
Open `index.html` in your browser.


