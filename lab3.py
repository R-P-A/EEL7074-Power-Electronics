# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------

# Saving Original Images based on CSV files of the Osciloscope
# Plotting Original CH1, CH2 and MATH and saving for reference

# General function for plotting originals. Returns the dataframe created with all channels.
def plot_original_ch1_ch2(orig_path_ch1, orig_path_ch2, ch1_2_scale, ch1_name, ch2_name, out_path_name):
    # Importing data from source CSVs
    ch1 = pd.read_csv(orig_path_ch1, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch1_name])
    ch2 = pd.read_csv(orig_path_ch2, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch2_name])
    # Correcting current for better scaling in image. Vscale/Iscale
    out = pd.concat([ch1, ch2*ch1_2_scale], axis=1)
    # Plotting and saving the image
    plt.plot(out.index, out[ch1_name])
    plt.plot(out.index, out[ch2_name])
    plt.xlabel('Tempo (s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_path_name)
    plt.clf()
    return out


# Full Wave Rectfier with RL Load
out_fwrrl_2_5ms = plot_original_ch1_ch2(
    "src_img/lab3/ALL0022/F0022CH1.CSV",
    "src_img/lab3/ALL0022/F0022CH2.CSV",
    100,
    'Vin (V)',
    'Iin (A) x 100',
    'img/lab3/orig_rl_2,5ms.png'
)

# Full Wave Rectfier with RL Load
out_fwrrl_5ms = plot_original_ch1_ch2(
    "src_img/lab3/ALL0023/F0023CH1.CSV",
    "src_img/lab3/ALL0023/F0023CH2.CSV",
    100,
    'Vin (V)',
    'Iin (A) x 100',
    'img/lab3/orig_rl_5ms.png'
)

# -------------------------------------------------------------------------------------------------

# Calculating and Plotting Fourier Transforms

# Function to calculate Fourier Transform
def calculate_fft(time, signal):
    fourier = np.fft.fft(signal)
    freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
    return [freq_fourier, fourier]

# Function to plot Original Function and Fourier Transform
def plot_fourier_transform(number_samples, time, values, y_name, out_path_name):
    # Getting the correct sample amount
    time = time[0:number_samples]
    values = values[0:number_samples]
    # Calculating fft
    fft = calculate_fft(time, values)
    # Correcting fft for energy
    fft[1] = fft[1] / number_samples
    # Plotting fft with original
    figure, plot = plt.subplots(2,1)
    plot[0].plot(time, values)
    plot[0].set_title('Sinal Original Vin')
    plot[0].set_xlabel('Tempo (s)')
    plot[0].set_ylabel(y_name)
    plot[0].grid(True)
    plot[1].stem(fft[0], np.abs(fft[1]))
    plot[1].set_title('Transformada Fourier')
    plot[1].set_xlabel('Frequência (Hz)')
    plot[1].set_ylabel(y_name)
    plot[1].set_xlim(-1000,1000)
    plot[1].grid(True)
    plt.tight_layout()
    plt.savefig(out_path_name)
    return fft

fft_vin_rl_2_5ms = plot_fourier_transform(
    2500,
    out_fwrrl_2_5ms.index.values,
    out_fwrrl_2_5ms['Vin (V)'].values,
    "Tensão (V)",
    "img/lab3/vin_rl_2_5ms_2500_samples_fourier.png"
)

fft_vin_rl_2_5ms = plot_fourier_transform(
    1667,
    out_fwrrl_2_5ms.index.values,
    out_fwrrl_2_5ms['Vin (V)'].values,
    "Tensão (V)",
    "img/lab3/vin_rl_2_5ms_1667_samples_fourier.png"
)

fft_vin_rl_5ms = plot_fourier_transform(
    2500,
    out_fwrrl_5ms.index.values,
    out_fwrrl_5ms['Vin (V)'].values,
    "Tensão (V)",
    "img/lab3/vin_rl_5ms_fourier.png"
)