from fastapi import FastAPI
from pydantic import BaseModel

from github_fetcher import get_repo_files, download_file
from analyzer import analyze_code
from llm_reviewer import review_code_with_llm

app = FastAPI()


# Request model
class RepoRequest(BaseModel):
    repo_url: str = "https://github.com/pallets/flask"


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "AI GitHub Code Review Assistant API",
        "usage": "POST /analyze-repo with repo_url"
    }


# Main analysis endpoint
@app.post("/analyze-repo")
def analyze_repository(request: RepoRequest):

    owner, repo, files = get_repo_files(request.repo_url)

    results = []
    total_issues = 0

    for file_path in files[:8]:

        code = download_file(owner, repo, file_path)

        if not code:
            continue

        issues = analyze_code(file_path, code)

        # Run AI review only if file has issues
        ai_review = []

        if issues:
            ai_review = review_code_with_llm(code[:800])

        results.append({
            "file": file_path,
            "issues": issues,
            "ai_review": ai_review
        })

        total_issues += len(issues)

    issue_penalty = total_issues * 0.5
    quality_score = max(1, round(10 - issue_penalty))

    return {
        "repository": repo,
        "files_analyzed": len(results),
        "results": results,
        "quality_score": quality_score
    }