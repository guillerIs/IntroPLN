import numpy as np
import seaborn as sns
import matplotlib . pylab as plt
random_data = np. random . rand (30 , 30)
ax = sns. heatmap ( random_data , linewidth =0.5)
plt . show ()