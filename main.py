import os
import sys
pipeline_path = os.path.dirname(os.path.realpath(__file__)) + '\\pipeline'
sys.path.insert(0, pipeline_path)
storage_path = os.path.dirname(os.path.realpath(__file__)) + '\\storage'
sys.path.insert(0, storage_path)

import pipeline

# Acessando os dados disponibilizados
results = pipeline.access_data()

# Análise exploratória e adaptações
results = pipeline.clear_data(results)

# Selecionando dados a serem utilizados na classificação
results = pipeline.select_data(results)

# Processamento dos dados
results = pipeline.processing(results)

# Visualização dos resultados
results = pipeline.show_results(results)
