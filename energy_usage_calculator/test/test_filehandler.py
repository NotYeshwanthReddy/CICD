import unittest
import pandas as pd

from utils.filehandler import FileHandler

class TestFileHandler(unittest.TestCase):
    def __init__(self):
        self.fh = FileHandler()
        
    def test_read_data(self):
        """
        Check if the function is working for all kind of files
        """
        result = self.fh.read_data()
        self.assertEqual(type(result), pd.DataFrame)

    def test_write_data(self):
        """
        Test that it can sum a list of fractions
        """
        result = self.fh.write_data()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
