import os, json, requests

def main(context):
    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    text = f":rotating_light: Incident: {context['incident'].get('type')} | score={context.get('threat_score','-')} | actions={context.get('actions',[])}"
    if webhook:
        try:
            requests.post(webhook, json={"text": text}, timeout=5)
        except Exception:
            pass
    else:
        print("[SLACK]", text)
    return {}
