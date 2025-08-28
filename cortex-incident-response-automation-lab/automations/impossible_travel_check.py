from math import radians, sin, cos, asin, sqrt
from datetime import datetime, timezone

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    c = 2*asin(sqrt(a))
    return R*c

def hours_between(t1, t2):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    dt1 = datetime.strptime(t1, fmt).replace(tzinfo=timezone.utc)
    dt2 = datetime.strptime(t2, fmt).replace(tzinfo=timezone.utc)
    return abs((dt2 - dt1).total_seconds())/3600.0

def main(context):
    logins = context["incident"].get("logins", [])
    if len(logins) < 2:
        return {"impossible_travel": False}
    a, b = logins[0], logins[1]
    dist_km = haversine(a["lat"], a["lon"], b["lat"], b["lon"])
    hours = hours_between(a["time"], b["time"])
    speed = dist_km / hours if hours > 0 else float("inf")
    # Flag if required speed exceeds 900 km/h (commercial jet)
    flag = speed > 900
    return {"impossible_travel": flag, "travel_speed_kmh": speed}
