# =============================================================================
# Visualização dos resultados
# =============================================================================

def show_results(df):
  # Distribuição geral
  print("Distribuição geral do corpus:\n", df['topic'].value_counts(normalize=True))

  # Distribuição de avaliações negativas
  # print("\nDistribuição das avaliações Negativas:\n", df['topic'][df['sentiment'] == 'NEGATIVO'].value_counts(normalize=True))

  # Distribuição de avaliações positivas
  # print("\nDistribuição das avaliações Positivas:\n", df['topic'][df['sentiment'] == 'POSITIVO'].value_counts(normalize=True))