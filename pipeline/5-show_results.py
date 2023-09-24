# =============================================================================
# Visualização dos resultados
# =============================================================================

def show_results(df):
  # Distribuição geral
  print("Distribuição geral do corpus:\n", df['topic'].value_counts(normalize=True))

  # Distribuição de avaliações negativas
  print("\nDistribuição das avaliações Negativas:\n", df['topic'][df['overall_rating'] == 'Negativo'].value_counts(normalize=True))

  # Distribuição de avaliações neutras
  print("\nDistribuição das avaliações Neutras:\n", df['topic'][df['overall_rating'] == 'Neutro'].value_counts(normalize=True))

  # Distribuição de avaliações positivas
  print("\nDistribuição das avaliações Positivas:\n", df['topic'][df['overall_rating'] == 'Positivo'].value_counts(normalize=True))