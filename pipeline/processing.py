# =============================================================================
# Processamento dos dados
# =============================================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import os
import sys
import numpy as np
from storage import update_stats

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import utils.format_comments as format_comments
import utils.show_topics as show_topics

training_model = __import__("training_model")


def processing(df, num_topics_default=7):
    # Limpeza dos dados e lematização
    print("- Limpeza dos dados e lematização...")
    dp = format_comments.DataPreparation()
    corpus = []
    for review in df["text"]:
        result = dp.lemmatize(review)
        corpus.append(result[0])
    df["corpus"] = corpus
    print("Limpeza dos dados e lematização concluída ")

    # Análise de sentimentos
    print(
        "-----------------------------------------------------------------------------"
    )
    print("- Análise de sentimentos...")
    df = training_model.classification_model(df)
    print("Análise de sentimentos concluída")

    try:
        # Non-Negative Matrix Factorization (NMF)
        print(
            "-----------------------------------------------------------------------------"
        )
        print("- Non-Negative Matrix Factorization (NMF)...")
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
            [line for line in df["corpus"]]
        ).toarray()
        num_topics = num_topics_default

        nmf = NMF(
            n_components=num_topics, random_state=42, l1_ratio=0.5, init="nndsvdar"
        )
        nmf.fit(feature_vectors)
        nmf_weights = nmf.components_
        nmf_feature_names = vectorizer.get_feature_names_out()
        print("Non-Negative Matrix Factorization (NMF) concluída")

    except np.core._exceptions._ArrayMemoryError as e:
        memory_error = {
            "memory_log_error": {
                "error_type": str(type(e)),
                "error_message": str(e),
                "error_bugfix_message": "Considere reduzir a quandidade de dados",
            }
        }
        update_stats(memory_error)

        raise MemoryError(
            "Erro de memória: Não foi possível alocar 5.35 GiB para array de tamanho (71772, 10000)"
        )

    print(
        "-----------------------------------------------------------------------------"
    )
    print("Tópicos e suas 5 principais palavras")
    topics = show_topics.get_topics_terms_weights(nmf_weights, nmf_feature_names)
    show_topics.print_topics_udf(topics, total_topics=num_topics, num_terms=5)
    print(
        "-----------------------------------------------------------------------------"
    )

    # Transformação e inserção dos tópicos no Dataset
    print("- Transformação e inserção dos tópicos no Dataset...")
    topic_values = nmf.transform(feature_vectors)
    df["topic"] = topic_values.argmax(axis=1)

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

    df = df.replace(labels)
    print("Transformação e inserção dos tópicos no Dataset concluída")

    return df
