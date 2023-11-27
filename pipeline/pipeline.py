from pipeline.access_data import access_data
from pipeline.clear_data import clear_data
from pipeline.select_data import select_data
from pipeline.pre_processing import pre_processing
from pipeline.processing import processing
from pipeline.storage import insert, update_stats

from utils.test_classification_model import testing
from utils.print_topic import init_topic, finish_topic_default


# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
def step1_access_data():
    init_topic("Acessando os dados disponibilizados...")
    df = access_data()
    finish_topic_default()

    return df


# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
def step2_pre_processing(df):
    init_topic("Pré processamento: análise exploratória, adaptações...")
    df = clear_data(df)
    df = pre_processing(df)
    finish_topic_default()

    return df


# =============================================================================
# Treinando o modelo de análise de sentimento
# =============================================================================
def step_extra_testing_classification_model(df):
    init_topic("Testando o modelo de análise de sentimento...")
    testing(df)
    finish_topic_default()


# =============================================================================
# Processamento dos dados
# =============================================================================
def step3_processing(df):
    init_topic("Processamento dos dados...")
    df = select_data(df)
    df = processing(df)
    finish_topic_default()

    return df


# =============================================================================
# Armazenamento dos dados
# =============================================================================
def step4_storage_data(df):
    init_topic("Armazenando os dados...")
    insert(df)
    finish_topic_default()


def step5_update_data(df):
    init_topic("Armazenando tempo de execução...")
    update_stats(df)
    finish_topic_default()
