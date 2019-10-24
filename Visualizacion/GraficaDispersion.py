import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns

random_data = pd. DataFrame (np. random . rand (100 , 3))
ax = sns. scatterplot (x=0, y=1, hue =2, data = random_data )
plt . show ()