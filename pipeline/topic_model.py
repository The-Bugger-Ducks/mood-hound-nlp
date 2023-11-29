from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
from pipeline.storage import update_stats

# =============================================================================
# Criando e treinando o modelo
# =============================================================================
def topic_model(data, num_topics_default):
    try:
        vectorizer = TfidfVectorizer(
            min_df=2,
            max_df=0.75,
            analyzer="word",
            strip_accents="unicode",
            use_idf=True,
            ngram_range=(1, 2),
            max_features=10000,
        )
        feature_vectors = vectorizer.fit_transform(
            [line for line in data["corpus"]]
        ).toarray()
        num_topics = num_topics_default

        nmf = NMF(
            n_components=num_topics, random_state=42, l1_ratio=0.5, init="nndsvdar"
        )
        nmf.fit(feature_vectors)
        print("Non-Negative Matrix Factorization (NMF) concluída")

    except np.core._exceptions._ArrayMemoryError as e:
        memory_error = {
            "erros": {
                "memory_log_error": {
                    "error_type": str(type(e)),
                    "error_message": str(e),
                    "error_bugfix_message": "Considere reduzir a quandidade de dados",
                }
            }
        }
        update_stats(memory_error)

    # Transformação e inserção dos tópicos no Dataset
    print("- Transformação e inserção dos tópicos no Dataset...")
    topic_values = nmf.transform(feature_vectors)
    data["topic"] = topic_values.argmax(axis=1)

    labels = {
        0: "QUALIDADE",
        1: "RECEBIMENTO",
        2: "ENTREGA",
        3: "ENTREGA",
        4: "EXPECTATIVA",
        5: "OUTROS",
        6: "SATISFAÇÃO",
        7: "CUSTO BENEFÍCIO",
        8: "RECOMENDAÇÃO",
        9: "ENTREGA",
    }

    data = data.replace(labels)
    print("Transformação e inserção dos tópicos no Dataset concluída")

    return data
