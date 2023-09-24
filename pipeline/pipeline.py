import os
import sys
utils_path = os.getcwd() + '\\utils'
sys.path.insert(0, utils_path)

import print_topic

access = __import__('1-access_data')
clear = __import__('2-clear_data')
select = __import__('3-select_data')
processing_data = __import__('4-processing')
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
# Selecionando as avaliações pelo sentimento (positivo, neutro ou negativo)
# =============================================================================
def select_data(df):
  print_topic.init('Selecionando as avaliações pelo sentimento (positivo, neutro ou negativo)...')
  df = select.select_data(df)
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
# Visualização dos resultados
# =============================================================================
def show_results(df):
  df = show.show_results(df)

  return df