import os, requests, json, base64
def main(context):
    url = os.environ.get("JIRA_URL")
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    actions = context.get("actions", [])
    payload = {
        "fields": {
            "project": {"key": "IR"},
            "summary": f"IR: {context['incident'].get('type')} on {context['incident'].get('hostname','n/a')}",
            "description": json.dumps(context, indent=2),
            "issuetype": {"name": "Task"}
        }
    }
    if url and email and token:
        try:
            auth = (email, token)
            requests.post(url.rstrip("/") + "/rest/api/2/issue", json=payload, auth=auth, timeout=5)
        except Exception:
            pass
    actions.append({"action": "jira_create", "project": "IR"})
    return {"actions": actions}
