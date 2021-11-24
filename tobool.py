import pandas as pd
import xlrd
import os

for root, directories, files in os.walk('C:/Users/erenb/Desktop/Pro/NewDatas/'):
    for filename in files:
        df = pd.read_excel('C:/Users/erenb/Desktop/Pro/NewDatas/' + filename, engine='openpyxl')
        df['bug'] = df['bug'].astype('bool')
        print(df)
    
