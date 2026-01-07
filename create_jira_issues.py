import os
import requests
from requests.auth import HTTPBasicAuth
import json

from flask import Flask

app = Flask (__name__)

@app.route("/createJIRA", methods=['POST'])

def createJIRA():  

    url = "https://siva027.atlassian.net/rest/api/3/issue"

    email = "toxicreyes07@gmail.com"

    API_TOKEN = os.getenv("JIRA_API_TOKEN")

    auth = HTTPBasicAuth(email, API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first JIRA ticket to track the progress.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10003"
        },
        "project": {
        "key": "SCRUM"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000)


