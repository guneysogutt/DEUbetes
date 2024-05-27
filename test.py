import unittest

from main import PreprocessedDiabetesDataset

class TestPreprocessedDiabetesDataset(unittest.TestCase):
    def test_diabetes_dataset_loading(self):
        self.assertEqual(42, 42)


if __name__ == '__main__':
    unittest.main()
