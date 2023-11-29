import numpy as np
import gc

from utils.random_select import random_select


# =============================================================================
# Selecionando avaliações por estrelas
# =============================================================================
def select_data(df):
    positive = random_select(100, df, "POSITIVO", 28000)  # máximo: 78210
    neutral = random_select(100, df, "NEUTRO", 0)  # máximo de neutras: 15834
    negative = random_select(100, df, "NEGATIVO", 28000)  # máximo: 32594
    select = np.concatenate([positive, neutral, negative])

    df = df[df["text"].isin(select)].reset_index(drop=True)
    df = df.sample(frac=1).reset_index(drop=True)

    del positive, neutral, negative, select
    gc.collect()

    return df
