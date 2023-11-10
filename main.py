import os
import sys
from timeit import timeit
import datetime
pipeline_path = os.path.dirname(os.path.realpath(__file__)) + '/pipeline'
sys.path.insert(0, pipeline_path)

import pipeline

def pipe():
  # Acessando os dados disponibilizados
  results = pipeline.access_data()

  # Análise exploratória e adaptações
  results = pipeline.clear_data(results)

# Treinando modelo de análise de sentimento
# pipeline.training_classification_model(results)

  # Processamento dos dados
  results = pipeline.processing(results)

  # Visualização dos resultados
  pipeline.show_results(results)

  # Armazenamento dos dados
  results = pipeline.storage_data(results)

tempo = timeit('pipe()', globals=globals(),number=1)
format = datetime.timedelta(seconds=tempo)
pipeline.update_data(str(format))