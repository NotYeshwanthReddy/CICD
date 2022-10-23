# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from mockito import mock, verify
from utils import filehandler
# import inference
import unittest


class TestFileHandler(unittest.TestCase): 
    
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def run(self):
        filehand = filehandler.FileHandler()
        process_results = filehand.run(True)
        self.assertEqual(process_results, True)

if __name__ == '__main__': 
    unittest.main() 
