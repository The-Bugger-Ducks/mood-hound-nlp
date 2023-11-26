import pandas as pd
import numpy as np
from gensim.models import word2vec
from sklearn.neural_network import MLPClassifier

from utils.random_select import random_select, random_select_sentiment
from utils.format_comments import DataPreparation


# =============================================================================
# Organização dos dados
# =============================================================================
def select_mock_data(df):
    positive = random_select(100, df, "POSITIVO", 15)
    neutral = random_select(100, df, "NEUTRO", 45)
    negative = random_select(100, df, "NEGATIVO", 20)
    select = np.concatenate([positive, neutral, negative])
    df = df[df["text"].isin(select)].reset_index(drop=True)
    df = df.sample(frac=1).reset_index(drop=True)

    dp = DataPreparation()

    corpus = []
    for review in df["text"]:
        result = dp.lemmatize(review)
        corpus.append(result[0])

    df["corpus"] = corpus
    df["sentiment"] = [
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEGATIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "NEUTRO",
        "NEUTRO",
        "POSITIVO",
        "NEUTRO",
        "NEUTRO",
        "NEGATIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "POSITIVO",
        "NEGATIVO",
        "NEGATIVO",
        "NEUTRO",
        "POSITIVO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "NEGATIVO",
        "POSITIVO",
        "POSITIVO",
        "POSITIVO",
        "NEGATIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "POSITIVO",
        "POSITIVO",
        "NEUTRO",
        "NEUTRO",
        "NEUTRO",
        "NEUTRO",
        "POSITIVO",
        "NEGATIVO",
        "POSITIVO",
        "NEUTRO",
        "NEUTRO",
    ]

    positive = random_select_sentiment(100, df, "POSITIVO", 20)
    neutral = random_select_sentiment(100, df, "NEUTRO", 20)
    negative = random_select_sentiment(100, df, "NEGATIVO", 20)
    selected = np.concatenate([positive, neutral, negative])
    df = df[df["text"].isin(selected)].reset_index(drop=True)
    df = df.sample(frac=1).reset_index(drop=True)

    return df


# =============================================================================
# Separação dos dados para treinamento
# =============================================================================
def separate_training_and_testing_data(df, is_testing=False):
    # Organização dos dados de treino e teste para inserir no algoritmo
    positive_reviews = []
    neutral_reviews = []
    negative_reviews = []

    for classified_review in df:
        if classified_review["sentiment"] == "POSITIVO":
            positive_reviews.append(classified_review)
        if classified_review["sentiment"] == "NEUTRO":
            neutral_reviews.append(classified_review)
        if classified_review["sentiment"] == "NEGATIVO":
            negative_reviews.append(classified_review)

    positive_training = positive_reviews
    neutral_training = neutral_reviews
    negative_training = negative_reviews

    if is_testing:
        positive_training = positive_reviews[:5]
        neutral_training = neutral_reviews[:5]
        negative_training = negative_reviews[:5]

        print(
            "-----------------------------------------------------------------------------"
        )
        data = {
            "POSITIVO": [len(positive_training), len(positive_reviews[5:])],
            "NEUTRO": [len(neutral_training), len(neutral_reviews[5:])],
            "NEGATIVO": [len(negative_training), len(negative_reviews[5:])],
        }
        print(pd.DataFrame(data, columns=["Treino", "Teste"]))

    training_data = positive_training + neutral_training + negative_training
    testing_data = positive_reviews[5:] + neutral_reviews[5:] + negative_reviews[5:]

    return {"testing_data": testing_data, "training_data": training_data}


# =============================================================================
# Treinamento do modelo
# =============================================================================
def training_model(data, is_testing=False):
    df = select_mock_data(data)
    comparison_data = separate_training_and_testing_data(
        df.to_dict("records"), is_testing
    )
    train_data = pd.DataFrame(comparison_data["training_data"])

    sentences = [line.split() for line in data["corpus"]]
    w2v_model = word2vec.Word2Vec(
        sentences, vector_size=5, window=2, min_count=1, sample=1e-3, epochs=50
    )

    doc_embeddings_train = []
    for row in train_data.iterrows():
        sentence = row[1]["corpus"].split()
        result = []
        if len(sentence) > 0:
            for word in sentence:
                result.append(w2v_model.wv[word])
            result = np.mean(np.array(result), axis=0)
            doc_embeddings_train.append(result)
        else:
            train_data.drop(row[0], inplace=True)
            data.drop(row[0], inplace=True)

    w2v_train_df = pd.DataFrame(np.array(doc_embeddings_train))

    return {
        "train_data": train_data,
        "w2v_model": w2v_model,
        "w2v_train_df": w2v_train_df,
        "test_data": pd.DataFrame(comparison_data["testing_data"]),
    }


# =============================================================================
# Modelo
# =============================================================================
def classification_model(data):
    model = training_model(data)

    doc_embeddings = []
    for row in data.iterrows():
        sentence = row[1]["corpus"].split()
        result = []
        if len(sentence) > 0:
            for word in sentence:
                result.append(model["w2v_model"].wv[word])
            result = np.mean(np.array(result), axis=0)
            doc_embeddings.append(result)
        else:
            data.drop(row[0], inplace=True)

    w2v_df = pd.DataFrame(np.array(doc_embeddings))

    y_train = model["train_data"].iloc[:, -1]

    mlp = MLPClassifier(
        hidden_layer_sizes=(100, 50, 10), random_state=7, max_iter=10000
    )
    mlp.fit(model["w2v_train_df"], y_train)
    w2v_predict = mlp.predict(w2v_df)

    data["sentiment"] = w2v_predict

    return data
