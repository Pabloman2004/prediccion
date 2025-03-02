import numpy as np
import pandas as pd
import transform_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class PredictMatch:
    def __init__(self):
        self.data = None
        self.model = RandomForestClassifier()

    def load_data(self):
        transformer = transform_data.DataTransformer()
        transformer.load_data()
        self.data = transformer.data
        transformer.mostrar()

