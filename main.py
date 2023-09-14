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
