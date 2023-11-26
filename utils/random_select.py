import numpy as np


def select(seedNumber, df, sentiment, quantity):
    condition = df["stars"] >= 4  # 4 e 5 "estrelas"
    if sentiment == "NEUTRO":
        condition = df["stars"] == 3  # 3 "estrelas"
    if sentiment == "NEGATIVO":
        condition = df["stars"] <= 2  # 1 e 2 "estrelas"

    np.random.seed(seed=seedNumber)
    return np.random.choice(df["text"][condition], quantity, replace=False)


def random_select_sentiment(seedNumber, df, sentiment, quantity):
    condition = df["sentiment"] == sentiment
    np.random.seed(seed=seedNumber)
    return np.random.choice(df["text"][condition], quantity, replace=False)
