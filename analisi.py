import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./dataset_climatico.csv", parse_dates=["data_osservazione"])
df.dropna(inplace=True)

# colonne da standardizzare
columns_to_standardize = ["temperatura_media", "precipitazioni", "umidita", "velocita_vento"]
# applicare la formula Z-score
df_zscore = ((df[columns_to_standardize] - df[columns_to_standardize].mean()) / df[columns_to_standardize].std())

# calcolo media
df_mean = df[columns_to_standardize].mean()
# calcolo mediana
df_median = df[columns_to_standardize].median()
# calcolo deviazione standard
df_dev = df[columns_to_standardize].std()

# Imposta l'indice su data_osservazione
df.set_index("data_osservazione", inplace=True)

# traccia l'andamento mensile per la media precipitazioni 
df.resample("M")["precipitazioni"].mean().plot(kind="line")
plt.title("Andamento mensile delle Precipitazioni Media")
plt.xlabel("Data")
plt.ylabel("Precipitazioni Media")
plt.show()

# visualizza media velocita vento raggruppato per stazione
df.groupby("stazione_meteorologica")["velocita_vento"].mean().plot(kind="bar")
plt.title("Velocita vento per stazione")
plt.xlabel("Stazione")
plt.ylabel("Media Velocita vento")
plt.show()

