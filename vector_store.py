import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []

    def create_store(self, documents):
        """
        Create embeddings and store them in FAISS.
        """

        self.documents = documents

        texts = [doc["text"] for doc in documents]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        embeddings = embeddings.astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

    def search(self, query, top_k=5):
        """
        Find the most relevant document chunks.
        """

        if self.index is None or len(self.documents) == 0:
            return []

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        query_embedding = query_embedding.astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            min(top_k, len(self.documents))
        )

        results = []

        for distance, index in zip(distances[0], indices[0]):
            if index < 0:
                continue

            document = self.documents[index].copy()
            document["score"] = float(distance)

            results.append(document)

        return results