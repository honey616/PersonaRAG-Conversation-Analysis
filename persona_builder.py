import json
from collections import Counter

with open("output/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

all_text = " ".join(messages).lower()

persona = {
    "habits": [],
    "personal_facts": [],
    "personality_traits": [],
    "communication_style": {}
}

# Habits with evidence

if "coffee" in all_text:
    persona["habits"].append({
        "habit": "Talks about coffee",
        "evidence": "coffee mentioned in conversations"
    })

if "sleep" in all_text:
    persona["habits"].append({
        "habit": "Discusses sleep patterns",
        "evidence": "sleep related messages found"
    })

# Personal facts

if "college" in all_text:
    persona["personal_facts"].append({
        "fact": "Mentions college",
        "evidence": "college keyword found"
    })

if "job" in all_text:
    persona["personal_facts"].append({
        "fact": "Talks about career or jobs",
        "evidence": "job keyword found"
    })

# Personality traits

if "haha" in all_text or "lol" in all_text:
    persona["personality_traits"].append({
        "trait": "Humorous",
        "evidence": "laugh expressions detected"
    })

if "thank you" in all_text:
    persona["personality_traits"].append({
        "trait": "Polite",
        "evidence": "frequent gratitude expressions"
    })

# Communication style

avg_words = sum(len(msg.split()) for msg in messages) / len(messages)

persona["communication_style"] = {
    "average_words_per_message": round(avg_words, 2),
    "message_style": "Short Messages" if avg_words < 15 else "Long Messages",
    "total_messages": len(messages)
}

with open("output/persona.json", "w", encoding="utf-8") as f:
    json.dump(persona, f, indent=4)

print("Persona Created Successfully")