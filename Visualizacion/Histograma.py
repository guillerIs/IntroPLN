import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns
df = pd. read_csv ( "https://coded2.herokuapp.com/datavizpandas/meals2.csv")
df['columna']. hist ( bins =100)
plt . show ()