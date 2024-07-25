
import unittest
import pandas as pd
from qbpma import QuantumPredictiveMarketAnalysis

class TestQBPMA(unittest.TestCase):
    def setUp(self):
        self.market_data = pd.DataFrame({
            'Open': [100, 102, 104, 103, 101],
            'High': [105, 107, 109, 108, 106],
            'Low': [95, 97, 99, 98, 96],
            'Close': [104, 106, 108, 107, 105],
            'Volume': [1000, 1100, 1050, 1030, 1080]
        }, index=pd.date_range(start='2022-01-01', periods=5))
        self.qbpma = QuantumPredictiveMarketAnalysis(self.market_data)

    def test_train_model(self):
        self.qbpma.train_model(self.market_data)
        self.assertIsNotNone(self.qbpma.model)

    def test_predict_market(self):
        self.qbpma.train_model(self.market_data)
        predictions = self.qbpma.predict_market(self.market_data)
        self.assertEqual(len(predictions), len(self.market_data) - 1)

    def test_quantum_analysis(self):
        result = self.qbpma.quantum_analysis(self.market_data)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
    