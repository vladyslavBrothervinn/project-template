import unittest
import pandas as pd
from app.io.input import read_file, read_file_pandas


class TestReadFile(unittest.TestCase):

    def test_read_file_exists(self):
        result = read_file('test_data/test_file.txt')
        self.assertIsNotNone(result)

    def test_read_file_content(self):
        expected_content = "This is a test file.\nIt contains some text."
        result = read_file('test_data/test_file.txt')
        self.assertEqual(result, expected_content)

    def test_read_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file('test_data/nonexistent_file.txt')


class TestReadFilePandas(unittest.TestCase):

    def test_read_file_pandas_exists(self):
        result = read_file_pandas('test_data/test_file.csv')
        self.assertIsInstance(result, pd.DataFrame)

    def test_read_file_pandas_content(self):
        expected_columns = ['col1', 'col2']
        expected_data = [[1, 2], [3, 4]]
        result = read_file_pandas('test_data/test_file.csv')
        self.assertEqual(list(result.columns), expected_columns)
        self.assertListEqual(result.values.tolist(), expected_data)

    def test_read_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas('test_data/nonexistent_file.csv')


if __name__ == '__main__':
    unittest.main()
