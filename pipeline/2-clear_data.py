# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
import pandas as pd

def clear_data(df): 
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

  print('-----------------------------------------------------------------------------')
  print(analysis_table)

  return df_after