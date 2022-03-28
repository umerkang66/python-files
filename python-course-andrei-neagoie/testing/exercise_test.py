import unittest
import exercise


class TestGame(unittest.TestCase):
    def test_input(self):
        result = exercise.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = exercise.run_guess(5, 4)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = exercise.run_guess(5, 15)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = exercise.run_guess(5, "15")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
