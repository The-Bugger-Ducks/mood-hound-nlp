from pipeline.access_data import access_data
from pipeline.clear_data import clear_data
from pipeline.select_data import select_data
from pipeline.pre_processing import pre_processing
from pipeline.processing import processing
from pipeline.storage import insert, insert_stats, update_stats

from utils.test_classification_model import testing
from utils.print_topic import init_topic, finish_topic_default
from datetime import datetime


# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
def step1_access_data():
    init_topic("Acessando os dados disponibilizados...")
    df = access_data()
    exec_time = finish_topic_default()
    insert_stats([
        {"erros": [],
         "created_at" : datetime.now()}])

    update_stats(
        {
            "metrics": {
                "stage": "Acesso aos dados",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )

    

    return df




# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
def step2_pre_processing(df):
    init_topic("Pré processamento: análise exploratória, adaptações...")
    df = clear_data(df)
    df = pre_processing(df)
    exec_time = finish_topic_default()

    update_stats(
        {
            "metrics": {
                "stage": "Pré processamento",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )

    return df


# =============================================================================
# Treinando o modelo de análise de sentimento
# =============================================================================
def step_extra_testing_classification_model(df):
    init_topic("Testando o modelo de análise de sentimento...")
    testing(df)
    exec_time = finish_topic_default()

    update_stats(
        {
            "metrics": {
                "stage": "Treinamento do modelo",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )


# =============================================================================
# Processamento dos dados
# =============================================================================
def step3_processing(df):
    init_topic("Processamento dos dados...")
    df = select_data(df)
    df = processing(df)
    exec_time = finish_topic_default()

    update_stats(
        {
            "metrics": {
                "stage": "Processamento de dados",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )

    return df


# =============================================================================
# Armazenamento dos dados
# =============================================================================
def step4_storage_data(df):
    init_topic("Armazenando os dados...")
    insert(df)
    exec_time = finish_topic_default()

    update_stats(
        {
            "metrics": {
                "stage": "Armazenamento de dados",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )


def step5_update_data(df):
    init_topic("Armazenando tempo de execução...")
    update_stats(df)
    exec_time = finish_topic_default()

    update_stats(
        {
            "metrics": {
                "stage": "Atualizando métricas",
                "day": datetime.now(),
                "time": exec_time,
            }
        }
    )


