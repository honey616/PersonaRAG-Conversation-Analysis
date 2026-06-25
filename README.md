# PersonaRAG: Topic-Aware Conversation Analysis & User Persona Chatbot

## Project Overview

PersonaRAG is an offline conversation intelligence system that analyzes long conversation histories and builds a Retrieval-Augmented Generation (RAG) chatbot.

The system processes conversations chronologically, detects topic changes, extracts user personas, tracks persona drift over time, classifies user intent offline, performs conflict-aware retrieval, and provides an interactive Streamlit interface for querying conversation history.

This project was developed as part of the **AI/ML Engineer Internship Assignment**.

---

# Live Demo

### Streamlit Application

https://personarag-conversation-analysis-ixjxuumkklowuoplpeg5cr.streamlit.app/

---

# System Design Document

https://1drv.ms/w/c/64802506e3436956/IQBUrW6ywn1wQ6saoRrVlVAsAQkLjbw4aYV6soVxkbNWm9M?e=mg1AJL

---

# Features

## Round 1

* Chronological conversation processing
* Topic detection
* Topic checkpoint generation
* 100-message checkpoints
* Persona extraction
* Topic-aware RAG retrieval
* Streamlit chatbot
* JSON output generation

---

## Round 2

### Adaptive Persona Engine

* Detects persona drift across topic checkpoints
* Detects mood changes
* Detects tone changes
* Identifies conversation triggers
* Generates persona drift timeline

**Output**

* `persona_drift.json`

---

### Offline Intent Classifier

A lightweight offline classifier built using **Scikit-learn**.

**Supported Intents**

* Reminder
* Emotional Support
* Action Item
* Small Talk
* Unknown

**Features**

* Completely offline
* No OpenAI API
* No Gemini API
* CPU inference
* Lightweight and fast

---

### Conflict Resolution in RAG

The retrieval pipeline supports conflict-aware retrieval.

**Features**

* Retrieves multiple relevant checkpoints
* Ranks checkpoints using recency
* Uses emotional weight for ranking
* Detects contradictory information
* Produces one merged coherent response

---

# Workflow

```text
Conversation CSV
        │
        ▼
Topic Detection
        │
        ▼
Topic Summaries
        │
        ▼
Persona Extraction
        │
        ▼
Adaptive Persona Engine
        │
        ▼
Intent Classification
        │
        ▼
Conflict Resolution
        │
        ▼
Streamlit Chatbot
```

---

# Topic Detection

Messages are processed chronologically.

SentenceTransformer (`all-MiniLM-L6-v2`) embeddings are generated and cosine similarity is used to detect topic changes.

Whenever similarity falls below a threshold:

* A new topic checkpoint is created
* Message range is stored
* Topic summary is generated

Each checkpoint stores:

* Topic ID
* Message Range
* Topic Summary

---

# Persona Extraction

The system extracts:

## Habits

* Coffee discussions
* Sleep patterns

## Personal Facts

* College references
* Career discussions

## Personality Traits

* Humorous
* Polite

## Communication Style

* Average words per message
* Message style
* Total messages

---

# Adaptive Persona Engine

The Persona Engine analyzes topic checkpoints and generates:

* Mood
* Tone
* Trigger
* Persona Drift Timeline

### Example

```text
Topic 20

Mood  : Positive
Tone  : Casual

        ↓

Topic 53

Mood    : Emotional
Tone    : Neutral
Trigger : Anxiety

        ↓

Topic 87

Mood    : Emotional
Tone    : Casual
Trigger : Family
```

---

# Offline Intent Classifier

### Example

**Input**

```text
I feel sad
```

**Output**

```text
Emotional Support
```

**Input**

```text
Remind me tomorrow
```

**Output**

```text
Reminder
```

**Input**

```text
Submit the assignment today
```

**Output**

```text
Action Item
```

---

# Conflict Resolution

The resolver:

1. Retrieves relevant topic checkpoints.
2. Ranks them using:

   * Recency
   * Emotional Weight
3. Detects contradictions.
4. Returns one merged response.

---

# Output Files

```text
output/
├── messages.json
├── topic_summaries.json
├── checkpoints.json
├── persona.json
└── persona_drift.json
```

---

# Example Questions

## RAG

* What are the user's habits?
* What kind of person is this user?
* How does this user communicate?
* What topics were discussed?
* Tell me about family.
* Tell me about anxiety.

## Intent Classifier

* I feel sad
* Remind me tomorrow
* Submit my assignment

---

# Project Structure

```text
KaStack_Assignment/
│
├── app.py
├── rag.py
├── topic_detection.py
├── topic_checkpoints.py
├── checkpoints.py
├── persona_builder.py
├── persona_drift.py
├── intent_classifier.py
├── conflict_resolver.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── conversations.csv
│
├── output/
│   ├── messages.json
│   ├── topic_summaries.json
│   ├── checkpoints.json
│   ├── persona.json
│   └── persona_drift.json
│
└── screenshots/
    ├── home.png
    ├── persona.png
    ├── topics.png
    ├── communication.png
    └── habits.png
```

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Run

```bash
python topic_detection.py
python topic_checkpoints.py
python checkpoints.py
python persona_builder.py
python persona_drift.py
python intent_classifier.py

streamlit run app.py
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* SentenceTransformers
* Scikit-learn
* Streamlit
* JSON

---

# Screenshots

### Home

![Home](screenshots/home.png)

### Persona

![Persona](screenshots/persona.png)

### Topics

![Topics](screenshots/topics.png)

### Communication

![Communication](screenshots/communication.png)

### Habits

![Habits](screenshots/habits.png)

---

# Limitations

* The provided dataset does not contain timestamps.
* Therefore, topic checkpoints are treated as temporal segments while detecting persona drift.

---

# Future Improvements

* Cloud synchronization
* Vector database integration
* Improved intent classifier
* Real-time conversation synchronization
* LLM-based persona generation

---

# Key Highlights

* Processed **11,000+** conversation messages.
* Generated **174** topic checkpoints.
* Built an **Adaptive Persona Engine**.
* Developed an **Offline Intent Classifier**.
* Implemented **Conflict-Aware RAG Retrieval**.
* Created a complete **Streamlit chatbot**.
* Designed a **privacy-first offline architecture**.
