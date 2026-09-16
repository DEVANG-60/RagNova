import os
import streamlit as st
from dotenv import load_dotenv

from rag_pipeline import RAGPipeline


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RAGNova",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# ENVIRONMENT
# =========================================================

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       MAIN APPLICATION
       ========================= */

    .stApp {
        background: #0b1120 !important;
    }

    [data-testid="stAppViewContainer"] {
        background: #0b1120 !important;
    }

    [data-testid="stMain"] {
        background: #0b1120 !important;
    }

    .main .block-container {
        max-width: 1200px;
        padding-top: 40px;
        padding-bottom: 60px;
    }


    /* =========================
       SIDEBAR
       ========================= */

    [data-testid="stSidebar"] {
        background: #111827 !important;
    }

    [data-testid="stSidebar"] > div {
        background: #111827 !important;
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    [data-testid="stSidebar"] h1 {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] h2 {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }


    /* =========================
       NORMAL TEXT
       ========================= */

    .stApp p {
        color: #cbd5e1;
    }

    .stApp label {
        color: #e2e8f0 !important;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3 {
        color: #ffffff !important;
    }


    /* =========================
       HERO CONTAINER
       ========================= */

    .hero-box {
        background: #111827;
        border: 1px solid #263247;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-box h1 {
        color: #ffffff !important;
        font-size: 46px !important;
        margin-bottom: 10px;
    }

    .hero-box p {
        color: #94a3b8 !important;
        font-size: 18px;
    }


    /* =========================
       FEATURE CARDS
       ========================= */

    .feature-card {
        background: #111827;
        border: 1px solid #263247;
        border-radius: 16px;
        padding: 25px;
        min-height: 180px;
    }

    .feature-card h3 {
        color: #ffffff !important;
        margin-bottom: 10px;
    }

    .feature-card p {
        color: #94a3b8 !important;
        line-height: 1.6;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        width: 100%;
        min-height: 45px;
        border-radius: 10px;
        border: 1px solid #334155;
        background: #2563eb;
        color: #ffffff !important;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #1d4ed8;
        border-color: #60a5fa;
    }


    /* =========================
       FILE UPLOADER
       ========================= */

    [data-testid="stFileUploader"] {
        background: #0f172a !important;
        border: 1px solid #263247;
        border-radius: 12px;
        padding: 10px;
    }

    [data-testid="stFileUploader"] section {
        background: #0f172a !important;
    }


    /* =========================
       CHAT
       ========================= */

    [data-testid="stChatMessage"] {
        background: #111827 !important;
        border: 1px solid #263247;
        border-radius: 14px;
        margin-bottom: 12px;
    }

    [data-testid="stChatMessage"] p {
        color: #e2e8f0 !important;
    }


    /* =========================
       CHAT INPUT
       ========================= */

    [data-testid="stChatInput"] {
        background: #111827 !important;
        border: 1px solid #334155 !important;
    }

    [data-testid="stChatInput"] textarea {
        background: #111827 !important;
        color: #ffffff !important;
    }


    /* =========================
       SOURCE BOX
       ========================= */

    .source-box {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 12px;
        margin-top: 8px;
    }

    .source-box p {
        color: #cbd5e1 !important;
    }


    /* =========================
       DIVIDER
       ========================= */

    hr {
        border-color: #263247 !important;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer-text {
        text-align: center;
        color: #64748b !important;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #263247;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "rag" not in st.session_state:
    st.session_state.rag = None

if "documents_processed" not in st.session_state:
    st.session_state.documents_processed = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🚀 RAGNova")

    st.caption(
        "Retrieval-Augmented Document Intelligence"
    )

    st.divider()

    st.subheader("📄 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.write("**Selected Files:**")

        for file in uploaded_files:
            st.write("📘 " + file.name)

    st.write("")

    if st.button("⚡ Process Documents"):

        if not API_KEY:

            st.error(
                "GROQ_API_KEY is missing. "
                "Please add it to your .env file."
            )

        elif not uploaded_files:

            st.warning(
                "Please upload at least one PDF document."
            )

        else:

            with st.spinner("Processing your documents..."):

                try:

                    st.session_state.rag = RAGPipeline(API_KEY)

                    success = st.session_state.rag.process_documents(
                        uploaded_files
                    )

                    if success:

                        st.session_state.documents_processed = True
                        st.session_state.chat_history = []

                        st.success(
                            "Documents processed successfully!"
                        )

                    else:

                        st.error(
                            "No readable text was found "
                            "in the uploaded PDF."
                        )

                except Exception as e:

                    st.error(
                        f"Processing error: {e}"
                    )

    if st.session_state.documents_processed:

        st.success("🟢 RAGNova Ready")

        if st.button("🗑️ Clear Chat"):

            st.session_state.chat_history = []

            st.rerun()

    st.divider()

    st.subheader("🔄 RAG Pipeline")

    st.write("1️⃣ PDF Upload")
    st.write("2️⃣ Text Extraction")
    st.write("3️⃣ Text Chunking")
    st.write("4️⃣ Embeddings")
    st.write("5️⃣ FAISS Retrieval")
    st.write("6️⃣ Grounded Answer")

    st.divider()

    st.caption(
        "RAGNova • Domain-Specific RAG Chatbot"
    )


# =========================================================
# HOME PAGE
# =========================================================

if not st.session_state.documents_processed:

    st.markdown(
        """
        <div class="hero-box">
            <h1>🚀 RAGNova</h1>
            <p>
                Ask Your Documents. Get Grounded Answers.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("👋 Welcome to RAGNova")

    st.write(
        "RAGNova is a Domain-Specific Retrieval-Augmented "
        "Generation system that allows you to ask questions "
        "directly from your PDF documents."
    )

    st.write("")

    st.subheader("✨ What RAGNova Does")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="feature-card">
                <h3>📄 Understand Documents</h3>
                <p>
                    Extracts and processes information
                    from your uploaded PDF documents.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">
                <h3>🔍 Retrieve Knowledge</h3>
                <p>
                    Finds the most relevant passages
                    using semantic similarity.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="feature-card">
                <h3>💬 Generate Answers</h3>
                <p>
                    Generates answers using the
                    retrieved document context.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.info(
        "👉 Upload a PDF from the sidebar and click "
        "'Process Documents' to start asking questions."
    )


# =========================================================
# CHAT PAGE
# =========================================================

else:

    st.title("💬 Ask RAGNova")

    st.write(
        "Ask questions about your uploaded documents."
    )

    st.divider()

    # ---------------------------------------------
    # Previous conversation
    # ---------------------------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            if message["role"] == "assistant":

                sources = message.get("sources", [])

                if sources:

                    st.markdown("**📚 Sources**")

                    for source in sources:

                        st.markdown(
                            f"""
                            <div class="source-box">
                                📄 {source["source"]}
                                &nbsp;&nbsp; | &nbsp;&nbsp;
                                📖 Page {source["page"]}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

    # ---------------------------------------------
    # New question
    # ---------------------------------------------

    question = st.chat_input(
        "Ask something about your PDF..."
    )

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("Searching your documents..."):

                try:

                    answer, sources = (
                        st.session_state.rag.ask_question(
                            question
                        )
                    )

                    st.write(answer)

                    if sources:

                        st.markdown("**📚 Sources**")

                        for source in sources:

                            st.markdown(
                                f"""
                                <div class="source-box">
                                    📄 {source["source"]}
                                    &nbsp;&nbsp; | &nbsp;&nbsp;
                                    📖 Page {source["page"]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                    st.session_state.chat_history.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": sources
                        }
                    )

                except Exception as e:

                    error_message = (
                        f"Something went wrong: {e}"
                    )

                    st.error(error_message)

                    st.session_state.chat_history.append(
                        {
                            "role": "assistant",
                            "content": error_message,
                            "sources": []
                        }
                    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer-text">
        RAGNova — Domain-Specific Retrieval-Augmented Generation
        <br>
        Intelligent PDF Question Answering
    </div>
    """,
    unsafe_allow_html=True
)