import numpy as np
import pandas as pd
import scipy.stats
import xlrd
import csv
import os

#Algoritma tutarsa tamamına uygulanacak
#for root, directories, files in os.walk('C:/Users/erenb/Desktop/Pro/Old Datas'):
#    for filename in files:

df = pd.read_excel('C:/Users/erenb/Desktop/NewxercesV1.xlsx' , engine='openpyxl')

#25 farklı attribute var / len = 25
#588 farklı row var
#print()

df_nmp = df.to_numpy()



#print(df_nmp[1][21])
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
a10 = []
a11 = []
a12 = []
a13 = []
a14 = []
a15 = []
a16 = []
a17 = []
a18 = []
a19 = []
a20 = []
a21 = []
a22 = []
a23 = []
a24 = []
a25 = []

for i in range(len(df_nmp)):
    a1.append(df_nmp[i][0])
    a2.append(df_nmp[i][1])
    a3.append(df_nmp[i][2])
    a4.append(df_nmp[i][3])
    a5.append(df_nmp[i][4])
    a6.append(df_nmp[i][5])
    a7.append(df_nmp[i][6])
    a8.append(df_nmp[i][7])
    a9.append(df_nmp[i][8])
    a10.append(df_nmp[i][9])
    a11.append(df_nmp[i][10])
    a12.append(df_nmp[i][11])
    a13.append(df_nmp[i][12])
    a14.append(df_nmp[i][13])
    a15.append(df_nmp[i][14])
    a16.append(df_nmp[i][15])
    a17.append(df_nmp[i][16])
    a18.append(df_nmp[i][17])
    a19.append(df_nmp[i][18])
    a20.append(df_nmp[i][19])
    a21.append(df_nmp[i][20])
    a22.append(df_nmp[i][21])
    a23.append(df_nmp[i][22])
    a24.append(df_nmp[i][23])
    a25.append(df_nmp[i][24])

#print(a15)
a_total = []
a_total.append(a1)
a_total.append(a2)
a_total.append(a3)
a_total.append(a4)
a_total.append(a5)
a_total.append(a6)
a_total.append(a7)
a_total.append(a9)
a_total.append(a10)
a_total.append(a11)
a_total.append(a12)
a_total.append(a13)
a_total.append(a14)
a_total.append(a15)
a_total.append(a16)
a_total.append(a17)
a_total.append(a18)
a_total.append(a19)
a_total.append(a20)
a_total.append(a21)
a_total.append(a22)
a_total.append(a23)
a_total.append(a24)
a_total.append(a25)


#print(a_total)

print(scipy.stats.pearsonr(a1, a25))
#print(scipy.stats.pearsonr(a2, a15))
#print(scipy.stats.pearsonr(a3, a15))
#print(scipy.stats.pearsonr(a4, a15))
print(scipy.stats.pearsonr(a5, a25))
print(scipy.stats.pearsonr(a6, a25))
print(scipy.stats.pearsonr(a7, a25))
print(scipy.stats.pearsonr(a8, a25))
print(scipy.stats.pearsonr(a9, a25))
print(scipy.stats.pearsonr(a10, a25))
print(scipy.stats.pearsonr(a11, a25))
print(scipy.stats.pearsonr(a12, a25))
print(scipy.stats.pearsonr(a13, a25))
print(scipy.stats.pearsonr(a14, a25))
print(scipy.stats.pearsonr(a15, a25))
print(scipy.stats.pearsonr(a16, a25))
print(scipy.stats.pearsonr(a17, a25))
print(scipy.stats.pearsonr(a18, a25))
print(scipy.stats.pearsonr(a19, a25))
print(scipy.stats.pearsonr(a20, a25))
print(scipy.stats.pearsonr(a21, a25))
print(scipy.stats.pearsonr(a22, a25))
print(scipy.stats.pearsonr(a23, a25))
print(scipy.stats.pearsonr(a24, a25))
print(scipy.stats.pearsonr(a25, a25))

np.corrcoef(a24,a25,a23,a12,a15)


for i in range(25):
   for j in range(25):
    print("i = " + str(i) + np.correlate(a_total[i], a_total[j]))
    break
    
print(df.unique())


#for i in range(len(df_nmp[0])):


