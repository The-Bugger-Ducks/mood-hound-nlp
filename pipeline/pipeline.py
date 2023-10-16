import os
import sys
utils_path = os.getcwd() + '/utils'
sys.path.insert(0, utils_path)

import print_topic

access = __import__('1-access_data')
clear = __import__('2-clear_data')
select = __import__('3-select_data')
training_model = __import__('3-training_model')
processing_data = __import__('4-processing')
store = __import__('6-storage')
show = __import__('5-show_results')

# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
def access_data():
  print_topic.init('Acessando os dados disponibilizados...')
  df = access.access_data()
  print_topic.finish_default()

  return df

# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
def clear_data(df):
  print_topic.init('Análise exploratória e adaptações...')
  df = clear.clear_data(df)
  print_topic.finish_default()

  return df

# =============================================================================
# Treinando o modelo de análise de sentimento
# =============================================================================
def training_classification_model():
  print_topic.init('Treinando o modelo de análise de sentimento...')
  classified_reviews = training_model.select_data()
  separated_reviews = training_model.separate_training_and_testing_data(classified_reviews, True)
  training_model.training(separated_reviews['training_data'],separated_reviews['testing_data'])
  training_model.get_accuracy_and_precision(separated_reviews['training_data'],separated_reviews['testing_data'])
  print_topic.finish_default()

# =============================================================================
# Selecionando e classificando o sentimento (positivo ou negativo)
# =============================================================================
def select_data(df):
  print_topic.init('Selecionando e classificando o sentimento (positivo ou negativo)...')
  df = select.select_data(df)
  classified_reviews = training_model.select_data()
  separated_reviews = training_model.separate_training_and_testing_data(classified_reviews, False)
  training_model.classification_model(separated_reviews['training_data'], df)
  print_topic.finish_default()

  return df

# =============================================================================
# Processamento dos dados
# =============================================================================
def processing(df):
  print_topic.init('Processamento dos dados...')
  df = processing_data.processing(df)
  print_topic.finish_default()

  return df

# =============================================================================
# Armazenamento dos dados
# =============================================================================
def storage_data(df):
  print_topic.init('Armazenando os dados...')
  store.insert(df)
  print_topic.finish_default()

# =============================================================================
# Visualização dos resultados
# =============================================================================
def show_results(df):
  show.show_results(df)
