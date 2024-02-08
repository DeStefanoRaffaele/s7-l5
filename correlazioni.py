import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./dataset_climatico.csv", parse_dates=["data_osservazione"])
df.dropna(inplace=True)

# colonne da standardizzare
columns_to_standardize = ["temperatura_media", "precipitazioni", "umidita", "velocita_vento"]

# Calcola la matrice di correlazione
correlation_matrix = df[columns_to_standardize].corr()

# Crea una heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", linewidths=.5)
plt.title("Matrice di Correlazione tra Variabili Meteorologiche")
plt.show()