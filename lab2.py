# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------

# Saving Original Images based on CSV files of the Osciloscope

# Plotting Original CH1, CH2 and MATH and saving for reference
# Full Wave Rectfier with R Load
ch1_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
ch2_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin x 83.33 (A)'])
mth_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
out_fwrr = pd.concat([ch1_fwrr,ch2_fwrr,mth_fwrr], axis=1)
out_fwrr['Iin x 83.33 (A)'] = out_fwrr['Iin x 83.33 (A)']*83.33
out_fwrr.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load.pdf')

# Full Wave Rectfier with RL Load
ch1_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
ch2_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin x 83.33 (A)'])
mth_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
out_fwrrl = pd.concat([ch1_fwrrl, ch2_fwrrl, mth_fwrrl], axis=1)
out_fwrrl['Iin x 83.33 (A)'] = out_fwrrl['Iin x 83.33 (A)']*83.33
out_fwrrl.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_rl_load.pdf')
    
# Plotting Original FFT and saving for reference
# Full Wave Rectfier with R Load
fft_fwrr = pd.read_csv('src_img/lab2/ALL0016/F0016FFT.CSV', usecols=[3,4], index_col=[0], header=None, names=['f (Hz)', 'Módulo (dB)'])
fft_fwrr.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load_fourier.pdf')

# Full Wave Rectfier with RL Load
fft_fwrrl = pd.read_csv('src_img/lab2/ALL0019/F0019FFT.CSV', usecols=[3,4], index_col=[0], header=None, names=['f (Hz)', 'Módulo (dB)'])
fft_fwrrl.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load_fourier.pdf')
plt.savefig('img/lab2/orig_full_wave_rectfier_rl_load_fourier.pdf')

# -------------------------------------------------------------------------------------------------

# Calculating the Frequency Spectrum of the Voltage Input
time = out_fwrr.index.values
signal = out_fwrr['Vin (V)'].values

fourier = np.fft.fft(signal, norm="ortho")
freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
inv_fourier = np.fft.ifft(fourier, norm="ortho")

figure, plot = plt.subplots(3,1)
plot[0].plot(time, signal)
plot[0].set_title('Sinal Original Vin')
plot[1].stem(freq_fourier, np.abs(fourier))
plot[1].set_title('Transformada Fourier')
plot[1].set_xlim(-1000,1000)
plot[2].plot(time, inv_fourier)
plot[2].set_title('Transformada Inversa')
plt.tight_layout()
plt.savefig('img/lab2/vin_r_fourier.pdf')