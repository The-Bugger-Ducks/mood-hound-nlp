# =============================================================================
# Criando e treinando o modelo
# =============================================================================
import pandas as pd
import numpy as np
import json
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
import seaborn as sn
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from datetime import datetime
from storage import insert_stats

select = __import__('select_data')

# =============================================================================
# Organização dos dados
def select_data():
  # Captura das reviews previamente classificadas manualmente
  classified_reviews = []
  with open('data.json') as file:
    json_data = json.load(file)
    for classified_review in json_data:
      classified_reviews.append({ 'text': classified_review['text'], 'sentiment': classified_review['sentiment'].upper(), 'predict': '', 'feature_vector': [] })

  return classified_reviews

def separate_training_and_testing_data(classified_reviews, isTraining):
  # Organização dos dados de treino e teste para inserir no algoritmo
  positive_reviews = []
  negative_reviews = []

  for classified_review in classified_reviews:
      if classified_review['sentiment'] == 'POSITIVO':
          positive_reviews.append(classified_review)
      else:
          negative_reviews.append(classified_review)

  positive_training = positive_reviews
  negative_training = negative_reviews

  if isTraining:
    positive_training = positive_reviews[:int((0.2 * len(positive_reviews)))]
    negative_training = negative_reviews[:int((0.2 * len(negative_reviews)))]

    print('-----------------------------------------------------------------------------')
    print('POSITIVO - Total:', len(positive_reviews),'| Quantidade treino (20%):', len(positive_training))
    print('NEGATIVO - Total:', len(negative_reviews),'| Quantidade treino (20%):', len(negative_training))

  training_data = positive_training + negative_training
  testing_data = positive_reviews[int((0.2 * len(positive_reviews))):] + negative_reviews[int((0.2 * len(negative_reviews))):]

  return {'testing_data': testing_data,'training_data': training_data}


# =============================================================================
# Funções do modelo
def build_model_lexicon(words, model_lexicon):
    for word in words:
        if word not in model_lexicon:
            model_lexicon.append(word)
    model_lexicon.sort()

def build_feature_vector(words, model_lexicon):
    bag_of_words_count = np.zeros(len(model_lexicon))
    for pos in range(len(model_lexicon)):
        for word in words:
            if word == model_lexicon[pos]:
                bag_of_words_count[pos] += 1
    return bag_of_words_count

# =============================================================================
# Teste do modelo
def training(training_data, testing_data):
  base_model_lexicon = []

  # Criando o modelo léxico
  # Para os dados de treino
  for classified_review in training_data:
      build_model_lexicon(classified_review['text'].split(), base_model_lexicon)
  # Para os dados de teste
  for unclassified_review in testing_data:
      build_model_lexicon(unclassified_review['text'].split(), base_model_lexicon)

  # Extraindo os vetores considerando o modelo léxico
  # Para os dados de treino
  for classified_review in training_data:
      classified_review['feature_vector'] = build_feature_vector(classified_review['text'].split(), base_model_lexicon)
  # Para os dados de teste
  for unclassified_review in testing_data:
      unclassified_review['feature_vector'] = build_feature_vector(unclassified_review['text'].split(), base_model_lexicon)

  X = [] # feature vectors
  Y = [] # feature classes
  for review in training_data:
      X.append(review['feature_vector'])
      Y.append(review['sentiment'])

  # Configuração do modelo baseado em KNN
  neigh = KNeighborsClassifier(n_neighbors=3)
  neigh.fit(X, Y)

  # index = 1
  # Aplicação do modelo nos dados de teste
  for unclassified_review in testing_data:
      # print(index, ' --------------------------------')
      # index = index + 1
      unclassified_review['predict'] = neigh.predict([unclassified_review['feature_vector']])[0]
      # print('Avaliação:', unclassified_review['text'], ' \nBateu? ', unclassified_review['sentiment'] == unclassified_review['predict'],' | Manual:', unclassified_review['sentiment'],' | Modelo:', unclassified_review['predict'])
      # print('Probabilidades de cada sentimento:', neigh.predict_proba([unclassified_review['feature_vector']]))
      # print('Classes possíveis:',neigh.classes_)

def get_accuracy_and_precision(mannual_classification, model_classification):
  model_results = pd.DataFrame(mannual_classification)
  rating_counts_train = model_results['sentiment'].value_counts()
  rating_p_train = model_results['sentiment'].value_counts(normalize=True).apply(lambda x: '{:.0f}%'.format(x * 100))

  model_results = pd.DataFrame(model_classification)
  rating_counts_test = model_results['predict'].value_counts()
  rating_p_test = model_results['predict'].value_counts(normalize=True).apply(lambda x: '{:.0f}%'.format(x * 100))

  print('-----------------------------------------------------------------------------')
  print('Quadro de proporções')
  print(pd.DataFrame({
    'Qtd (treino)': rating_counts_train,
    'Porcentagem (treino)': rating_p_train,
    'Qtd (teste)': rating_counts_test,
    'Porcentagem (teste)': rating_p_test}))

  unclassified_reviews_mannual = [] 
  unclassified_reviews_model = [] 

  for review in model_classification:
    unclassified_reviews_mannual.append(review['sentiment'])
    unclassified_reviews_model.append(review['predict'])

  print('-----------------------------------------------------------------------------')
  # Calculando a acurácia
  acuracia = accuracy_score(unclassified_reviews_mannual, unclassified_reviews_model)
  print('Acurácia: {:.1f}%'.format(acuracia * 100))

  # Calculando a precisão
  precision = precision_score(unclassified_reviews_mannual, unclassified_reviews_model, pos_label="POSITIVO")
  print('Precision: {:.1f}%'.format(precision * 100))

  print('-----------------------------------------------------------------------------')
  print('Matriz de confusão')
  confusion_matrix = pd.crosstab(
        unclassified_reviews_mannual,
        unclassified_reviews_model, 
        rownames=['Manual'], 
        colnames=['Predito'])
  
  print(confusion_matrix)
  
  # Salvar dados

  confusion_matrix_dict = {
     "verdadeiro_positivo": int(confusion_matrix.at['POSITIVO', 'POSITIVO']),
     "falso_positivo": int(confusion_matrix.at['NEGATIVO', 'POSITIVO']),
     "falso_negativo": int(confusion_matrix.at['POSITIVO', 'NEGATIVO']),
     "verdadeiro_negativo": int(confusion_matrix.at['NEGATIVO', 'NEGATIVO']),
    }
  
  

  stats_data = {
     'model_accuracy':float(acuracia),
     'model_precision':float(precision),
     'confusion_matrix':[confusion_matrix_dict],
     'created_at':datetime.now()
  }

  insert_stats(stats_data)  
  
# =============================================================================
# Aplicação do modelo
def classification_model(training_data, data):
  print('-----------------------------------------------------------------------------')
  print('- Classificando sentimentos...')
  base_model_lexicon = []

  data = data.to_dict("records")
  
  for classified_review in training_data:
      build_model_lexicon(classified_review['text'].split(), base_model_lexicon)
  for unclassified_review in data:
      build_model_lexicon(unclassified_review['text'].split(), base_model_lexicon)

  for classified_review in training_data:
      classified_review['feature_vector'] = build_feature_vector(classified_review['text'].split(), base_model_lexicon)
  for unclassified_review in data:
      unclassified_review['feature_vector'] = build_feature_vector(unclassified_review['text'].split(), base_model_lexicon)

  X = []
  Y = []
  for review in training_data:
      X.append(review['feature_vector'])
      Y.append(review['sentiment'])

  neigh = KNeighborsClassifier(n_neighbors=3)
  neigh.fit(X, Y)

  for unclassified_review in data:
      unclassified_review['sentiment'] = neigh.predict([unclassified_review['feature_vector']])[0]

  data = pd.DataFrame(data)
  data = data.drop(columns=['feature_vector'])

  return data