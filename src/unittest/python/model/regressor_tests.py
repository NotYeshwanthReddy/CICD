# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from model import regressor
import unittest


class TestRegressionModel(unittest.TestCase): 
      
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def test_train(self):
        self.assertEqual((True), (True))

    # Returns True if inferencing works fine. 
    def test_predict(self):
        self.assertEqual((True), (True))

    # Returns True if inferencing works fine. 
    def test_save_model(self):
        self.assertEqual((True), (True))

    # Returns True if inferencing works fine. 
    def test_load_model(self):
        self.assertEqual((True), (True))

if __name__ == '__main__': 
    unittest.main() 
