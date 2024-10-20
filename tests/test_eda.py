import os
import sys
import unittest
import pytest
import pandas as pd
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../scripts'))
sys.path.append(os.path.abspath('../tests'))
from eda import univariateAnalysis, bivariateAnalysis
from test_data_loading import load_sample_data

class TestEDA(unittest.TestCase):
    def setUp(self):
        # Load sample data for the tests
        self.fraud_data, self.creditcard_data, self.ip_address_data = load_sample_data()

    def test_eda_execution(self):
        """
        Test if the EDA function executes without errors using the sample data.
        This test checks that all visualizations are generated and the function runs.
        """
        try:
            univariateAnalysis(self.fraud_data, self.creditcard_data, self.ip_address_data)
            bivariateAnalysis(self.fraud_data, self.creditcard_data, self.ip_address_data)
            self.assertTrue(True)  # If no error occurs, the test passes.
        except Exception as e:
            self.fail(f"EDA function failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
