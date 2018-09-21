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
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('img/lab2/orig_full_wave_rectfier_r_load.pdf')

# Full Wave Rectfier with RL Load
ch1_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH1.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Vin (V)'])
ch2_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018CH2.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'Iin (A)'])
mth_fwrrl = pd.read_csv('src_img/lab2/ALL0018/F0018MTH.CSV', usecols=[3,4], index_col=[0], header=None, names=['t (s)', 'P (W)'])
out_fwrrl = pd.concat([ch1_fwrrl, ch2_fwrrl, mth_fwrrl], axis=1)
out_fwrrl['Iin (A)'] = out_fwrrl['Iin (A)']*83.33
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

def calculate_fourier(time, signal):
    fourier = np.fft.fft(signal)
    freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
    return [freq_fourier, fourier]

def calculate_thd(freq_fourier, fourier):
    # Calculating Harmonics in multiple of 60 Hz
    fourier_harmonics = []
    counter = 0
    for i in range(9):
        if i % 2 == 0:
            if (i == 0):
                interpol = np.polyfit(freq_fourier[counter+1:counter+4], np.abs(fourier[counter+1:counter+4]), 2)
                fourier_harmonic = interpol[0]*((60*(i+1))**2) + interpol[1]*(60*(i+1)) + interpol[2]
                fourier_harmonics.append(fourier_harmonic)
                print(np.abs(fourier[counter+1:counter+4]))
                print(fourier_harmonics[i])
            else:
                interpol = np.polyfit(freq_fourier[counter+1:counter+3], np.abs(fourier[counter+1:counter+3]), 1)
                fourier_harmonic = interpol[0]*(60*(i+1)) + interpol[1]
                print(np.abs(fourier[counter+1:counter+3]))
                print(fourier_harmonic)
                fourier_harmonics.append(fourier_harmonic)
        else:
            counter = counter + 3
            fourier_harmonics.append(np.abs(fourier[counter]))
    
    # Calculando THD
    thd = 0
    for i in range(1,9):
        thd = thd + (fourier_harmonics[i])**2
    thd = np.sqrt(thd) / fourier_harmonics[0]
    return thd

time_index_period = 1667
# Calculating the Frequency Spectrum of the Voltage Input for R
time = ch1_fwrr.index.values
time = time[0:time_index_period]
vin_r = ch1_fwrr['Vin (V)'].values
vin_r = vin_r[0:time_index_period]
fft_vin_r = calculate_fourier(time, vin_r)
fft_vin_r[1] = fft_vin_r[1] / time_index_period
thd = calculate_thd(fft_vin_r[0], fft_vin_r[1])
print("THD: {}".format(thd))

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
plt.savefig('img/lab2/vin_r_fourier.pdf')

# Calculating the Frequency Spectrum of the Current Input for R load
time = ch2_fwrr.index.values
time = time[0:time_index_period]
iin_r = ch2_fwrr['Iin (A)'].values
iin_r = iin_r[0:time_index_period]
fft_iin_r = calculate_fourier(time, iin_r)
fft_iin_r[1] = fft_iin_r[1] / time_index_period
thd = calculate_thd(fft_iin_r[0], fft_iin_r[1])
print("THD: {}".format(thd))

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
plt.savefig('img/lab2/iin_r_fourier.pdf')

# Calculating the Frequency Spectrum of the Voltage Input for RL
time = ch1_fwrrl.index.values
time = time[0:time_index_period]
vin_rl = ch1_fwrrl['Vin (V)'].values
vin_rl = vin_rl[0:time_index_period]
fft_vin_rl = calculate_fourier(time, vin_rl)
fft_vin_rl[1] = fft_vin_rl[1]/time_index_period
thd = calculate_thd(fft_vin_rl[0], fft_vin_rl[1])
print("THD: {}".format(thd))

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
plt.savefig('img/lab2/vin_rl_fourier.pdf')

# Calculating the Frequency Spectrum of the Current Input for RL load
time = ch2_fwrrl.index.values
time = time[0:time_index_period]
iin_rl = ch2_fwrrl['Iin (A)'].values
iin_rl = iin_rl[0:time_index_period]
fft_iin_rl = calculate_fourier(time, iin_rl)
fft_iin_rl[1] = fft_iin_rl[1]/time_index_period
thd = calculate_thd(fft_iin_rl[0], fft_iin_rl[1])
print("THD: {}".format(thd))

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
plt.savefig('img/lab2/iin_rl_fourier.pdf')