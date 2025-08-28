# Mappings

## NIST 800-61 IR Phases
- **Preparation**: Playbooks, integrations, environment variables, ticketing templates.
- **Detection & Analysis**: Phishing IoC extraction, EncodedCommand detection (if extended), impossible travel check.
- **Containment**: XDR isolate endpoint, block domains/IPs, Okta disable user.
- **Eradication & Recovery**: (Out-of-scope for the offline sim; add imaging/rebuild steps in XSOAR).
- **Post‑Incident**: Jira ticket, Slack summary; extend with retrospective and metrics.

## MITRE ATT&CK
- **T1110 Brute Force** (extend with failed logins correlation)
- **T1059.001 PowerShell** (extend with EncodedCommand triage)
- **T1078 Valid Accounts** (disable user accounts)
- **T1041 Exfiltration Over C2** (block domains/IPs)
