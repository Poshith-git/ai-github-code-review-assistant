import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder:1.3b"


def review_code_with_llm(code_snippet):
    """
    Sends code to Ollama DeepSeek model
    and returns 3 short review suggestions
    """

    prompt = f"""
You are a senior software engineer reviewing code.

Return EXACTLY 3 short suggestions:

• 1 readability improvement
• 1 maintainability improvement
• 1 optimization idea

Rules:
- Max 8 words per line
- No explanations
- No numbering
- Output only 3 lines

Code:
{code_snippet[:1200]}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=20
        )

        result = response.json()["response"].strip()

        # Convert lines into list
        suggestions = [
            line.strip("• ").strip()
            for line in result.split("\n")
            if line.strip()
        ]

        return suggestions[:3]

    except Exception as e:
        return [f"AI review failed: {str(e)}"]