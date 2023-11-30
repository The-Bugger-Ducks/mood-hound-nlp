import unittest
import time

from utils.calculate_time import init, finish, get


class TestTimeFunctions(unittest.TestCase):
    def test_init_finish_get(self):
        init()
        time.sleep(5)
        finish()
        result = get()
        self.assertEqual(result, "00:00:05", "Tempo formatado incorretamente")


if __name__ == "__main__":
    unittest.main()
