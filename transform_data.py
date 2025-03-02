import pandas as pd
import os
class DataTransformer:
    def __init__(self, ):
        self.folder_path = 'datos/'
        self.data = None

    def load_data(self):
        all_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.csv')] # List all files in the folder
        self.data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True) # Concatenate all files into one dataframe

    def transform_data(self):
        self.data.dropna(inplace=True)

    def mostrar(self):
        print(self.data.head(100))