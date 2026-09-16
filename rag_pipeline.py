from langchain_text_splitters import RecursiveCharacterTextSplitter
from groq import Groq

from document_loader import extract_text_from_pdf
from vector_store import VectorStore
from prompt import create_prompt


class RAGPipeline:

    def __init__(self, api_key):

        self.vector_store = VectorStore()

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=120
        )

        self.client = Groq(api_key=api_key)

    def process_documents(self, pdf_files):

        all_chunks = []

        for pdf_file in pdf_files:

            pages = extract_text_from_pdf(pdf_file)

            for page in pages:

                chunks = self.splitter.split_text(
                    page["text"]
                )

                for chunk in chunks:

                    all_chunks.append({
                        "text": chunk,
                        "page": page["page"],
                        "source": page["source"]
                    })

        if not all_chunks:
            return False

        self.vector_store.create_store(all_chunks)

        return True

    def ask_question(self, question):

        results = self.vector_store.search(
            question,
            top_k=5
        )

        if not results:
            return (
                "I could not find this information in "
                "the uploaded documents.",
                []
            )

        context_parts = []

        for result in results:

            context_parts.append(
                f"""
Source: {result['source']}
Page: {result['page']}

{result['text']}
"""
            )

        context = "\n".join(context_parts)

        prompt = create_prompt(
            context,
            question
        )

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        answer = response.choices[0].message.content

        return answer, results