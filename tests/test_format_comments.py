import unittest
import spacy
import nltk
nltk.download('rslp')
import pandas as pd
import re
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from utils.format_comments import DataPreparation

nlp = spacy.load("pt_core_news_sm", disable=['parser', 'ner'])
stemmer = nltk.stem.RSLPStemmer()

class TestDataPreparation(unittest.TestCase):
    def setUp(self):
        self.data_preparation = DataPreparation()

    def test_remove_stopwords(self):
        input_text = "Este é um excelente produto"
        cleaned_text = self.data_preparation.remove_stopwords(input_text)
        self.assertNotIn("um", cleaned_text)
        self.assertNotIn("este", cleaned_text)
        self.assertNotIn("um", cleaned_text)

    def test_clean_text(self):
        input_text = str(["Este é um ótimo produto", "A entrega foi rápida"])
        cleaned_corpus = self.data_preparation.clean_text(input_text)
        self.assertEqual(cleaned_corpus, ['ótimo produto entrega rápida'])

    def test_lemmatization(self):
        input_text = ["eu", "sou", "correndo", "eles", "são", "correr"]
        lemmatized_text = self.data_preparation.lemmatization([input_text])
        self.assertEqual(lemmatized_text[0], ["eu", "ser", "correr", "ele", "ser", "correr"])
 
    def test_lemmatize(self):
        input_text = str(["Este é um ótimo produto", "A entrega foi rápida"])
        lemmatized_text = self.data_preparation.lemmatize(input_text)
        self.assertEqual(lemmatized_text, ["bom produto entregar rápido"])

if __name__ == '__main__':
    unittest.main()
