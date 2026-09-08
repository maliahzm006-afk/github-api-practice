import requests 
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/repos/maliahzm006-afk/github-api-practice/issues"

data = {
    "title": "My first API-created issue",
    "body": "This issue was created using Python requests."
}

headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

print(token is None) # Check if the token is None

r = requests.post(
    url,
    headers=headers,
    json=data
)

print(r.status_code)
print(r.json())

