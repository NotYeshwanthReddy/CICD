# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from mockito import mock, verify
from model import postprocessing
# import inference
import unittest


class TestPostprocessing(unittest.TestCase): 
    
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def run(self):
        postprocess = postprocessing.Postprocessing()
        process_results = postprocess.run(True)
        self.assertEqual(process_results, True)

if __name__ == '__main__': 
    unittest.main() 
