# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
import pandas as pd

def access_data():
  url = 'https://raw.githubusercontent.com/americanas-tech/b2w-reviews01/main/B2W-Reviews01.csv'
  df = pd.read_csv(url, sep = ',',low_memory=False)
  
  return df


