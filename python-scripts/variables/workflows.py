import requests
import json

site = "https://your-site.atlassian.net"
auth = ("email", "api-token")

# Get all workflows
workflows = requests.get(
    f"{site}/rest/api/3/workflow/search",
    auth=auth
).json()

for wf in workflows.get("values", []):
    print(f"Workflow: {wf['id']['name']}")
    
    # Get workflow details
    details = requests.get(
        f"{site}/rest/api/3/workflow/{wf['id']['name']}",
        auth=auth
    ).json()
    
    print(json.dumps(details, indent=2))
