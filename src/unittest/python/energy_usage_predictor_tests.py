# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
from energy_usage_predictor_tests import inference, train
import unittest


class TestEnergyUsagePredictior(unittest.TestCase): 
      
    def setUp(self): 
        pass

    # Returns True if training works fine. 
    def test_train(self):
        train_response = train()
        self.assertEqual(train_response, True)

    # Returns True if inferencing works fine. 
    def test_inference(self):
        inference_response = inference()
        self.assertEqual(inference_response, True)

if __name__ == '__main__': 
    unittest.main() 
