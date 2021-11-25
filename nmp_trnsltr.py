import pandas as pd
import xlrd
import os
import numpay as np

os.chdir("C:/Users/erenb/Desktop/Pro/NewDatas/wBool")

df_nmp = []

for root, directories, files in os.walk('C:/Users/erenb/Desktop/Pro/NewDatas/'):
    for filename in files:
        df = pd.read_excel('C:/Users/erenb/Desktop/Pro/NewDatas/' + filename, engine='openpyxl')
        df['bug'] = df['bug'].astype('bool')
        df.to_excel("New_" + filename)
        df_nmp.append(np.array(df))
        
        
for i in range(len(df_nmp)):
    
     ###to be continued
