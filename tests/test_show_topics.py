import unittest
import os
import sys
import numpy as np

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from utils.show_topics import get_topics_terms_weights


class TestGetTopicsTermsWeights(unittest.TestCase):
    def test_get_topics_terms_weights(self):
        weights = np.array([[0.2, 0.1, 0.5, 0.3], [0.3, 0.2, 0.4, 0.1]])
        feature_names = ["word1", "word2", "word3", "word4"]

        topics = get_topics_terms_weights(weights, feature_names)
        self.assertEqual(len(topics), len(weights))
        for topic in topics:
            for term, weight in topic:
                self.assertIn(term, feature_names)
                self.assertIsInstance(float(weight), float)


if __name__ == "__main__":
    unittest.main()
