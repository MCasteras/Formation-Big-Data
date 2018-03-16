# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:13:11 2018

@author: Aziz Big data
"""

import pandas as pd
import numpy as np
import matplotlib #as plt
import matplotlib.pyplot as plt
import pylab as pl


#Ouverture du fichier CSV
df = pd.read_csv("SuperstoreSalesExcel.csv", sep=";", decimal=",");
#print(fichier)

#informations sur le dataframe
print(df.axes)
print (df.dtypes)

# description du dataframe = statistic sur les colonnes numériques
#print(df.describe())

#le nombre de produit
n_produits = df["Product Name"].value_counts()
n = len(n_produits); #nombre de produits
print(n)


#solution pour garder les trois colonnes
dfsales = df[['Product Sub-Category', 'Sales', 'Discount', 'Shipping Cost']] # j'isoles les colonnes qui m'interessent

#isolons les lignes "office Furnishings"
dff = dfsales.loc[dfsales['Product Sub-Category'] == "Office Furnishings"] #J'isoles toutes les lignes contenant "Office Furnishings"
print("Les colonnes Office Furnishings sont : \n" , dff)

# faire la moyennne de toutes les colonnes des ventes (Sales), de Products Sub-Categories
dsales_mean = dfsales.groupby('Product Sub-Category').mean().Sales
print("Les moyennes des sous produits sont : \n", dsales_mean)

dsales_mean2 = dfsales.groupby('Product Sub-Category').mean()

print(dsales_mean2)

#trier par date : on fait fd.dtypes pour avoir le type de donnée
df['Order Date'] = pd.to_datetime(df['Order Date'])
dfTseries = df.sort_values(by = ['Order Date'])
#(dfTseries["Order Date"])
#On peut également utiliser la méthode .iloc pour chercher des lignes ou des colonnes dans un df.

# Figures sur python

plt.plot(dsales_mean2)
plt.figure(1)
plt.title('Mean values of each Sub-Categories ')
plt.ylabel('Mean values')
plt.xlabel('Products Sub-Categories')
plt.show()



#Times series of order date
dfTseries_order_date = dfTseries["Order Date"];
dfTseries_Sales = dfTseries["Sales"];
#plt.title('Order Date Figure')
#plt.plot(dfTseries_order_date);

#Times series of order date en fonction de la Sales
# Méthode 1 = en idexant le "Oder Date"
dfTseries.index = dfTseries['Order Date'];
plt.figure(2)
ventes = dfTseries_Sales;
dfTseries["Sales"].plot()


#Times series of order date en fonction de la Sales
# Méthode 2 : En choisant les ventes et les dates dans 2 dataframe differentes
dates = dfTseries_order_date;
ventes = dfTseries_Sales;
plt.figure(3)
plt.plot(dates,ventes)
plt.title("Sales by Dates")
plt.ylabel("Sales")
plt.xlabel("Dates")