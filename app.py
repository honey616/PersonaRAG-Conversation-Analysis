import streamlit as st
from rag import answer_query

# Page Configuration
st.set_page_config(
    page_title="PersonaRAG",
    layout="wide"
)

# Header
st.title("PersonaRAG")
st.subheader("Topic-Aware Conversation Analysis and User Persona Chatbot")

st.write(
    """
    This system analyzes conversation history, topic checkpoints,
    message summaries, and user persona information using a
    Retrieval-Augmented Generation (RAG) approach.
    """
)

# Example Questions
with st.expander("Example Questions"):

    st.write("What kind of person is this user?")
    st.write("What are the user's habits?")
    st.write("How does this user communicate?")
    st.write("What topics were discussed?")
    st.write("Tell me about the user's personality traits.")

# User Input
query = st.text_input("Ask a Question")

# Process Query
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

# Footer
st.markdown("---")

st.caption(
    "Conversation Intelligence, Topic Awareness and User Persona Understanding"
)