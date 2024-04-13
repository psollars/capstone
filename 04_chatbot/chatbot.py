import streamlit as st
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain_core.prompts import PromptTemplate
from ragatouille import RAGPretrainedModel

import re
import time
import random

base_dir = "./.."


@st.cache_resource
def get_retriever():
    RAG = RAGPretrainedModel.from_index(
        index_path=f"{base_dir}/colbert_index/colbert/indexes/combined/"
    )

    retriever = RAG.as_langchain_retriever(k=5)

    return retriever


@st.cache_resource
def get_llm(_retriever):
    template = """
    Use only the following pieces of context to answer the question at the end.
    Keep your answers concise and do not provide additional explanations or interpretations.
    If the answer cannot be deduced from the context, just say that you don't know the answer, don't try to make up an answer.

    {context}

    Question: {question}
    Helpful Answer:
    """

    std_out = StreamingStdOutCallbackHandler()
    callback_manager = CallbackManager([std_out])

    llm_open = LlamaCpp(
        model_path=f"{base_dir}/models/mistral-7b-instruct-v0.2.gguf",
        n_ctx=32 * 1024,  # 4096 for Llama, 32*1024 for Mistral
        n_gpu_layers=50,
        temperature=0.15,
        top_p=1,
        top_k=40,
        repeat_penalty=1.1,
        max_tokens=512,
        callback_manager=callback_manager,
        stream=True,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm_open,
        chain_type="stuff",
        retriever=_retriever,
        return_source_documents=True,
        verbose=True,
        chain_type_kwargs={
            "prompt": PromptTemplate(
                template=template, input_variables=["context", "question"]
            )
        },
    )

    return qa_chain


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

retriever = get_retriever()
qa_chain = get_llm(retriever)

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
        next_response = qa_chain(prompt)
        response = st.write_stream(fake_stream_response(next_response))
        response = next_response["result"]

        st.write("##### Sources")
        st.write(build_source(next_response["source_documents"][:3]))

    st.session_state.messages.append({"role": "assistant", "content": response})


# Who is the instructor for the SQL and Databases class?
# What classes does Graham Hukill teach?
# How many credits do I need to complete the MADS program?
# How does PCA work?

# What is Elle O'Brien's role in the MADS program?
# According to your information, who is Laura Stagnaro?
# Who is Kevyn Collins-Thompson?
# Which class involves time series analysis?
# Who teaches the SQL and Databases class?
# What are the prerequisites for Data Science for Social Good?
# What is a backpack for MADS students?
# When is the latest I can drop a course?
# How do I get an override to take a class?
# How do I take a leave of absence from the MADS program?
