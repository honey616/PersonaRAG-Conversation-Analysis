import json

with open("output/topic_summaries.json", "r", encoding="utf-8") as f:
    topics = json.load(f)


def get_mood(summary):

    s = summary.lower()

    if any(word in s for word in [
        "anxiety", "worried", "cancer", "miss",
        "sorry", "stress", "afraid"
    ]):
        return "emotional"

    elif any(word in s for word in [
        "love", "great", "awesome", "favorite",
        "glad", "happy"
    ]):
        return "positive"

    return "neutral"


def get_tone(summary):

    s = summary.lower()

    if any(word in s for word in [
        "business", "marketing", "feedback"
    ]):
        return "formal"

    elif any(word in s for word in [
        "family", "music", "garden",
        "movies", "games", "food"
    ]):
        return "casual"

    return "neutral"

def get_trigger(summary):

    summary = summary.lower()

    summary = summary.replace(
        "discussion related to:",
        ""
    )

    stop_words = {
        "love",
        "like",
        "great",
        "good",
        "yeah",
        "really",
        "very",
        "time",
        "thing",
        "things",
        "today",
        "okay",
        "sure"
    }

    triggers = []

    for word in summary.split(","):

        word = word.strip()

        if word and word not in stop_words:

            triggers.append(word)

    if len(triggers) == 0:
        triggers.append("general conversation")

    return triggers[:3]


def generate_persona_drift():

    timeline = []

    previous_mood = None
    previous_tone = None

    for topic in topics:

        mood = get_mood(topic["summary"])
        tone = get_tone(topic["summary"])
        trigger = get_trigger(topic["summary"])

        # Drift Detection
        if previous_mood is None:
            drift = "Initial Persona"

        elif previous_mood != mood or previous_tone != tone:
            drift = (
                f"{previous_mood}/{previous_tone}"
                f" -> {mood}/{tone}"
            )

        else:
            drift = "No Significant Drift"

        timeline.append({

            "checkpoint": f"Topic {topic['topic_id']}",

            "message_range":
                f"{topic['start_message']} - {topic['end_message']}",

            "mood": mood,

            "tone": tone,

            "trigger": trigger,

            "drift": drift

        })

        previous_mood = mood
        previous_tone = tone

    with open(
        "output/persona_drift.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            timeline,
            f,
            indent=4
        )

    return timeline


if __name__ == "__main__":

    result = generate_persona_drift()

    print(json.dumps(result[:15], indent=4))