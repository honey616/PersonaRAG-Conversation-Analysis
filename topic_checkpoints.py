import json
import re
from collections import Counter

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading messages...")

with open("output/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

topics = []

current_topic = []
start_idx = 1

topic_embedding = None

stop_words = {
    "user", "that", "this", "with", "have",
    "your", "about", "what", "from", "they",
    "them", "just", "really", "would", "there",
    "been", "were", "their", "then", "than",
    "when", "where", "which", "while", "also"
}


def generate_summary(topic_messages):

    text = " ".join(topic_messages).lower()

    words = re.findall(r'\b[a-z]{4,}\b', text)

    words = [w for w in words if w not in stop_words]

    if not words:
        return "General conversation"

    keywords = Counter(words).most_common(5)

    keyword_text = ", ".join([word for word, count in keywords])

    return f"Discussion related to: {keyword_text}"


for i, msg in enumerate(messages):

    msg_embedding = model.encode([msg])

    if topic_embedding is None:
        current_topic.append(msg)
        topic_embedding = msg_embedding
        continue

    similarity = cosine_similarity(
        topic_embedding,
        msg_embedding
    )[0][0]

    if similarity < 0.30:

        topics.append({
            "topic_id": len(topics) + 1,
            "start_message": start_idx,
            "end_message": i,
            "summary": generate_summary(current_topic)
        })

        current_topic = [msg]
        start_idx = i + 1
        topic_embedding = msg_embedding

    else:
        current_topic.append(msg)

if current_topic:

    topics.append({
        "topic_id": len(topics) + 1,
        "start_message": start_idx,
        "end_message": len(messages),
        "summary": generate_summary(current_topic)
    })

with open("output/topic_summaries.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, indent=4)

print("Topics Created:", len(topics))
print("Saved to output/topic_summaries.json")