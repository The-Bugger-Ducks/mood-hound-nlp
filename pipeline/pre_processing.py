from utils.format_comments import DataPreparation


# =============================================================================
# Pré processamento dos dados
# =============================================================================
def pre_processing(df):
    # Limpeza dos dados e lematização
    print("- Limpeza dos dados e lematização...")
    dp = DataPreparation()
    corpus = []
    for review in df["text"]:
        result = dp.lemmatize(review)
        corpus.append(result[0])
    df["corpus"] = corpus
    print("Limpeza dos dados e lematização concluída ")

    return df
