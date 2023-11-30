from timeit import timeit
from datetime import datetime, timedelta

from pipeline.pipeline import (
    step1_access_data,
    step2_pre_processing,
    step3_processing,
    step4_storage_data,
    step5_update_data,
    step_extra_testing_classification_model,
)


def pipe():
    # Acessando os dados disponibilizados
    results = step1_access_data()

    # Análise exploratória e adaptações
    results = step2_pre_processing(results)

    # Treinando modelo de análise de sentimento
    # step_extra_testing_classification_model(results)

    # Processamento dos dados
    results = step3_processing(results)

    # Armazenamento dos dados
    results = step4_storage_data(results)


tempo = timeit("pipe()", globals=globals(), number=1)
timedelta_time = timedelta(seconds=tempo)
format = str(timedelta_time)
data_format = {"metrics": {"stage": "Pipeline completa", "day": datetime.now(), "time": format}}

step5_update_data(str(format))
