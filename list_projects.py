import os
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://siva027.atlassian.net/rest/api/3/project"

email = "toxicreyes07@gmail.com"

API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth(email, API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))