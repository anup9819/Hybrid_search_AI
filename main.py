import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

vectorizer = TfidfVectorizer()
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open("documents.json", "r") as f:
    documents = json.load(f)

document_texts = [doc["content"]for doc in documents]
document_vectors = vectorizer.fit_transform(document_texts) # for keyword mactching
document_embeddings = embedding_model.encode(document_texts) # for semantic matching

#more statistical based fixed result
def keyword_search(query, k=3):
    results = []

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    ranked_indices = similarities.argsort()[::-1] #gives the most similar indices and not the sorted on values
    top_results = ranked_indices[:k]
    # for idx in top_results:
    #     print(documents[idx]["id"], similarities[idx])
    for idx in top_results:
        results.append({
        "id": documents[idx]["id"],
        "type": documents[idx]["type"],
        "content": documents[idx]["content"],
        "score": float(similarities[idx])
    })

    return results
# more curated results as the checks are in-depth now
def semantic_search(query, k=3):

    results = []

    # Convert query into embedding
    query_embedding = embedding_model.encode([query])

    # Compare query embedding with document embeddings
    similarities = cosine_similarity(
        query_embedding,
        document_embeddings
    ).flatten()

    # Rank documents
    ranked_indices = similarities.argsort()[::-1]

    top_results = ranked_indices[:k]

    # Build structured results
    for idx in top_results:

        results.append({
            "id": documents[idx]["id"],
            "type": documents[idx]["type"],
            "content": documents[idx]["content"],
            "score": float(similarities[idx])
        })

    return results

# query = "specs for ASTM C150 cement" # for keyword matching
query = "what do we do if pouring concrete when it's freezing outside?"


results = semantic_search(query)

for result in results:
    print(result)