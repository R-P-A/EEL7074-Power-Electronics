# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plotting CH1, CH2 and MATH
for i in [12,13,14,17,18]:
    print("\n---------------- File: " + str(i) + " ----------------")
    ch1 = pd.read_csv('src_img/lab2/ALL00'+str(i)+'/F00'+str(i)+'CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
    ch2 = pd.read_csv('src_img/lab2/ALL00'+str(i)+'/F00'+str(i)+'CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin x 83.33 (A)'])
    mth = pd.read_csv('src_img/lab2/ALL00'+str(i)+'/F00'+str(i)+'MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
    out = pd.concat([ch1,ch2,mth], axis=1)
    out['Iin x 83.33 (A)'] = out['Iin x 83.33 (A)']*83.33
    print(out.head())
    print(out.tail())
    out.plot()
    plt.savefig('img/lab2/plot' + str(i) + '.pdf')

# Plotting FFT
for i in [15,16,19,20]:
    print("\n---------------- File: " + str(i) + " ----------------")
    fft = pd.read_csv('src_img/lab2/ALL00'+str(i)+'/F00'+str(i)+'FFT.CSV', usecols=[3,4], index_col=[0], header=None, names=['f (Hz)', 'Módulo (dB)'])
    print(fft.head())
    print(fft.tail())
    fft.plot()
    plt.savefig('img/lab2/plot' + str(i) + '.pdf')