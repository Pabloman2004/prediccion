import pandas as pd
import os

def data_match(data,equipoL, equipoV):
    toRet = []
    resultadosL = []
    cont = 0
    contR = 0
    data_invertido = data.iloc[::-1].reset_index(drop=True)  # Invertir el orden de las filas
    for i in range(len(data_invertido)):          
            if data_invertido['HomeTeam'][i] == equipoL and data_invertido['AwayTeam'][i] == equipoV and cont <= 10:
                cont += 1
                if data_invertido['FTR'][i] == 'H':
                    toRet.append(equipoL)
                elif data_invertido['FTR'][i] == 'D':
                    toRet.append(equipoV)
                else:
                    toRet.append('empate')            

    for i in range(len(data_invertido)):
        if contR < cont:            
            if data_invertido['HomeTeam'][i] == equipoL or data_invertido['AwayTeam'][i] == equipoL:
                print(data_invertido['HomeTeam'][i], data_invertido['AwayTeam'][i], data_invertido['Date'][i])
                contR += 1
                if data_invertido['HomeTeam'][i] == equipoL and data_invertido['FTR'][i] == 'H' or data_invertido['AwayTeam'][i] == equipoL and data_invertido['FTR'][i] == 'A':
                    resultadosL.append('Victoria')
                elif data_invertido['FTR'][i] == 'D':
                    resultadosL.append('Empate')
                else:
                    resultadosL.append('Derrota')
    new_data = pd.DataFrame({'enfrentamiento': toRet, 'resultados equipo local': resultadosL})
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