# =============================================================================
# Importação de bibliotecas
# =============================================================================
import pandas as pd
pd.set_option('max_colwidth', 400)
import numpy as np
import re
from unidecode import unidecode

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, log_loss,confusion_matrix

import spacy
import nltk
from nltk import FreqDist

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#plt.style.use('seaborn')
import seaborn as sns
# %matplotlib inline

import  warnings
warnings.filterwarnings("ignore")

# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
url = 'https://raw.githubusercontent.com/americanas-tech/b2w-reviews01/main/B2W-Reviews01.csv'
df = pd.read_csv(url, sep = ',')
# df.head(5)

# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
df_after = df
df_after = df_after[~df_after['review_text'].isna()].reset_index(drop=True)
df_after = df_after[df_after['review_text'].str.contains("\w")]
df_after = df_after[df_after['review_text'].str.len() > 3]
df_after = df_after.drop_duplicates('review_text').reset_index(drop=True)
df_after['submission_date'] = pd.to_datetime(df_after['submission_date']).dt.strftime('%d/%m/%Y')

analysis_table = {
    'Formato do dataset': [df.shape, df_after.shape], 
    'Avaliações nulas': [df['review_text'].isnull().sum(), df_after['review_text'].isnull().sum()], 
    'Registros duplicados': [df['review_text'].duplicated(keep=False).sum(), df_after['review_text'].duplicated(keep=False).sum()]
}
analysis_table = pd.DataFrame(analysis_table)
analysis_table.index = ['Antes das adaptações', 'Depois das adaptações']
print('=============================================================================')
print('Análise exploratória e adaptações')
print('=============================================================================')
print(analysis_table)

# Dados depois das adaptações
df = df_after
print('=============================================================================')
print('Dados depois das adaptações')
print('=============================================================================')
print(df.head(5))
