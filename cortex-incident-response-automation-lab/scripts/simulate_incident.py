#!/usr/bin/env python3
"""
Local playbook runner to simulate SOAR flow without a live XSOAR tenant.

Usage:
  python3 scripts/simulate_incident.py playbooks/phishing.yml data/phishing_email.json
"""
import sys, json, importlib, time, os
import yaml

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def eval_condition(expr, ctx):
    # Very small, safe eval: expose only 'context' dict
    allowed_names = {"context": ctx}
    code = compile(expr, "<expr>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise ValueError(f"Illegal name in expression: {name}")
    return eval(code, {"__builtins__": {}}, allowed_names)

def run_step(step, ctx):
    name = step.get("id", step.get("run"))
    cond = step.get("when")
    if cond:
        try:
            if not eval_condition(cond, ctx):
                print(f"[SKIP] {name} (condition false: {cond})")
                return ctx
        except Exception as e:
            print(f"[ERR ] Condition error in {name}: {e}")
            return ctx

    mod_name = step["run"]
    try:
        mod = importlib.import_module(f"automations.{mod_name}")
    except ModuleNotFoundError:
        print(f"[ERR ] Automation not found: {mod_name}")
        return ctx

    print(f"[RUN ] {name} -> {mod_name}")
    try:
        updates = mod.main(ctx)
        if updates and isinstance(updates, dict):
            ctx.update(updates)
    except Exception as e:
        print(f"[ERR ] {name} failed: {e}")
    return ctx

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 scripts/simulate_incident.py <playbook.yml> <incident.json>")
        sys.exit(1)

    playbook = load_yaml(sys.argv[1])
    incident = load_json(sys.argv[2])
    context = {"incident": incident, "artifacts": {}, "actions": []}

    print(f"=== Playbook: {playbook.get('name')} ===")
    for step in playbook.get("steps", []):
        context = run_step(step, context)

    print("=== Context (final) ===")
    print(json.dumps(context, indent=2))

if __name__ == "__main__":
    main()
