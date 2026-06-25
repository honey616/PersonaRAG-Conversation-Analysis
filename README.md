# PersonaRAG: Topic-Aware Conversation Analysis & User Persona Chatbot

## Project Overview

PersonaRAG is an offline conversation intelligence system that analyzes long conversation histories and builds a Retrieval-Augmented Generation (RAG) based chatbot.

The system performs chronological topic detection, persona extraction, adaptive persona drift detection, offline intent classification, conflict-aware retrieval, and provides an interactive Streamlit interface.

This project was developed as part of the AI/ML Engineer Internship Assignment.

---

# Live Demo

**Streamlit Application**

https://personarag-conversation-analysis-ixjxuumkklowuoplpeg5cr.streamlit.app/

---
# System Design PDF

https://1drv.ms/w/c/64802506e3436956/IQBUrW6ywn1wQ6saoRrVlVAsAQkLjbw4aYV6soVxkbNWm9M?e=mg1AJL

---
# Features

## Round 1 Features

* Chronological conversation processing
* Topic checkpoint generation
* 100-message checkpoints
* Persona extraction
* Topic-aware RAG retrieval
* Streamlit chatbot
* JSON outputs

---

## Round 2 Features

### Adaptive Persona Engine

* Detects persona drift across conversation checkpoints
* Detects mood changes
* Detects tone changes
* Identifies trigger (topic/event/person)
* Generates persona drift timeline

Output:

* persona_drift.json

---

### Offline Intent Classifier

Offline lightweight classifier using Scikit-learn.

Supported intents:

* Reminder
* Emotional Support
* Action Item
* Small Talk
* Unknown

Features

* Runs completely offline
* No OpenAI API
* No Gemini API
* CPU inference
* Lightweight model

---

### Conflict Resolution in RAG

The retrieval pipeline supports conflict-aware retrieval.

Features

* Retrieves multiple relevant checkpoints
* Ranks checkpoints using recency
* Uses emotional weight while ranking
* Detects contradictions
* Generates one merged coherent answer

---

### System Design

The project includes a one-page system design describing:

* On-device storage
* Future cloud synchronization
* Conflict resolution strategy
* Overall architecture

---

# Workflow

Conversation CSV

↓

Topic Detection

↓

Topic Summaries

↓

Persona Extraction

↓

Adaptive Persona Engine

↓

Intent Classification

↓

Conflict Resolution

↓

Streamlit Chatbot

---

# Topic Detection

Messages are processed chronologically.

SentenceTransformer (all-MiniLM-L6-v2) embeddings are generated.

Cosine similarity is used to detect topic changes.

Whenever similarity falls below a threshold:

* New topic checkpoint is created
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

Example

Topic 20

Mood → Positive

Tone → Casual

↓

Topic 53

Mood → Emotional

Tone → Neutral

Trigger → Anxiety

↓

Topic 87

Mood → Emotional

Tone → Casual

Trigger → Family

---

# Offline Intent Classifier

Example

Input:

I feel sad

Output:

Emotional Support

Input:

Remind me tomorrow

Output:

Reminder

Input:

Submit the assignment today

Output:

Action Item

---

# Conflict Resolution

The resolver:

1. Retrieves relevant topic checkpoints

2. Ranks them using

* Recency
* Emotional Weight

3. Detects contradictions

4. Returns one merged response

---

# Output Files

* messages.json
* topic_summaries.json
* checkpoints.json
* persona.json
* persona_drift.json

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

KaStack_Assignment/

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

├── System_Design_Document_PersonaRAG.pdf

│

├── data/

│ └── conversations.csv

│

├── output/

│ ├── messages.json

│ ├── topic_summaries.json

│ ├── checkpoints.json

│ ├── persona.json

│ └── persona_drift.json

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

streamlit run app.py
```

---

# Technologies

* Python
* Pandas
* SentenceTransformers
* Scikit-learn
* Streamlit
* JSON

---

# Limitations

The provided dataset does not contain timestamps.

Therefore, topic checkpoints are treated as temporal segments while detecting persona drift.

---

# Future Improvements

* Cloud synchronization
* Vector database
* Better intent classifier
* Real-time synchronization
* LLM-based persona generation

---

# Key Highlights

* Processed 11,000+ messages
* Generated 174 topic checkpoints
* Built an Adaptive Persona Engine
* Built an Offline Intent Classifier
* Implemented Conflict Resolution in RAG
* Developed a complete Streamlit application
* Privacy-first offline architecture
