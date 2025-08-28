import os, json, requests

def main(context):
    arts = context.get("artifacts", {})
    actions = context.get("actions", [])
    blocked = {"ips": [], "domains": []}

    # Example: push to PAN-OS or DNS filter via webhook/API (stubbed)
    api_url = os.environ.get("BLOCKLIST_API_URL")
    api_key = os.environ.get("BLOCKLIST_API_KEY")

    for d in arts.get("domains", []):
        blocked["domains"].append(d)
        if api_url and api_key:
            try:
                requests.post(api_url, json={"indicator": d, "type": "domain"}, headers={"Authorization": f"Bearer {api_key}"}, timeout=5)
            except Exception:
                pass
    for ip in arts.get("ips", []):
        blocked["ips"].append(ip)

    actions.append({"action": "block", "details": blocked})
    return {"actions": actions}
