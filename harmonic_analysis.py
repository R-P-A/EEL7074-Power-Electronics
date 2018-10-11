# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------

# Saving Original Images based on CSV files of the Osciloscope
# Plotting Original CH1, CH2 and MATH and saving for reference

# General function for plotting originals ch1, ch2 and mth. Returns the dataframe created with all channels.
def plot_oscope_original(
        output_name = "",
        ch1_name = "",
        ch2_name = "",
        mth_name = "",
        ch1_2_scale = "",
        xlimits = "",
        orig_path_ch1 = "",
        orig_path_ch2 = "",
        orig_path_mth = "",
        output_path = ""
    ):
    channels = []
    plt.clf()
    # Plot CH1 if exists
    if orig_path_ch1 != "":
        ch1 = pd.read_csv(orig_path_ch1, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch1_name])
        plt.plot(ch1.index, ch1[ch1_name])
        channels.append(ch1)
    # Plot CH2 if exists
    if orig_path_ch2 != "":
        ch2_name_scale = ch2_name
        if ch1_2_scale != "":
            ch2_name_scale = (ch2_name + ' x ' + str(ch1_2_scale)).replace('.', ',')
        ch2 = pd.read_csv(orig_path_ch2, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch2_name_scale])
        plt.plot(ch2.index, ch2[ch2_name_scale]*ch1_2_scale)
        ch2 = ch2.rename(columns = {ch2_name_scale : ch2_name})
        channels.append(ch2)
    # Prepare MTH if exists
    if orig_path_mth != "":
        mth = pd.read_csv(orig_path_mth, usecols=[3,4], index_col=[0], header=None, names=['t (s)', mth_name])
        plt.plot(mth.index, mth[mth_name])
        channels.append(mth)
    # Correcting current for better scaling in image. Vscale/Iscale
    # Plotting and saving the image
    plt.xlabel('Tempo (s)')
    if (xlimits != "") and (len(xlimits) == 2):
        plt.xlim(xlimits[0], xlimits[1])
    plt.title(output_name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    # Making all the data a single data frame to return
    output = pd.concat(channels, axis=1)
    return output

# Function to calculate Fourier Transform
def calculate_fft(time, signal):
    fourier = np.fft.fft(signal)
    freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
    return [freq_fourier, fourier]

# Function to calculate Total Harmonic Distortion of a signal
def calculate_thd(fourier, freq0_interval, freq0_multiples = 20):   
    thd = 0
    for i in range(2, freq0_multiples):
        thd = thd + np.abs(fourier[i*freq0_interval])**2
    
    thd = np.sqrt(thd) / np.abs(fourier[1*freq0_interval])
    return thd

# Function to calculate and plot Original Function and Fourier Transform
def plot_fourier_transform(number_samples, time, values, y_name, title, out_path_name, xlimits = ""):
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
    plot[0].set_title(title)
    plot[0].set_xlabel('Tempo (s)')
    plot[0].set_ylabel(y_name)
    if len(xlimits) == 2:
        plot[0].set_xlim(xlimits[0], xlimits[1])
    plot[0].grid(True)
    plot[1].stem(fft[0], np.abs(fft[1]))
    plot[1].set_title('Transformada de Fourier')
    plot[1].set_xlabel('Frequência (Hz)')
    plot[1].set_ylabel(y_name)
    plot[1].set_xlim(0,800)
    plot[1].grid(True)
    plt.tight_layout()
    plt.savefig(out_path_name)
    return fft