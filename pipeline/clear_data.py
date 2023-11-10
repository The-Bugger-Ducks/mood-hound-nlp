# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
import pandas as pd
from datetime import datetime

def clear_data(df): 
  df_after = df
  df_after.rename(columns = {'overall_rating': 'stars','submission_date':'created_at','review_text':'text'}, inplace=True)
  df_after['processed_at'] = datetime.now()
  df_after = df_after[~df_after['text'].isna()].reset_index(drop=True)
  df_after = df_after[df_after['text'].str.contains("\w")]
  df_after = df_after[df_after['text'].str.len() > 3]
  df_after = df_after.drop_duplicates('text').reset_index(drop=True)
  df_after['created_at'] = pd.to_datetime(df_after['created_at'])
  df_after = df_after.drop(columns=[
      'reviewer_id', 
      'product_brand', 
      'site_category_lv1', 
      'site_category_lv2', 
      'review_title',
      'recommend_to_a_friend'])
  analysis_table = {
      'Formato do dataset': [df.shape, df_after.shape], 
      'Avaliações nulas': [df['text'].isnull().sum(), df_after['text'].isnull().sum()], 
      'Registros duplicados': [df['text'].duplicated(keep=False).sum(), df_after['text'].duplicated(keep=False).sum()]
  }

  analysis_table = pd.DataFrame(analysis_table)
  analysis_table.index = ['Antes das adaptações', 'Depois das adaptações']

  print('-----------------------------------------------------------------------------')
  print(analysis_table)

  return df_after