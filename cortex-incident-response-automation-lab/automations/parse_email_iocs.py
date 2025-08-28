import re
def find_all(pattern, text):
    return re.findall(pattern, text, flags=re.I)

def main(context):
    body = context.get("incident", {}).get("email", {}).get("body", "") or ""
    urls = find_all(r"https?://[^\s)]+", body)
    ips  = find_all(r"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b", body)
    hashes = find_all(r"\\b[a-f0-9]{32,64}\\b", body)
    domains = []
    for u in urls:
        try:
            d = u.split("//",1)[1].split("/",1)[0]
            domains.append(d)
        except Exception:
            pass
    artifacts = context.get("artifacts", {})
    artifacts.update({"urls": urls, "ips": ips, "hashes": hashes, "domains": list(set(domains))})
    return {"artifacts": artifacts}
