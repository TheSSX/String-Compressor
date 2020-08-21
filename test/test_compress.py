import unittest
import sys
import os
from sinon import stub, spy
import builtins
import timeit
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.compress import Compressor, compress_and_time

class TestCompression(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "1222311" : "(1, 1) (3, 2) (1, 3) (2, 1)",
            "eeeeeeeeee" : "(10, e)",
            "a" : "(1, a)",
            "123456789123456789123456789" : "(1, 1) (1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7) (1, 8) (1, 9) (1, 1) (1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7) (1, 8) (1, 9) (1, 1) (1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7) (1, 8) (1, 9)"
        }
        self.invalid_data = ["", True, False, None, 1, 0, -1, 1.5, TypeError, [], {}, ()]

    def tearDown(self):
        self.valid_data.clear()
        self.invalid_data.clear()

    def test_basic_valid(self):
        for key, val in self.valid_data.items():
            self.assertEqual(Compressor.basic_compressor(key), val)

    def test_basic_invalid(self):
        for item in self.invalid_data:
            self.assertEqual(Compressor.basic_compressor(item), "Invalid input!")

    def test_advanced_valid(self):
        for key, val in self.valid_data.items():
            self.assertEqual(Compressor.advanced_compressor(key), val)

    def test_advanced_invalid(self):
        for item in self.invalid_data:
            self.assertEqual(Compressor.advanced_compressor(item), "Invalid input!")

class TestInitial(unittest.TestCase):
    def setUp(self):
        self.input_stub = stub(builtins, "input").returns("Test input")
        self.timer_spy = spy(timeit, "default_timer")
        self.print_stub = stub(builtins, "print").returns("")

    def tearDown(self):
        self.input_stub.restore()
        self.timer_spy.restore()
        self.print_stub.restore()

    def test_initial(self):
        compress_and_time()
        self.assertTrue(self.input_stub.calledOnce)
        self.assertTrue(self.print_stub.called)

if __name__ == '__main__':
    unittest.main()
