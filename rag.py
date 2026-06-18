import json

with open("output/topic_summaries.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

with open("output/persona.json", "r", encoding="utf-8") as f:
    persona = json.load(f)

with open("output/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)


def answer_query(query):

    q = query.lower()

    # Persona Queries

    if "habit" in q:
        return persona["habits"]

    if "person" in q or "personality" in q:
        return persona["personality_traits"]

    if "talk" in q or "communicate" in q:
        return persona["communication_style"]

    # Show Topics

    if "topic" in q or "discussed" in q:

        topic_list = []

        for topic in topics[:5]:

            topic_list.append({
                "topic_id": topic["topic_id"],
                "message_range": f"{topic['start_message']} - {topic['end_message']}",
                "topic_summary": topic["summary"][:200] + "..."
            })

        return topic_list

    # Retrieval

    matched_topics = []

    for topic in topics:

        summary = topic["summary"].lower()

        if any(word in summary for word in q.split()):

            start_msg = topic["start_message"]
            end_msg = topic["end_message"]

            context = messages[
                start_msg - 1:
                min(start_msg + 5, len(messages))
            ]

            matched_topics.append({
                "topic_id": topic["topic_id"],
                "message_range": f"{start_msg} - {end_msg}",
                "topic_summary": topic["summary"][:250] + "...",
                "sample_messages": context[:3]
            })

    if matched_topics:
        return matched_topics[:3]

    return "No relevant information found."