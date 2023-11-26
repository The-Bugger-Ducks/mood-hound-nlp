# =============================================================================
# Classe para preprocessamento de texto
# =============================================================================
import spacy
import nltk

nltk.download("rslp")
import pandas as pd
import re

nlp = spacy.load("pt_core_news_sm", disable=["parser", "ner"])
stemmer = nltk.stem.RSLPStemmer()


class DataPreparation:
    def remove_stopwords(self, text):
        # Remove stopwords
        stop_words = [word for word in nlp.Defaults.stop_words]
        stop_words.remove("não")
        cleaned_text = " ".join([i for i in text if i not in set(stop_words)])
        return cleaned_text

    def clean_text(self, text):
        # Aplica a remoção de stopwords, caracteres não alfabéticos e outras palavras curtas
        df_corpus = []
        df_c = (
            re.sub("[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]", " ", text)
            .lower()
            .split()
        )
        df_corpus.append(df_c)
        df_corpus = pd.Series(df_corpus).apply(
            lambda x: " ".join([w for w in x if len(w) > 2])
        )
        corpus = [self.remove_stopwords(r.split()) for r in df_corpus]
        return corpus

    def lemmatization(self, text):
        # Extrai o lema das palavras
        global nlp
        output = []
        for word in text:
            doc = nlp(" ".join(word))
            output.append([token.lemma_ for token in doc])
        return output

    def lemmatize(self, text):
        # Aplica a limpeza do texto e a lemmatização
        token = self.lemmatization(
            pd.Series(self.clean_text(text)).apply(lambda x: x.split())
        )
        token_lemma = []
        for i in range(len(token)):
            token_lemma.append(" ".join(token[i]))
        return token_lemma
