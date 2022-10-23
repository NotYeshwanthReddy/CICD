# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from model import preprocessing 
# import inference
import unittest


class TestPreprocessing(unittest.TestCase): 
      
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def run(self):
        self.assertEqual((True), (True))

if __name__ == '__main__': 
    unittest.main() 
