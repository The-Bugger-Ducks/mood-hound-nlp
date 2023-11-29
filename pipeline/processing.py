from pipeline.classification_model import classification_model
from pipeline.topic_model import topic_model


# =============================================================================
# Processamento dos dados
# =============================================================================
def processing(data, num_topics_default=7):
    # Análise de sentimentos
    print(
        "-----------------------------------------------------------------------------"
    )
    print("- Análise de sentimentos...")
    data = classification_model(data)
    print("Análise de sentimentos concluída")

    # Non-Negative Matrix Factorization (NMF)
    print(
        "-----------------------------------------------------------------------------"
    )
    print("- Non-Negative Matrix Factorization (NMF)...")
    data = topic_model(data, num_topics_default)

    return data
