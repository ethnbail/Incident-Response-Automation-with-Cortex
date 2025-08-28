# Import to Cortex XSOAR

1. **Create/Verify Integrations** (or Mock):
   - Slack incoming webhook
   - Okta (users: deactivate)
   - Jira Cloud/Server
   - Cortex XDR (isolate endpoint)

2. **Automations**:
   - In XSOAR: *Settings → Automations → New Script →* paste the Python from `automations/` (one per script).

3. **Playbooks**:
   - *Playbooks → New → Import*: use YAML from `xsoar/phishing_template.yml` (and create similar for `ransomware` and `suspicious_login`).

4. **Incident Type** (optional):
   - Create incident type "Phishing", map email fields, set default playbook.

5. **Test**:
   - Create a phishing incident with the body/URL from `data/phishing_email.json` and run the playbook. Verify Slack/Jira actions.
