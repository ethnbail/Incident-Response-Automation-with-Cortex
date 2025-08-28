import re
SUSPICIOUS_TLDS = {"zip","mov","gq","tk","work","party","click"}
KEYWORDS = {"verify","account","password","login","update","invoice","urgent"}

def score_domain(d):
    score = 0
    parts = d.lower().split(".")
    if parts[-1] in SUSPICIOUS_TLDS: score += 25
    if any(k in d.lower() for k in KEYWORDS): score += 25
    if len(d) > 30: score += 10
    return min(score, 60)

def main(context):
    arts = context.get("artifacts", {})
    domains = arts.get("domains", [])
    urls = arts.get("urls", [])
    base = 10 if urls else 0
    domain_score = max([score_domain(d) for d in domains], default=0)
    total = min(100, base + domain_score + (15 if arts.get("hashes") else 0))
    return {"threat_score": total}
