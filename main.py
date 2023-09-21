import os
import sys
utils_path = os.path.dirname(os.path.realpath(__file__)) + '\\utils'
sys.path.insert(0, utils_path)
pipeline_path = os.path.dirname(os.path.realpath(__file__)) + '\\pipeline'
sys.path.insert(0, pipeline_path)

import print_topic
import organize_rating
import format_comments
import pandas as pd
pd.set_option('max_colwidth', 400)
import numpy as np
import re
from unidecode import unidecode
import spacy
import nltk
import  warnings
from sklearn.feature_extraction.text import TfidfVectorizer
warnings.filterwarnings("ignore")

# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
print_topic.init('Acessando os dados disponibilizados...')

url = 'https://raw.githubusercontent.com/americanas-tech/b2w-reviews01/main/B2W-Reviews01.csv'
df = pd.read_csv(url, sep = ',')

print_topic.finish_default()

# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
print_topic.init('Análise exploratória e adaptações...')

df_after = df
df_after = df_after[~df_after['review_text'].isna()].reset_index(drop=True)
df_after = df_after[df_after['review_text'].str.contains("\w")]
df_after = df_after[df_after['review_text'].str.len() > 3]
df_after = df_after.drop_duplicates('review_text').reset_index(drop=True)
df_after['submission_date'] = pd.to_datetime(df_after['submission_date']).dt.strftime('%d/%m/%Y')
df_after = df_after.drop(columns=[
    'reviewer_id', 
    'product_brand', 
    'site_category_lv1', 
    'site_category_lv2', 
    'review_title',
    'recommend_to_a_friend',
    'reviewer_birth_year',
    'reviewer_gender'])

analysis_table = {
    'Formato do dataset': [df.shape, df_after.shape], 
    'Avaliações nulas': [df['review_text'].isnull().sum(), df_after['review_text'].isnull().sum()], 
    'Registros duplicados': [df['review_text'].duplicated(keep=False).sum(), df_after['review_text'].duplicated(keep=False).sum()]
}
analysis_table = pd.DataFrame(analysis_table)
analysis_table.index = ['Antes das adaptações', 'Depois das adaptações']

print_topic.finish_variation()
print(analysis_table)
print('-----------------------------------------------------------------------------')
# Dados depois das adaptações
df = df_after
print('Dados depois das adaptações')
print(df.head(5))
print('=============================================================================')

df = organize_rating.organize_rating(df)

# =============================================================================
# Pré-processamento do corpus
# =============================================================================
print_topic.init('Pré-processamento do corpus (lemmatization)...')
dp = format_comments.DataPreparation()
corpus = dp.lemmatize(df['review_text'])
print_topic.finish_default()

# =============================================================================
# Vetorização TF-IDF
# =============================================================================
print_topic.init('Pré-processamento do corpus (Vetorização TF-IDF)...')

vectorizer = TfidfVectorizer(min_df=0., max_df=1., strip_accents='unicode', use_idf=True)
feature_vectors = vectorizer.fit_transform(corpus).toarray()
model_lexicon = vectorizer.get_feature_names_out()
feature_df = pd.DataFrame(feature_vectors, columns= model_lexicon).transpose()

print_topic.finish_variation()
print(feature_df)
print('=============================================================================')