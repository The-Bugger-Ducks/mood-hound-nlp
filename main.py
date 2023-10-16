import os
import sys
pipeline_path = os.path.dirname(os.path.realpath(__file__)) + '/pipeline'
sys.path.insert(0, pipeline_path)

import pipeline

# Acessando os dados disponibilizados
results = pipeline.access_data()

# Análise exploratória e adaptações
results = pipeline.clear_data(results)

# Treinando modelo de análise de sentimento
# pipeline.training_classification_model()

# Selecionando dados a serem utilizados na classificação
results = pipeline.select_data(results)

# Processamento dos dados
results = pipeline.processing(results)

# Visualização dos resultados
pipeline.show_results(results)

# Armazenamento dos dados
results = pipeline.storage_data(results)

