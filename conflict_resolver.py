import json

with open("output/topic_summaries.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

def resolve_conflict(keyword):

    matched = []

    for topic in topics:

        if keyword.lower() in topic["summary"].lower():

            emotional_weight = 0

            if any(
                word in topic["summary"].lower()
                for word in [
                    "anxiety",
                    "worried",
                    "cancer",
                    "miss"
                ]
            ):
                emotional_weight = 2

            matched.append({
                "topic": topic,
                "weight": emotional_weight
            })

    if not matched:

        return {
            "answer": "No information found.",
            "contradiction": False
        }

    matched.sort(
        key=lambda x: (
            x["weight"],
            x["topic"]["end_message"]
        ),
        reverse=True
    )

    answer = (
        f"Found {len(matched)} references "
        f"related to '{keyword}'. "
        f"Results ranked using recency "
        f"and emotional weight."
    )

    return {
        "answer": answer,
        "contradiction": len(matched) > 1,
        "sources": [
            item["topic"]["topic_id"]
            for item in matched[:5]
        ]
    }