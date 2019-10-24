import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib . pylab as plt

fmri = sns. load_dataset ("fmri")
ax = sns. lineplot (x="timepoint", y="signal", data = fmri )
plt . show ()