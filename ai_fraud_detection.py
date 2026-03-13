import pandas as pd
from sklearn.ensemble import IsolationForest

class FraudDetector:

    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def train(self):

        data = [
            {"amount":100},
            {"amount":200},
            {"amount":150},
            {"amount":300},
            {"amount":250},
        ]

        df = pd.DataFrame(data)

        self.model.fit(df[['amount']])

    def predict(self, amount):

        df = pd.DataFrame([[amount]], columns=['amount'])

        result = self.model.predict(df)

        if result[0] == -1:
            return True

        return False
