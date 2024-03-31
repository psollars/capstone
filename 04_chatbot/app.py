import streamlit as st
import random
import time


def get_data_from_database(user_message):
    # Implement your logic to connect and query the vector database
    # based on user_message and return relevant document(s) or information
    # This example is for illustration, adapt based on your library

    return "This course extends Data Mining I and introduces additional data representations and tasks involved in mining real world data, with a particular focus on sequence modeling, time series analysis, and mining data streams.\xa0 It introduces how to extract patterns, compute similarities/distances of data, and make predictions under these data representations."


metadata = {
    "course_date": "February 2023",
    "course_number": "SIADS 632",
    "course_title": "Data Mining II",
    "heading": "Course Overview and Prerequisites",
    "source": "2023-02_632.md",
}

st.set_page_config(page_title="MADS-GPT", page_icon="")

st.title("MADS-GPT")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Prompt Here"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    response = "This course extends Data Mining I and introduces additional data representations and tasks involved in mining real world data, with a particular focus on sequence modeling, time series analysis, and mining data streams.\xa0 It introduces how to extract patterns, compute similarities/distances of data, and make predictions under these data representations."

    for word in response.split():
        yield word + " "
        time.sleep(0.05)


# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

    st.write(
        "<p style='font-size: 13px;'> Source: " + " |".join(metadata.values()) + "</p>",
        unsafe_allow_html=True,
    )


# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
