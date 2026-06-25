import json

with open("output/topic_summaries.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

with open("output/persona.json", "r", encoding="utf-8") as f:
    persona = json.load(f)

with open("output/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)


def answer_query(query):

    q = query.lower()

    # ==========================
    # Persona Queries
    # ==========================

    if "habit" in q:
        return persona["habits"]

    if "person" in q or "personality" in q:
        return persona["personality_traits"]

    if "talk" in q or "communicate" in q:
        return persona["communication_style"]

    # ==========================
    # Topic Overview
    # ==========================

    if "topic" in q or "discussed" in q:

        topic_list = []

        for topic in topics[:10]:

            topic_list.append({
                "topic_id": topic["topic_id"],
                "message_range":
                    f"{topic['start_message']} - {topic['end_message']}",
                "topic_summary": topic["summary"]
            })

        return topic_list

    # ==========================
    # Family Query
    # ==========================

    if "family" in q:

        results = []

        for topic in topics:

            if "family" in topic["summary"].lower():

                results.append({
                    "topic_id": topic["topic_id"],
                    "summary": topic["summary"],
                    "range":
                        f"{topic['start_message']} - {topic['end_message']}"
                })

        return results[:5]

    # ==========================
    # Anxiety Query
    # ==========================

    if "anxiety" in q:

        results = []

        for topic in topics:

            if "anxiety" in topic["summary"].lower():

                results.append({
                    "topic_id": topic["topic_id"],
                    "summary": topic["summary"],
                    "range":
                        f"{topic['start_message']} - {topic['end_message']}"
                })

        return results[:5]

    # ==========================
    # General Retrieval
    # ==========================

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
                "message_range":
                    f"{start_msg} - {end_msg}",
                "topic_summary": topic["summary"],
                "sample_messages": context[:3]
            })

    if matched_topics:

        matched_topics = sorted(
            matched_topics,
            key=lambda x: int(
                x["message_range"].split("-")[1].strip()
            ),
            reverse=True
        )

        return matched_topics[:5]

    return {
        "answer": "No relevant information found."
    }