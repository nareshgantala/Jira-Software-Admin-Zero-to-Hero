import requests
import re

site = "https://your-site.atlassian.net"
auth = ("email", "api-token")

# Get all workflows
workflows = requests.get(
    f"{site}/rest/api/3/workflow/search",
    auth=auth,
    params={"expand": "transitions,statuses"}
).json()

# Get all custom fields for reference
fields = requests.get(f"{site}/rest/api/3/field", auth=auth).json()
custom_fields = {f["id"]: f["name"] for f in fields if f["id"].startswith("customfield_")}

print("=" * 60)
print("WORKFLOWS AND CUSTOM FIELD USAGE")
print("=" * 60)

for wf in workflows.get("values", []):
    wf_name = wf["id"]["name"]
    print(f"\nWorkflow: {wf_name}")
    print("-" * 40)
    
    # Get detailed workflow with transitions
    details = requests.get(
        f"{site}/rest/api/3/workflow/{wf_name}/transitions",
        auth=auth
    ).json()
    
    # Search for customfield references in the response
    details_str = str(details)
    
    # Find all customfield IDs mentioned
    cf_matches = re.findall(r'customfield_\d+', details_str)
    cf_unique = list(set(cf_matches))
    
    if cf_unique:
        print("Custom fields referenced:")
        for cf_id in cf_unique:
            cf_name = custom_fields.get(cf_id, "Unknown")
            print(f"  - {cf_id}: {cf_name}")
    else:
        print("No custom fields found in workflow properties")
