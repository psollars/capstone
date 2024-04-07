import streamlit as st
from langchain.vectorstores import Chroma
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain_core.prompts import PromptTemplate
import pickle
import time
import random

# base_dir = "./drive/MyDrive/Capstone"
base_dir = "./.."


@st.cache_resource
def get_retriever():
    print("loading context...")
    # Load documents from persistent store
    with open(f"{base_dir}/embeddings/documents.pickle", "rb") as handle:
        documents = pickle.load(handle)
    with open(f"{base_dir}/embeddings/embeddings.pickle", "rb") as handle:
        embeddings = pickle.load(handle)

    document_db = Chroma(
        "documents",
        embedding_function=embeddings,
        persist_directory=f"{base_dir}/embeddings",
        collection_metadata={"hnsw:space": "cosine"},
    )

    chroma_retriever = document_db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 20},
    )

    bm25_retriever = BM25Retriever.from_documents(documents)

    retrievers = [chroma_retriever, bm25_retriever]

    ensemble_retriever = EnsembleRetriever(retrievers=retrievers, weights=[0.5, 0.5])

    print("built retriever...")
    return ensemble_retriever


@st.cache_resource
def get_llm(_retriever, _callback_handler):
    template = """
    Use only the following pieces of context to answer the question at the end.
    Keep your answers concise and do not provide additional explanations or interpretations.
    If the answer cannot be deduced from the context, just say that you don't know the answer, don't try to make up an answer.

    {context}

    Question: {question}
    Helpful Answer:
    """

    std_out = StreamingStdOutCallbackHandler()

    callback_manager = CallbackManager([std_out, _callback_handler])

    llm_open = LlamaCpp(
        model_path=f"{base_dir}/models/mistral-7b-instruct-v0.2.Q4_K_S.gguf",
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


def stream_response(response):
    # response = "This course extends Data Mining I and introduces additional data representations and tasks involved in mining real world data, with a particular focus on sequence modeling, time series analysis, and mining data streams.\xa0 It introduces how to extract patterns, compute similarities/distances of data, and make predictions under these data representations."

    # response
    # "query": "Who teaches the SQL and Databases class?",
    # "result": "...",
    # "source_documents": [
    # Document(
    #     page_content="....",
    #     metadata={
    #        ...
    #     },
    # ),

    for word in response["result"].split():
        yield f"{word} "
        time.sleep(random.uniform(0.001, 0.1))


def main():
    st.title("MADS-RAG")
    st.subheader(
        "A Helpful Chatbot for Master's of Applied Data Science Students at the University of Michigan"
    )
    user_input = st.text_input("Ask a question about MADS:", key="user_input")

    placeholder = st.container()

    callback_handler = StreamlitCallbackHandler(placeholder)

    ensemble_retriever = get_retriever()

    qa_chain = get_llm(ensemble_retriever, callback_handler)

    # Who teaches the SQL and Databases class?
    if st.button("Send"):

        response = qa_chain(user_input)

        print(">>>", response)

        # st.write_stream(stream_response(response))


if __name__ == "__main__":
    main()
