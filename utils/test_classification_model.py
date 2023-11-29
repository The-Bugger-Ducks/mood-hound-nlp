import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score
from datetime import datetime

from pipeline.classification_model import training_model
from pipeline.storage import update_stats

# =============================================================================
# Teste do modelo
# =============================================================================
def testing(data):
    model = training_model(data, True)

    doc_embeddings_test = []
    for row in model["test_data"].iterrows():
        sentence = row[1]["corpus"].split()
        result = []
        if len(sentence) > 0:
            for word in sentence:
                result.append(model["w2v_model"].wv[word])
            result = np.mean(np.array(result), axis=0)
            doc_embeddings_test.append(result)
        else:
            model["test_data"].drop(row[0], inplace=True)

    w2v_test_df = pd.DataFrame(np.array(doc_embeddings_test))

    y_train = model["train_data"].iloc[:, -1]
    y_test = model["test_data"].iloc[:, -1]
    mlp = MLPClassifier(
        hidden_layer_sizes=(100, 50, 10), random_state=7, max_iter=10000
    )
    mlp.fit(model["w2v_train_df"], y_train)
    w2v_predict = mlp.predict(w2v_test_df)

    acc_test_score = accuracy_score(y_test, w2v_predict)
    pre_test_score = precision_score(y_test, w2v_predict, average="weighted")

    print(
        "-----------------------------------------------------------------------------"
    )
    print("Acurácia: {:.1f}%".format(acc_test_score * 100))
    print("Precisão: {:.1f}%".format(pre_test_score * 100))

    print(
        "-----------------------------------------------------------------------------"
    )
    print("Matriz de confusão")
    data = {"Manual": y_test, "Predito": w2v_predict}
    df_matrix = pd.DataFrame(data, columns=["Manual", "Predito"])
    confusion_matrix = pd.crosstab(
        df_matrix["Manual"],
        df_matrix["Predito"],
        rownames=["Manual"],
        colnames=["Predito"],
    )
    print(confusion_matrix)

    # Salvar dados
    stats_data = {
        "metrics": {
            "model_accuracy": float(acc_test_score),
            "model_precision": float(pre_test_score),
        },
    }
    update_stats(stats_data)