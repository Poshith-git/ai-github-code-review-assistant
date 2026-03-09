from urllib.parse import urlparse

def parse_github_url(repo_url):

    parsed = urlparse(repo_url)

    path_parts = parsed.path.strip("/").split("/")

    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub URL")

    owner = path_parts[0]
    repo = path_parts[1]

    return owner, repo