import streamlit as st
import time
import random
import re
import pickle

# from mock_responses import responses


@st.cache_resource
def get_next_response():
    with open("./sample_results_norouter_5.pkl", "rb") as handle:
        responses = pickle.load(handle)

    i = 0
    while True:
        i += 1
        if i >= len(responses):
            i = 0
        yield responses[i - 1]


def build_source(source_documents):
    sources = ""
    for doc in source_documents:
        m = doc.metadata

        if re.match(r".*\.en.txt$", m["source"]):  # transcripts
            lecture = (
                m["source"]
                .replace("_", " ")
                .replace("-", " ")
                .replace(".en.txt", "")
                .title()
            )
            sources += (
                f"- {m['course_title']} ({m['course_number']}) | Lecture: {lecture}\n"
            )
        elif re.match(r"^\d+_\d{4}-\d{2}\.md$", m["source"]):  # syllabus
            sources += f"- {m['course_title']} ({m['course_number']}) > {m['heading']} | [Course Syllabus]({m['document']})\n"
        else:  # document
            title = m["source"].replace("_", " ").replace(".md", "").title()
            sources += f"- [{title}]({m['document']}) > {m['heading']}\n"

    return sources


def fake_stream_response(r):
    for word in r["result"].split():
        yield f"{word} "
        time.sleep(random.uniform(0.001, 0.2))


st.markdown("## MADS-RAG")
st.markdown(
    "#### A Helpful Chatbot for Master's of Applied Data Science Students at "
    + "the University of Michigan"
)
st.markdown(
    "Please note that answers provided by this chatbot may not be correct "
    + "and should be verified by other means. "
    + "Some source data may be out of date. "
)
st.markdown("---")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        next_response = get_next_response().__next__()
        response = st.write_stream(fake_stream_response(next_response))

        st.write("##### Sources")
        st.write(build_source(next_response["source_documents"][:3]))

    st.session_state.messages.append({"role": "assistant", "content": response})


# Who is the instructor for the SQL and Databases class?
# What classes does Graham Hukill teach?
# How many credits do I need to complete the MADS program?
# How does PCA work?

# What is Elle O'Brien's role in the MADS program?
# According to your information, who is Laura Stagnaro?
# What can you tell me about Kevyn Collins-Thompson?
# Which class involves time series analysis?
# Who teaches the SQL and Databases class?
# What are the prerequisites for Data Science for Social Good?
# What is a backpack for MADS students?
# When is the latest I can drop a course?
# How do I get an override to take a class?
# How do I take a leave of absence from the MADS program?
