import unittest
from bot import on_command_error


class TestBot(unittest.TestCase):
    def test_1(self):
        self.assertEqual(on_command_error('error'),'{error}')


if __name__ == '__name__':
    unittest.main()