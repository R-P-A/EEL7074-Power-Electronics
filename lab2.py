# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ch1 = pd.read_csv('Imagens/ALL0012/F0012CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t', 'Vin (V)'])
ch2 = pd.read_csv('Imagens/ALL0012/F0012CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t', 'Iin (A*83.33)'])
mth = pd.read_csv('Imagens/ALL0012/F0012MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t', 'P (W)'])
out = pd.concat([ch1,ch2,mth], axis=1)
out['Iin (A*83.33)'] = out['Iin (A*83.33)']*83.33
print(out.head())
print(out.tail())

out.plot()
plt.show()