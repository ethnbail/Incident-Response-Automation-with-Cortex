import os, json, requests
# Stub call to Cortex XDR isolation API (replace with real endpoint mapping in your tenant)
def main(context):
    endpoint_id = context["incident"].get("endpoint_id")
    actions = context.get("actions", [])
    if not endpoint_id:
        return {}
    api = os.environ.get("XDR_API_URL")
    key = os.environ.get("XDR_API_KEY")
    if api and key:
        try:
            requests.post(api.rstrip("/") + "/isolate", json={"endpoint_id": endpoint_id}, headers={"Authorization": f"Bearer {key}"}, timeout=5)
        except Exception:
            pass
    actions.append({"action": "xdr_isolate", "endpoint_id": endpoint_id})
    return {"actions": actions}
