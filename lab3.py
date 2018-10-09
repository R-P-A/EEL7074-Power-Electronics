# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------

# Saving Original Images based on CSV files of the Osciloscope
# Plotting Original CH1, CH2 and MATH and saving for reference

# General function for plotting originals ch1 and ch2. Returns the dataframe created with all channels.
def plot_original_ch1_ch2(output_name, ch1_name, ch2_name, ch1_2_scale, orig_path_ch1, orig_path_ch2, output_path):
    # Importing data from source CSVs
    ch2_name_scale = (ch2_name + ' x ' + str(ch1_2_scale)).replace('.', ',')
    ch1 = pd.read_csv(orig_path_ch1, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch1_name])
    ch2 = pd.read_csv(orig_path_ch2, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch2_name_scale])
    # Correcting current for better scaling in image. Vscale/Iscale
    output = pd.concat([ch1, ch2*ch1_2_scale], axis=1)
    # Plotting and saving the image
    plt.plot(output.index, output[ch1_name])
    plt.plot(output.index, output[ch2_name_scale])
    plt.xlabel('Tempo (s)')
    plt.xlim(-0.012, 0.012)
    plt.title(output_name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.clf()
    # Correcting scale of ch2 for future uses
    output[ch2_name_scale] = output[ch2_name_scale]/83.33
    output = output.rename(columns = {ch2_name_scale : ch2_name})
    return output

# General function for plotting originals ch1, ch2 and mth. Returns the dataframe created with all channels.
def plot_original_ch1_ch2_mth(output_name, ch1_name, ch2_name, mth_name, ch1_2_scale, orig_path_ch1, orig_path_ch2, orig_path_mth, output_path):
    # Importing data from source CSVs
    ch2_name_scale = (ch2_name + ' x ' + str(ch1_2_scale)).replace('.', ',')
    ch1 = pd.read_csv(orig_path_ch1, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch1_name])
    ch2 = pd.read_csv(orig_path_ch2, usecols=[3,4], index_col=[0], header=None, names=['t (s)', ch2_name_scale])
    mth = pd.read_csv(orig_path_mth, usecols=[3,4], index_col=[0], header=None, names=['t (s)', mth_name])
    # Correcting current for better scaling in image. Vscale/Iscale
    output = pd.concat([ch1, ch2*ch1_2_scale, mth], axis=1)
    # Plotting and saving the image
    plt.plot(output.index, output[ch1_name])
    plt.plot(output.index, output[ch2_name_scale])
    plt.plot(output.index, output[mth_name])
    plt.xlabel('Tempo (s)')
    plt.xlim(-0.012, 0.012)
    plt.title(output_name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.clf()
    # Correcting scale of ch2 for future uses
    output[ch2_name_scale] = output[ch2_name_scale]/83.33
    output = output.rename(columns = {ch2_name_scale : ch2_name})
    return output

# Full Wave Rectfier Input with R Load
fwrr_in = plot_original_ch1_ch2_mth (
    'Retificador de Onda Completa Carga R - Entrada',
    'Vin (V)',
    'Iin (A)',
    'P (W)',
    83.33,
    'src_img/lab2/ALL0014/F0014CH1.CSV',
    'src_img/lab2/ALL0014/F0014CH2.CSV',
    'src_img/lab2/ALL0014/F0014MTH.CSV',
    'img/lab3/orig_in_r.png'
)

# Full Wave Rectfier Input with RL Load
fwrrl_in = plot_original_ch1_ch2_mth (
    'Retificador de Onda Completa Carga RL - Entrada',
    'Vin (V)',
    'Iin (A)',
    'P (W)',
    83.33,
    'src_img/lab2/ALL0018/F0018CH1.CSV',
    'src_img/lab2/ALL0018/F0018CH2.CSV',
    'src_img/lab2/ALL0018/F0018MTH.CSV',
    'img/lab3/orig_in_rl.png'
)

# Full Wave Rectfier Input with RC Load
fwrrc_in = plot_original_ch1_ch2_mth(
    'Retificador de Onda Completa Carga RC - Entrada',
    'Vin (V)',
    'Iin (A)',
    'P (W)',
    100,
    "src_img/lab3/ALL0028/F0028CH1.CSV",
    "src_img/lab3/ALL0028/F0028CH2.CSV",
    "src_img/lab3/ALL0028/F0028MTH.CSV",
    'img/lab3/orig_in_rc.png'
)

# Full Wave Rectfier Output with RC Load
fwrrc_out = plot_original_ch1_ch2(
    'Retificador de Onda Completa Carga RC - Saída',
    'Vin (V)',
    'Iin (A)',
    100,
    "src_img/lab3/ALL0023/F0023CH1.CSV",
    "src_img/lab3/ALL0023/F0023CH2.CSV",
    'img/lab3/orig_out_rc.png'
)

# -------------------------------------------------------------------------------------------------

# Calculating THD and Plotting Fourier Transforms


# Function to calculate Fourier Transform
def calculate_fft(time, signal):
    fourier = np.fft.fft(signal)
    freq_fourier = np.fft.fftfreq(signal.size, (time[1]-time[0]))
    return [freq_fourier, fourier]

def calculate_thd(fourier, samples_per_ff, precision):    
    # Calculando THD
    thd = 0
    for i in range(2, precision):
        thd = thd + np.abs(fourier[i*samples_per_ff])**2
    
    thd = np.sqrt(thd) / np.abs(fourier[1*samples_per_ff])
    return thd

# Function to plot Original Function and Fourier Transform
def plot_fourier_transform(number_samples, time, values, y_name, title, out_path_name):
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
    if number_samples == 2500:
        plot[0].set_xlim(-0.012,0.012)
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

# Full Wave Rectfier Voltage Input Fourier Transform with R Load
fft_vin_r = plot_fourier_transform(
    1667,
    fwrr_in.index.values,
    fwrr_in['Vin (V)'].values,
    "Tensão (V)",
    "Tensão de Entrada do Retificador de Onda Completa Carga R",
    "img/lab3/vin_r_fourier.png"
)

# Full Wave Rectfier Current Input Fourier Transform with R Load
fft_iin_r = plot_fourier_transform(
    1667,
    fwrr_in.index.values,
    fwrr_in['Iin (A)'].values,
    "Corrente (A)",
    "Corrente de Entrada do Retificador de Onda Completa Carga R",
    "img/lab3/iin_r_fourier.png"
)
thd = calculate_thd(fft_iin_r[1], 1, 50)
fp = 1/np.sqrt(1 + np.square(thd))
print("THD FWR R Iin: {}".format(thd))
print("FP FWR R Iin: {}".format(fp))

# Full Wave Rectfier Voltage Input Fourier Transform with RL Load
fft_vin_rl = plot_fourier_transform(
    1667,
    fwrrl_in.index.values,
    fwrrl_in['Vin (V)'].values,
    "Tensão (V)",
    "Tensão de Entrada do Retificador de Onda Completa Carga RL",
    "img/lab3/vin_rl_fourier.png"
)

# Full Wave Rectfier Current Input Fourier Transform with RL Load
fft_iin_rl = plot_fourier_transform(
    1667,
    fwrrl_in.index.values,
    fwrrl_in['Iin (A)'].values,
    "Corrente (A)",
    "Corrente de Entrada do Retificador de Onda Completa Carga RL",
    "img/lab3/iin_rl_fourier.png"
)
thd = calculate_thd(fft_iin_rl[1], 1, 50)
fp = 1/np.sqrt(1 + np.square(thd))
print("THD FWR RL Iin: {}".format(thd))
print("FP FWR RL Iin: {}".format(fp))

# Full Wave Rectfier Voltage Input Fourier Transform with RC Load
fft_vin_rc = plot_fourier_transform(
    2500,
    fwrrc_in.index.values,
    fwrrc_in['Vin (V)'].values,
    "Tensão (V)",
    "Tensão de Entrada do Retificador de Onda Completa Carga RC",
    "img/lab3/vin_rc_fourier.png"
)

# Full Wave Rectfier Current Input Fourier Transform with RC Load
fft_iin_rc = plot_fourier_transform(
    2500,
    fwrrc_in.index.values,
    fwrrc_in['Iin (A)'].values,
    "Corrente (A)",
    "Corrente de Entrada do Retificador de Onda Completa Carga RC",
    "img/lab3/iin_rc_fourier.png"
)
thd = calculate_thd(fft_iin_rc[1], 3, 50)
fp = 1/np.sqrt(1 + np.square(thd))
print("THD FWR RC Iin: {}".format(thd))
print("FP FWR RC Iin: {}".format(fp))