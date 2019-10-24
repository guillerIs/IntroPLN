import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib . pylab as plt
titanic = sns . load_dataset ("titanic")
ax = sns. countplot (x="class", hue="who", data = titanic )
plt . show ()