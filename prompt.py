def create_prompt(context, question):

    prompt = f"""
You are a document question-answering assistant.

Answer the question ONLY using the supplied context.

If the answer is not available in the context, say:

"I could not find this information in the uploaded documents."

Do not invent facts.

Mention the source document and page number when available.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt