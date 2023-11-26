import unittest
import time
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import utils.calculate_time as ct


class TestTimeFunctions(unittest.TestCase):
    def test_init_finish_get(self):
        ct.init()
        time.sleep(5)
        ct.finish()
        result = ct.get()
        self.assertEqual(result, "00:00:05", "Tempo formatado incorretamente")


if __name__ == "__main__":
    unittest.main()
