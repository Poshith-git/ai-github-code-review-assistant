# AI GitHub Code Review Assistant
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![LLM](https://img.shields.io/badge/AI-DeepSeekCoder-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered backend tool that analyzes GitHub repositories and generates automated code review suggestions.

## Features

- Analyze GitHub repositories automatically
- Detect code issues using static analysis
- Generate AI-powered code review suggestions
- Provide structured JSON reports
- Calculate repository code quality score

## Tech Stack

- Python
- FastAPI
- GitHub REST API
- Ollama (Local LLM Runtime)
- DeepSeek Coder Model

## Project Architecture

GitHub Repository  
↓  
Fetch Repository Files  
↓  
Static Code Analysis  
↓  
AI Code Review  
↓  
JSON Report

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-github-code-review-assistant.git
cd ai-github-code-review-assistant
```

### Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download:

https://ollama.com

Pull AI model:

```bash
ollama pull deepseek-coder:1.3b
```

### Configure GitHub Token

To avoid API rate limits set an environment variable.

Windows:

```
setx GITHUB_TOKEN "your_token_here"
```

Mac/Linux:

```
export GITHUB_TOKEN="your_token_here"
```

### Run the server

```bash
uvicorn main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
 "repo_url": "https://github.com/pallets/flask"
}
```

## Example Response

```json
{
 "repository": "flask",
 "files_analyzed": 8,
 "results": [
   {
     "file": "auth.py",
     "issues": ["Deep nesting"],
     "ai_review": [
       "Reduce nested if statements",
       "Extract helper functions",
       "Add docstrings"
     ]
   }
 ],
 "quality_score": 8
}
```

## Future Improvements

- GitHub Pull Request AI reviewer
- Web dashboard
- Multi-language support
- Code history analysis

## License

MIT License