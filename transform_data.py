import pandas as pd
import os

def data_match(data,equipoL, equipoV):
    toRet = []
    contD = 0
    cont = 0
    for i in range(len(data)):
        if data['HomeTeam'][i] == equipoL and data['AwayTeam'][i] == equipoV and contD<=10: #PARA AÑADIR LOS ENFRETAMIENTOS DIRECTOS
            contD += 1
            if data['FTR'][i] == 'H':
                toRet.append(equipoL)
            elif data['FTR'][i] == 'D':
                toRet.append(equipoV)
            else:
                toRet.append('empate')
        
    new_data = pd.DataFrame({'enfrentamiento' : toRet})    
    return new_data


class DataTransformer:
    def __init__(self, ):
        self.folder_path = 'datos/'
        self.data = None

    def load_data(self, equipoL, equipoV):
        all_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.csv')] # List all files in the folder
        self.data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True) # Concatenate all files into one dataframe
        self.useful_data = data_match(self.data, equipoL, equipoV)
        return self.useful_data
    
    def mostrar(self, x):
        print(x)