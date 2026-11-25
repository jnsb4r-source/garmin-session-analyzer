import json

with open ("data/sample_activities.json") as f:
    activities = json.load(f)

print(activities)