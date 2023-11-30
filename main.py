from timeit import timeit
import datetime

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
    step_extra_testing_classification_model(results)

    # Processamento dos dados
    results = step3_processing(results)

    # Armazenamento dos dados
    results = step4_storage_data(results)


tempo = timeit("pipe()", globals=globals(), number=1)
format = datetime.timedelta(seconds=tempo)
step5_update_data(str(format))
