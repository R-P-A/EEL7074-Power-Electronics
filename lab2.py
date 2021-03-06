# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------

# Saving Original Images based on CSV files of the Osciloscope

# Plotting Original CH1, CH2 and MATH and saving for reference
# Full Wave Rectfier with R Load
ch1_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
ch2_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin (A)'])
mth_fwrr = pd.read_csv('src_img/lab2/ALL0014/F0014MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
out_fwrr = pd.concat([ch1_fwrr,ch2_fwrr*83.33,mth_fwrr], axis=1)
out_fwrr = out_fwrr.rename(columns = {'Iin (A)' : 'Iin (A) x 83,33'})
plt.plot(out_fwrr.index, out_fwrr['Vin (V)'])
plt.plot(out_fwrr.index, out_fwrr['Iin (A) x 83,33'])
plt.plot(out_fwrr.index, out_fwrr['P (W)'])
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load.png')
plt.clf()

# Full Wave Rectfier with RL Load
ch1_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
ch2_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin (A)'])
mth_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
out_fwrrl = pd.concat([ch1_fwrrl, ch2_fwrrl*83.33, mth_fwrrl], axis=1)
out_fwrrl = out_fwrrl.rename(columns = {'Iin (A)' : 'Iin (A) x 83,33'})
plt.plot(out_fwrrl.index, out_fwrrl['Vin (V)'])
plt.plot(out_fwrrl.index, out_fwrrl['Iin (A) x 83,33'])
plt.plot(out_fwrrl.index, out_fwrrl['P (W)'])
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_rl_load.png')
plt.clf()
    
# Plotting Original FFT and saving for reference
# Full Wave Rectfier with R Load
fft_fwrr = pd.read_csv('src_img/lab2/ALL0016/F0016FFT.CSV', usecols=[3,4], index_col=[0], header=None, names=['f (Hz)', 'Módulo (dB)'])
fft_fwrr.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load_fourier.png')

# Full Wave Rectfier with RL Load
fft_fwrrl = pd.read_csv('src_img/lab2/ALL0019/F0019FFT.CSV', usecols=[3,4], index_col=[0], header=None, names=['f (Hz)', 'Módulo (dB)'])
fft_fwrrl.plot()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load_fourier.png')
plt.savefig('img/lab2/orig_full_wave_rectfier_rl_load_fourier.png')

# -------------------------------------------------------------------------------------------------

def calculate_fourier(time, signal):
    fourier = np.fft.fft(signal)
    freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
    return [freq_fourier, fourier]

def calculate_thd(fourier, precision):    
    # Calculando THD
    thd = 0
    for i in range(2,precision):
        thd = thd + np.abs(fourier[i])**2
    
    thd = np.sqrt(thd) / np.abs(fourier[1])
    return thd

number_samples = 1667
# Calculating the Frequency Spectrum of the Voltage Input for R
time = ch1_fwrr.index.values
time = time[0:number_samples]
vin_r = ch1_fwrr['Vin (V)'].values
vin_r = vin_r[0:number_samples]
fft_vin_r = calculate_fourier(time, vin_r)
fft_vin_r[1] = fft_vin_r[1] / number_samples
thd = calculate_thd(fft_vin_r[1], 50)
print("THD Vin R: {}".format(thd))

figure, plot = plt.subplots(2,1)
plot[0].plot(time, vin_r)
plot[0].set_title('Sinal Original Vin')
plot[0].set_xlabel('Tempo (s)')
plot[0].set_ylabel('Tensão (V)')
plot[0].grid(True)
plot[1].stem(fft_vin_r[0], np.abs(fft_vin_r[1]))
plot[1].set_title('Transformada Fourier')
plot[1].set_xlabel('Frequência (Hz)')
plot[1].set_ylabel('Tensão (V)')
plot[1].set_xlim(-1000,1000)
plot[1].grid(True)
plt.tight_layout()
plt.savefig('img/lab2/vin_r_fourier.png')

# Calculating the Frequency Spectrum of the Current Input for R load
time = ch2_fwrr.index.values
time = time[0:number_samples]
iin_r = ch2_fwrr['Iin (A)'].values
iin_r = iin_r[0:number_samples]
fft_iin_r = calculate_fourier(time, iin_r)
fft_iin_r[1] = fft_iin_r[1] / number_samples
thd = calculate_thd(fft_iin_r[1], 50)
print("THD Iin R: {}".format(thd))
fp = 1 / np.sqrt(1 + thd**2)
print("FP R: {}".format(fp))

figure, plot = plt.subplots(2,1)
plot[0].plot(time, iin_r)
plot[0].set_title('Sinal Original Iin')
plot[0].set_xlabel('Tempo (s)')
plot[0].set_ylabel('Corrente (A)')
plot[0].grid(True)
plot[1].stem(fft_iin_r[0], np.abs(fft_iin_r[1]))
plot[1].set_title('Transformada Fourier')
plot[1].set_xlabel('Frequência (Hz)')
plot[1].set_ylabel('Corrente (A)')
plot[1].set_xlim(-1000,1000)
plot[1].grid(True)
plt.tight_layout()
plt.savefig('img/lab2/iin_r_fourier.png')

# Calculating the Frequency Spectrum of the Voltage Input for RL
time = ch1_fwrrl.index.values
time = time[0:number_samples]
vin_rl = ch1_fwrrl['Vin (V)'].values
vin_rl = vin_rl[0:number_samples]
fft_vin_rl = calculate_fourier(time, vin_rl)
fft_vin_rl[1] = fft_vin_rl[1]/number_samples
thd = calculate_thd(fft_vin_rl[1], 50)
print("THD Vin RL: {}".format(thd))

figure, plot = plt.subplots(2,1)
plot[0].plot(time, vin_rl)
plot[0].set_title('Sinal Original Vin')
plot[0].set_xlabel('Tempo (s)')
plot[0].set_ylabel('Tensão (V)')
plot[0].grid(True)
plot[1].stem(fft_vin_rl[0], np.abs(fft_vin_rl[1]))
plot[1].set_title('Transformada Fourier')
plot[1].set_xlabel('Frequência (Hz)')
plot[1].set_ylabel('Tensão (V)')
plot[1].set_xlim(-1000,1000)
plot[1].grid(True)
plt.tight_layout()
plt.savefig('img/lab2/vin_rl_fourier.png')

# Calculating the Frequency Spectrum of the Current Input for RL load
time = ch2_fwrrl.index.values
time = time[0:number_samples]
iin_rl = ch2_fwrrl['Iin (A)'].values
iin_rl = iin_rl[0:number_samples]
fft_iin_rl = calculate_fourier(time, iin_rl)
fft_iin_rl[1] = fft_iin_rl[1]/number_samples
thd = calculate_thd(fft_iin_rl[1], 50)
print("THD Iin RL: {}".format(thd))
fp = 1 / np.sqrt(1 + thd**2)
print("FP RL: {}".format(fp))

figure, plot = plt.subplots(2,1)
plot[0].plot(time, iin_rl)
plot[0].set_title('Sinal Original Iin')
plot[0].set_xlabel('Tempo (s)')
plot[0].set_ylabel('Corrente (A)')
plot[0].grid(True)
plot[1].stem(fft_iin_rl[0], np.abs(fft_iin_rl[1]))
plot[1].set_title('Transformada Fourier')
plot[1].set_xlabel('Frequência (Hz)')
plot[1].set_ylabel('Corrente (A)')
plot[1].set_xlim(-1000,1000)
plot[1].grid(True)
plt.tight_layout()
plt.savefig('img/lab2/iin_rl_fourier.png')