# Incident Response Automation with Cortex (XSOAR) — Lab

Portfolio-ready lab demonstrating **SOAR** playbooks and automations for common incidents, designed for **Palo Alto Cortex XSOAR**.  
Includes a **local simulator** so you can run the logic without a live XSOAR tenant, plus **XSOAR-importable templates** to deploy later.

## What you can demo
- **Phishing auto‑triage** → extract IoCs → heuristic scoring → conditional blocking → Slack notify
- **Ransomware rapid response** → isolate endpoint (XDR) → disable user (Okta) → open Jira → notify
- **Suspicious login (impossible travel)** → geo/velocity check → Okta disable → notify

## Two ways to use
### A) Run locally (simulator)
1. Install deps:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
2. Run a playbook with sample data:
   ```bash
   python3 scripts/simulate_incident.py playbooks/phishing.yml data/phishing_email.json
   python3 scripts/simulate_incident.py playbooks/ransomware.yml data/ransomware_alert.json
   python3 scripts/simulate_incident.py playbooks/suspicious_login.yml data/suspicious_login.json
   ```
3. (Optional) Wire real APIs via env vars:  
   - `SLACK_WEBHOOK_URL`  
   - `XDR_API_KEY`, `XDR_API_URL`  
   - `OKTA_DOMAIN`, `OKTA_TOKEN`  
   - `JIRA_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`

### B) Import into Cortex XSOAR (when you have access)
- See `docs/XSOAR_IMPORT.md` for steps to create integrations, incident fields, and import YAML templates under `xsoar/`.

## Repo structure
```
automations/    # Python automations (runnable locally; easy to port into XSOAR automations)
playbooks/      # Simple YAML playbooks consumed by the local simulator
xsoar/          # XSOAR‑style templates (playbooks, layouts, incident fields)
data/           # Sample incident JSONs
docs/           # Guidance, ATT&CK and NIST mappings, diagrams
scripts/        # Local simulator
.github/        # CI for linting
```

## MITRE ATT&CK & NIST 800‑61
See `docs/mappings.md` for technique coverage and IR phase mapping.

> **Note**: The local simulator is intentionally lightweight—great for portfolio demos and interviews. For production, import the artifacts into a real XSOAR instance and connect live integrations.
