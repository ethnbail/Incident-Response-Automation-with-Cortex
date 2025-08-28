import os, requests
def main(context):
    user = context["incident"].get("user", {}).get("username")
    actions = context.get("actions", [])
    domain = os.environ.get("OKTA_DOMAIN")
    token = os.environ.get("OKTA_TOKEN")
    if user and domain and token:
        try:
            requests.post(f"https://{domain}/api/v1/users/{user}/lifecycle/deactivate", headers={"Authorization": f"SSWS {token}"}, timeout=5)
        except Exception:
            pass
    actions.append({"action": "okta_disable_user", "username": user})
    return {"actions": actions}
