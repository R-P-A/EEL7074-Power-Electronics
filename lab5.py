# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import my functions
import numeric_analysis as na

# -------------------------------------------------------------------------------------------------

# Plotting original images from oscilloscope

orig_in_30_r = na.plot_oscope_original(
    output_name = "Gradador com Alfa 30° e Carga R - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/in_30_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/in_30_r_load/CH2.CSV",
    orig_path_mth = "src_img/lab5/in_30_r_load/MTH.CSV",
    output_path = "img/lab5/orig_in_30_r.png"
)

orig_in_30_rl = na.plot_oscope_original(
    output_name = "Gradador com Alfa 30° e Carga RL - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/in_30_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/in_30_rl_load/CH2.CSV",
    orig_path_mth = "src_img/lab5/in_30_rl_load/MTH.CSV",
    output_path = "img/lab5/orig_in_30_rl.png"
)

orig_in_60_r = na.plot_oscope_original(
    output_name = "Gradador com Alfa 60° e Carga R - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/in_60_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/in_60_r_load/CH2.CSV",
    orig_path_mth = "src_img/lab5/in_60_r_load/MTH.CSV",
    output_path = "img/lab5/orig_in_60_r.png"
)

orig_in_60_rl = na.plot_oscope_original(
    output_name = "Gradador com Alfa 60° e Carga RL - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/in_60_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/in_60_rl_load/CH2.CSV",
    orig_path_mth = "src_img/lab5/in_60_rl_load/MTH.CSV",
    output_path = "img/lab5/orig_in_60_rl.png"
)

orig_out_30_r = na.plot_oscope_original(
    output_name = "Gradador com Alfa 30° e Carga R - Saída",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/out_30_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/out_30_r_load/CH2.CSV",
    output_path = "img/lab5/orig_out_30_r.png"
)

orig_out_30_rl = na.plot_oscope_original(
    output_name = "Gradador com Alfa 30° e Carga RL - Saída",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/out_30_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/out_30_rl_load/CH2.CSV",
    output_path = "img/lab5/orig_out_30_rl.png"
)

orig_out_60_r = na.plot_oscope_original(
    output_name = "Gradador com Alfa 60° e Carga R - Saída",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/out_60_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/out_60_r_load/CH2.CSV",
    output_path = "img/lab5/orig_out_60_r.png"
)

orig_out_60_rl = na.plot_oscope_original(
    output_name = "Gradador com Alfa 60° e Carga RL - Saída",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    ch1_2_scale = 100,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab5/out_60_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/out_60_rl_load/CH2.CSV",
    output_path = "img/lab5/orig_out_60_rl.png"
)

# -------------------------------------------------------------------------------------------------

# Calculating THD and Plotting Fourier Transforms

# Input 30° R Load
fft_vin_30_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_30_r.index.values,
    values = orig_in_30_r["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Gradador com Alfa 30° e Carga R",
    out_path_name = "img/lab5/fft_vin_30_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_30_r[0], fft_vin_30_r[1], 60, 100)
print("\nTHD for Voltage Alfa 30° R Load: %s" % (THD))

fft_iin_30_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_30_r.index.values,
    values = orig_in_30_r["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Gradador com Alfa 30° e Carga R",
    out_path_name = "img/lab5/fft_iin_30_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_30_r[0], fft_iin_30_r[1], 60, 100)
print("THD for Current Alfa 30° R Load: %s" % (THD))

# Input 30° RL Load
fft_vin_30_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_30_rl.index.values,
    values = orig_in_30_rl["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Gradador com Alfa 30° e Carga RL",
    out_path_name = "img/lab5/fft_vin_30_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_30_rl[0], fft_vin_30_rl[1], 60, 100)
print("\nTHD for Voltage Alfa 30° RL Load: %s" % (THD))

fft_iin_30_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_30_rl.index.values,
    values = orig_in_30_rl["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Gradador com Alfa 30° e Carga RL",
    out_path_name = "img/lab5/fft_iin_30_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_30_rl[0], fft_iin_30_rl[1], 60, 100)
print("THD for Current Alfa 30° RL Load: %s" % (THD))

# Input 60° R Load
fft_vin_60_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_60_r.index.values,
    values = orig_in_60_r["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Gradador com Alfa 60° e Carga R",
    out_path_name = "img/lab5/fft_vin_60_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_60_r[0], fft_vin_60_r[1], 60, 100)
print("\nTHD for Voltage Alfa 60° R Load: %s" % (THD))

fft_iin_60_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_60_r.index.values,
    values = orig_in_60_r["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Gradador com Alfa 60° e Carga R",
    out_path_name = "img/lab5/fft_iin_60_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_60_r[0], fft_iin_60_r[1], 60, 100)
print("THD for Current Alfa 60° R Load: %s" % (THD))

# Input 60° RL Load
fft_vin_60_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_60_rl.index.values,
    values = orig_in_60_rl["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Gradador com Alfa 60° e Carga RL",
    out_path_name = "img/lab5/fft_vin_60_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_60_rl[0], fft_vin_60_rl[1], 60, 100)
print("\nTHD for Voltage Alfa 60° RL Load: %s" % (THD))

fft_iin_60_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_60_rl.index.values,
    values = orig_in_60_rl["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Gradador com Alfa 60° e Carga RL",
    out_path_name = "img/lab5/fft_iin_60_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_60_rl[0], fft_iin_60_rl[1], 60, 100)
print("THD for Current Alfa 60° RL Load: %s\n" % (THD))