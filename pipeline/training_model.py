# =============================================================================
# Criando e treinando o modelo
# =============================================================================
import pandas as pd
import numpy as np
import json
from gensim.models.phrases import Phrases, Phraser
from gensim.models import word2vec
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score
select = __import__('select_data')

import os
import sys
utils_path = os.getcwd() + '\\utils'
sys.path.insert(0, utils_path)

import random_select
import format_comments

# =============================================================================
# Organização dos dados
# =============================================================================
def select_data(df):
  df = select.select_training_data(df)
  dp = format_comments.DataPreparation()

  corpus = []
  for review in df['text']:
    result = dp.lemmatize(review)
    corpus.append(result[0])
      
  df['corpus'] = corpus
  df['sentiment'] = ['POSITIVO','NEGATIVO','POSITIVO','NEGATIVO','NEGATIVO','POSITIVO','NEUTRO','NEGATIVO','POSITIVO','NEGATIVO','POSITIVO','NEUTRO','NEGATIVO','NEGATIVO','POSITIVO','POSITIVO','POSITIVO','NEGATIVO','POSITIVO','POSITIVO','POSITIVO','NEGATIVO','POSITIVO','POSITIVO','NEUTRO','NEGATIVO', 'NEUTRO','NEUTRO','POSITIVO','NEUTRO','NEUTRO','NEGATIVO','NEGATIVO','POSITIVO','NEUTRO','POSITIVO', 'NEUTRO','NEGATIVO','POSITIVO','POSITIVO','POSITIVO','POSITIVO','POSITIVO','POSITIVO','NEUTRO', 'NEGATIVO','POSITIVO','NEGATIVO','NEGATIVO','NEUTRO','POSITIVO','POSITIVO','NEGATIVO','POSITIVO','NEGATIVO','POSITIVO','POSITIVO','NEUTRO','NEGATIVO','POSITIVO','NEUTRO','NEGATIVO','POSITIVO','POSITIVO','POSITIVO','NEGATIVO','NEGATIVO','POSITIVO','NEUTRO','POSITIVO','POSITIVO','NEUTRO','NEUTRO','NEUTRO','NEUTRO','POSITIVO','NEGATIVO','POSITIVO','NEUTRO','NEUTRO']

  positive = random_select.random_select_sentiment(100, df, 'POSITIVO', 20)
  neutral = random_select.random_select_sentiment(100, df, 'NEUTRO', 20)
  negative = random_select.random_select_sentiment(100, df, 'NEGATIVO', 20)
  selected = np.concatenate([positive, neutral, negative])
  df = df[df['text'].isin(selected)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  return df


# =============================================================================
# Criação do modelo
# =============================================================================
def use_word2vec(corpus):
  words = [line.split() for line in corpus]
  phrases = Phrases(words, min_count=1, threshold=2, progress_per=1000) 
  bigram = Phraser(phrases)
  sentences = bigram[words]

  w2v_model = word2vec.Word2Vec(vector_size=5,window=2,min_count=1,sample=1e-3,epochs=50)
  w2v_model.build_vocab(sentences)

  return w2v_model


# =============================================================================
# Separação dos dados para treinamento
# =============================================================================
def separate_training_and_testing_data(df, is_training = False):
  # Organização dos dados de treino e teste para inserir no algoritmo
  positive_reviews = []
  neutral_reviews = []
  negative_reviews = []

  for classified_review in df:
    if classified_review['sentiment'] == 'POSITIVO':
      positive_reviews.append(classified_review)
    if classified_review['sentiment'] == 'NEUTRO':
      neutral_reviews.append(classified_review)
    if classified_review['sentiment'] == 'NEGATIVO':
      negative_reviews.append(classified_review)

  positive_training = positive_reviews
  neutral_training = neutral_reviews
  negative_training = negative_reviews

  if is_training:
    positive_training = positive_reviews[:5]
    neutral_training = neutral_reviews[:5]
    negative_training = negative_reviews[:5]

    print('-----------------------------------------------------------------------------')
    print('POSITIVO:', len(positive_reviews),'| Treino:', len(positive_training),'| Teste:', len(positive_reviews[5:]))
    print('NEUTRO:', len(neutral_reviews),'  | Treino:', len(neutral_training),'| Teste:', len(neutral_reviews[5:]))
    print('NEGATIVO:', len(negative_reviews),'| Treino:', len(negative_training),'| Teste:', len(negative_reviews[5:]))
    print('-----------------------------------------------------------------------------')

  training_data = positive_training + neutral_training + negative_training
  testing_data = positive_reviews[5:] + neutral_reviews[5:] + negative_reviews[5:]

  return {'testing_data': testing_data,'training_data': training_data}


# =============================================================================
# Teste do modelo
# =============================================================================
def training(df):
  df = select_data(df)
  comparison_data = separate_training_and_testing_data(df.to_dict("records"), True)
  train_data = pd.DataFrame(comparison_data['training_data'])
  test_data = pd.DataFrame(comparison_data['testing_data'])

  w2v_model = use_word2vec(df['corpus'])

  doc_embeddings_train = []
  for row in train_data.iterrows():
    sentence = row[1]['corpus'].split()
    result = []
    for word in sentence:
      try:
        result.append(w2v_model.wv[word])
      except:
        1
    result = np.mean(np.array(result),axis=0)
    doc_embeddings_train.append(result)
  
  w2v_train_df = pd.DataFrame(np.array(doc_embeddings_train))
  
  doc_embeddings_test = []
  for row in test_data.iterrows():
    sentence = row[1]['corpus'].split()
    result = []
    for word in sentence:
      try:
        result.append(w2v_model.wv[word])
      except:
        1
    result = np.mean(np.array(result),axis=0)
    doc_embeddings_test.append(result)
      
  w2v_test_df = pd.DataFrame(np.array(doc_embeddings_test))

  y_train = train_data.iloc[:, -1]
  y_test = test_data.iloc[:, -1]
  mlp = MLPClassifier(hidden_layer_sizes=(100, 50, 10), random_state=7, max_iter=10000)
  mlp.fit(w2v_train_df, y_train)
  w2v_predict = mlp.predict(w2v_test_df)
  acc_test_score = accuracy_score(y_test, w2v_predict)
  pre_test_score = precision_score(y_test, w2v_predict, average='weighted')
    
  print('-----------------------------------------------------------------------------')
  print('Matriz de confusão')
  data = {'Manual': y_test, 'Predito': w2v_predict}
  df_matrix = pd.DataFrame(data, columns=['Manual','Predito'])
  print(pd.crosstab(df_matrix['Manual'], df_matrix['Predito'], rownames=['Manual'], colnames=['Predito']))

  return { 'acc_test_score': acc_test_score,'pre_test_score': pre_test_score }


# =============================================================================
# Aplicação do modelo
def classification_model(data):
  print('antes')
  print(data.shape)
  df = select_data(data)
  print('depois - df')
  print(df.shape)
  comparison_data = separate_training_and_testing_data(df.to_dict("records"))
  train_data = pd.DataFrame(comparison_data['training_data'])

  base_model_lexicon = []

  print('data[corpus]')
  print(data['corpus'])
  print('train_data[corpus]')
  print(train_data['corpus'])
  # for hehe in data.iterrows():
  #   if 'rapir' in hehe[1]['corpus']: print('rapir ', hehe[1]['corpus'])
  w2v_model = use_word2vec(data['corpus'])

  if 'rapir' in w2v_model.wv: print('rapir w2v_model')
  # for word_vec in w2v_model.wv.key_to_index.keys():
  #   print('w2v_model word', word_vec)
  
  doc_embeddings_train = []
  for row in train_data.iterrows():
    sentence = row[1]['corpus'].split()
    result = []
    for word in sentence:
        result.append(w2v_model.wv[word])
    result = np.mean(np.array(result),axis=0)
    doc_embeddings_train.append(result)
  
  w2v_train_df = pd.DataFrame(np.array(doc_embeddings_train))

  doc_embeddings = []  
  for row, index in data.iterrows():
    sentence = row[1]['corpus'].split()
    result = []
    # tem_mais_de_um = False
    for word in sentence:
      result.append(w2v_model.wv[word])
        
    if len(result) > 0: 
      print(index)
      result = np.mean(np.array(result),axis=0)
    else: 
      print('deu ruim')
      result = np.zeros(100)
    doc_embeddings.append(result)

  w2v_df = pd.DataFrame(np.array(doc_embeddings))

  y_train = train_data.iloc[:, -1]

  mlp = MLPClassifier(hidden_layer_sizes=(100, 50, 10), random_state=7, max_iter=10000)
  mlp.fit(w2v_train_df, y_train)
  w2v_predict = mlp.predict(w2v_df)

  data['sentiment'] = w2v_predict

  return data
