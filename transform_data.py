import pandas as pd

class DataTransformer:
    def __init__(self):
        self.file_path = 'datos/season-2425.csv'
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def transform_data(self):
        print("Datos transformados:")

    def mostrar(self):
        print(self.data.head(10))