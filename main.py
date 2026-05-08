<<<<<<< HEAD
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


def hybrid_search(query, k=3):
    keyword_results = keyword_search(query,k=len(documents))
    semantic_results = semantic_search(query,k=len(documents))
    rrf_scores = {}
    rrf_k = 60
    for rank, result in enumerate(keyword_results,start=1):
        doc_id = result["id"]
        rrf_scores[doc_id] = (rrf_scores.get(doc_id, 0)+ 1 / (rrf_k + rank))
    for rank, result in enumerate(semantic_results,start=1):
        doc_id = result["id"]
        rrf_scores[doc_id] = (rrf_scores.get(doc_id, 0)+ 1 / (rrf_k + rank))

    reranked_results = sorted( rrf_scores.items(),key=lambda x: x[1],reverse=True)

    final_results = []  

    for doc_id, score in reranked_results[:k]:

        for doc in documents:

            if doc["id"] == doc_id:

                final_results.append({
                    "id": doc["id"],
                    "type": doc["type"],
                    "content": doc["content"],
                    "rrf_score": score
                })
    return final_results

# query = "specs for ASTM C150 cement" # for keyword matching
query = "what do we do if pouring concrete when it's freezing outside?"


results = hybrid_search(query)


#impovements display result
def display_results(results):
        for rank, result in enumerate(results, start=1):
            print("=" * 50)

            print(f"RANK {rank}")

            print(f"Document ID : {result['id']}")
            print(f"Type        : {result['type']}")

            if "rrf_score" in result:
                print(f"RRF Score   : {result['rrf_score']:.4f}")

            elif "score" in result:
                print(f"Score       : {result['score']:.4f}")

            print("\nContent:")
            print(result["content"])

            print("\n")
display_results(results)
=======
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
>>>>>>> a95cbe851e25ec9f64796620b0d3f1dab8b85881
