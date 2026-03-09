import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "AI-GitHub-Code-Review-Assistant"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


# -----------------------------
# Parse GitHub URL
# -----------------------------
def parse_github_url(repo_url):

    repo_url = repo_url.strip()

    if repo_url.endswith(".git"):
        repo_url = repo_url[:-4]

    repo_url = repo_url.rstrip("/")

    parts = repo_url.split("/")

    if len(parts) < 5:
        raise Exception("Invalid GitHub repository URL")

    owner = parts[3]
    repo = parts[4]

    return owner, repo


# -----------------------------
# Fetch Repository Files
# -----------------------------
def get_repo_files(repo_url):

    owner, repo = parse_github_url(repo_url)

    repo_api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_response = requests.get(repo_api, headers=HEADERS)

    if repo_response.status_code != 200:
        raise Exception(
            f"GitHub API Error: {repo_response.status_code} - {repo_response.text}"
        )

    repo_data = repo_response.json()

    default_branch = repo_data["default_branch"]

    tree_api = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"

    tree_response = requests.get(tree_api, headers=HEADERS)

    if tree_response.status_code != 200:
        raise Exception(
            f"GitHub Tree API Error: {tree_response.status_code} - {tree_response.text}"
        )

    tree_data = tree_response.json()

    files = []

    for item in tree_data["tree"]:

        if item["type"] == "blob":

            path = item["path"]

            if path.endswith((".py", ".js", ".java", ".cpp")):
                files.append(path)

    return owner, repo, files


# -----------------------------
# Download File Content
# -----------------------------
def download_file(owner, repo, file_path):

    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{file_path}"

    response = requests.get(raw_url)

    if response.status_code == 200:
        return response.text

    return None