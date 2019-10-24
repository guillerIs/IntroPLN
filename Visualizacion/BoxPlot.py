import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib . pylab as plt
tips = sns. load_dataset ("tips")
ax = sns. catplot (x="day", y="total_bill", kind ="box", data = tips )
plt . show ()