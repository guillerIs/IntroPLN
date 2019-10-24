import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns
import requests

# descargar datos para el análisis
#url = 'https://tutorials.technology/data/world-population.csv'
#response = requests.get(url)
#with open('world-population.csv', 'wb') as csv_file:
    #csv_file.write(response.content)

# usar pandas read_csv para cargar datos
#poblacion = pd.read_csv('world-population.csv', index_col=0)
dataframe = pd.read_csv("https://coded2.herokuapp.com/datavizpandas/meals2.csv", index_col = 0)
#df = pd.read_csv (data_path)
#x = dataframe.Height
#y = dataframe.Latitude
#plt.scatter(x, y)
#plt.show()  # or plt.savefig("name.png")

#graficar los datos usando PANDAS
#poblacion.plot.pie()
dataframe.plot.pie(subplots=True)
plt.show()