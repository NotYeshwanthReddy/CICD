# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from mockito import mock, verify
from utils import config
# import inference
import unittest


class TestPostprocessing(unittest.TestCase): 
    
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def run(self):
        type_of_config = type(config.config)
        self.assertEqual(type_of_config, type(dict()))

if __name__ == '__main__': 
    unittest.main() 
