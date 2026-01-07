import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

url = f"{JIRA_URL}/rest/api/3/issue"
auth = HTTPBasicAuth(JIRA_EMAIL,JIRA_API_TOKEN)

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
              "text": "testing API connection in creating ISSUES",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "duedate": "2026-05-11",
    "issuetype": {
      "id": "10008"
    },
    "labels": [
      "bugfix",
      "blitz_test"
    ],


    "project": {
      "id": "10033"
    },
    "summary": "Test Ticket usin API",
  },
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

