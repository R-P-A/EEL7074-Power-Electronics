# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import my functions
import harmonic_analysis as ha

# -------------------------------------------------------------------------------------------------

# Plotting original images from oscilloscope

orig_in_r = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga R - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 50,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab4/in_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/in_r_load/CH2.CSV",
    orig_path_mth = "src_img/lab4/in_r_load/MTH.CSV",
    output_path = "img/lab4/orig_in_r.png"
)

orig_in_rl = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga RL - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 50,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab4/in_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/in_rl_load/CH2.CSV",
    orig_path_mth = "src_img/lab4/in_rl_load/MTH.CSV",
    output_path = "img/lab4/orig_in_rl.png"
)

orig_in_rc = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga RC - Entrada",
    ch1_name = "Vin (V)",
    ch2_name = "Iin (A)",
    mth_name = "P (W)",
    ch1_2_scale = 50,
    xlimits = [-0.012, 0.012],
    orig_path_ch1 = "src_img/lab4/in_rc_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/in_rc_load/CH2.CSV",
    orig_path_mth = "src_img/lab4/in_rc_load/MTH.CSV",
    output_path = "img/lab4/orig_in_rc.png"
)

orig_out_r = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga R - Saída",
    ch1_name = "Vout (V)",
    ch2_name = "Iout (A)",
    mth_name = "P (W)",
    ch1_2_scale = 160,
    xlimits = [-0.003, 0.003],
    orig_path_ch1 = "src_img/lab4/out_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/out_r_load/CH2.CSV",
    output_path = "img/lab4/orig_out_r.png"
)

orig_out_rc = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga RC - Saída",
    ch1_name = "Vout (V)",
    ch2_name = "Iout (A)",
    mth_name = "P (W)",
    ch1_2_scale = 160,
    xlimits = [-0.003, 0.003],
    orig_path_ch1 = "src_img/lab4/out_rc_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/out_rc_load/CH2.CSV",
    output_path = "img/lab4/orig_out_rc.png"
)

orig_out_rl = ha.plot_oscope_original(
    output_name = "Retificador de Onda Completa Trifásico Carga RL - Saída",
    ch1_name = "Vout (V)",
    ch2_name = "Iout (A)",
    mth_name = "P (W)",
    ch1_2_scale = 160,
    xlimits = [-0.003, 0.003],
    orig_path_ch1 = "src_img/lab4/out_rl_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab4/out_rl_load/CH2.CSV",
    output_path = "img/lab4/orig_out_rl.png"
)

# -------------------------------------------------------------------------------------------------

# Calculating THD and Plotting Fourier Transforms

fft_vin_r = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_r.index.values,
    values = orig_in_r["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_vin_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_iin_r = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_r.index.values,
    values = orig_in_r["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_iin_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_vin_rl = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rl.index.values,
    values = orig_in_rl["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_vin_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_iin_rl = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rl.index.values,
    values = orig_in_rl["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_iin_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_vin_rc = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rc.index.values,
    values = orig_in_rc["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_vin_rc.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_iin_rc = ha.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rc.index.values,
    values = orig_in_rc["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_iin_rc.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)

fft_vout_r = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_vout_r.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)

fft_iout_r = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_iout_r.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)

fft_vout_rl = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_vout_rl.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)

fft_iout_rl = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_iout_rl.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)

fft_vout_rc = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_vout_rc.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)

fft_iout_rc = ha.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_iout_rc.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 2000]
)