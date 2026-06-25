import streamlit as st
from rag import answer_query
from persona_drift import generate_persona_drift
from intent_classifier import classify_intent
from conflict_resolver import resolve_conflict

# Page Configuration
st.set_page_config(
    page_title="PersonaRAG",
    layout="wide"
)

# Sidebar
page = st.sidebar.selectbox(
    "Select Module",
    [
        "RAG Chat",
        "Persona Drift",
        "Intent Classifier",
        "Conflict Resolver"
    ]
)

# ==========================================
# RAG CHAT
# ==========================================

if page == "RAG Chat":

    st.title("PersonaRAG")
    st.subheader(
        "Topic-Aware Conversation Analysis and User Persona Chatbot"
    )

    st.write(
        """
        This system analyzes conversation history,
        topic checkpoints,
        message summaries,
        and user persona information
        using a Retrieval-Augmented Generation (RAG) approach.
        """
    )

    with st.expander("Example Questions"):

        st.write("What kind of person is this user?")
        st.write("What are the user's habits?")
        st.write("How does this user communicate?")
        st.write("What topics were discussed?")
        st.write("Tell me about the user's personality traits?")

    query = st.text_input("Ask a Question")

    if query:

        result = answer_query(query)

        st.subheader("Response")

        if isinstance(result, list):

            for item in result:

                if isinstance(item, dict):
                    st.json(item)

                else:
                    st.write(item)

        elif isinstance(result, dict):

            st.json(result)

        else:

            st.write(result)

# ==========================================
# PERSONA DRIFT
# ==========================================

elif page == "Persona Drift":

    st.title("Adaptive Persona Engine")

    st.write(
        "Tracks mood, tone and trigger changes across conversation segments"
    )

    drift = generate_persona_drift()

    st.json(drift)

# ==========================================
# INTENT CLASSIFIER
# ==========================================

elif page == "Intent Classifier":

    st.title("Offline Intent Classifier")

    st.write(
        "Classifies messages into reminder, emotional-support, action-item, small-talk and unknown"
    )

    message = st.text_input("Enter a message")

    if message:

        intent = classify_intent(message)

        st.success(
            f"Detected Intent: {intent}"
        )

# ==========================================
# CONFLICT RESOLVER
# ==========================================

elif page == "Conflict Resolver":

    st.title("Conflict Resolution in RAG")

    st.write(
        "Search topic summaries and detect contradictory information"
    )

    keyword = st.text_input(
        "Enter keyword (family, dog, college, music)"
    )

    if keyword:

        result = resolve_conflict(keyword)

        st.json(result)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Conversation Intelligence, Topic Awareness and User Persona Understanding"
)