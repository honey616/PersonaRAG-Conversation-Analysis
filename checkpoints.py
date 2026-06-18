import json

with open("output/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

checkpoints = []

for i in range(0, len(messages), 100):

    chunk = messages[i:i+100]

    checkpoints.append({
        "checkpoint_id": len(checkpoints)+1,
        "start_message": i+1,
        "end_message": min(i+100, len(messages)),
        "summary": " ".join(chunk[:15])
    })

with open("output/checkpoints.json", "w", encoding="utf-8") as f:
    json.dump(checkpoints, f, indent=4)

print("Checkpoint Created:", len(checkpoints))