import numpy as np

def select(seedNumber, df, sentiment, quantity):
  np.random.seed(seed=seedNumber)
  return np.random.choice(df['text'][df['sentiment'] == sentiment], quantity, replace=False)