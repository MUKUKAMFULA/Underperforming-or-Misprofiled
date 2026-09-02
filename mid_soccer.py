# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:39:03 2026

@author: Mukuka Noward Mfula
"""
import pandas as pd
import matplotlib.pyplot as plt
def plot(x, y, z, xlabel, ylabel,title):
    # Clean x and y if they contain percentage strings
    if x.dtype == 'object':
        x = x.astype(str).str.replace("%", "", regex=False).astype(float)
    if y.dtype == 'object':
        y = y.astype(str).str.replace("%", "", regex=False).astype(float)
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y)
    for i, name in enumerate(z):
        plt.annotate(name, 
                     (x.iloc[i], y.iloc[i]),
                     xytext=(5, 5), textcoords='offset points', fontsize=8)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


#%%
df_midfielders = pd.read_csv("Midfielders.csv")

plot(df_midfielders["MINUTES PLAYED"],df_midfielders["BIG CHANCES CREATED"],
     df_midfielders["PLAYER"],"minutes played","Big Chances Created","Minutes played vs Big Chances Created")
plot(df_midfielders["MINUTES PLAYED"],
     df_midfielders["SUCCESSFUL PASSES"],df_midfielders["PLAYER"],
     "minutes played","SUCCESSFUL PASSES","Minutes played vs Successful Passes")
plot(df_midfielders["MINUTES PLAYED"],
     df_midfielders["CHANCES CREATED"],df_midfielders["PLAYER"],
     "minutes played","CHANCES CREATED","Minutes played vs Chances Created")
#%%
df_24_25 = pd.read_csv("2425.csv")
plot(df_24_25["GOALS "], df_24_25["ASSISTS"],df_24_25["PLAYER"],"GOALS","ASSISTS", "Goals vs Assists 24/25")
plt.figure(figsize=(20,20))
plt.bar(df_24_25["PLAYER"],df_24_25["G/A per game"])
plt.ylabel("G/A per game")
plt.title("G/A per game 24/25", fontsize = 40 )
plt.show()

#%%
df_25_26 = pd.read_csv("2526.csv")
plot(df_25_26["GOALS "], df_25_26["ASSISTS"],df_25_26["PLAYER"],"GOALS","ASSISTS", "Goals vs Assists 25/26")
plt.figure(figsize=(20,20))
plt.bar(df_25_26["PLAYER"],df_25_26["G/A per game"])
plt.ylabel("G/A per game")
plt.title("G/A per game 25/26",fontsize = 40)
plt.show()
plot(df_25_26["GOALS "], df_25_26["ASSISTS"],df_25_26["PLAYER"],"GOALS","ASSISTS", "Goals vs Assists 25/26")
