# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import my functions
import numeric_analysis as na

# -------------------------------------------------------------------------------------------------

# Plotting original images from oscilloscope

orig_in_r = na.plot_oscope_original(
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

orig_in_rl = na.plot_oscope_original(
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

orig_in_rc = na.plot_oscope_original(
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

orig_out_r = na.plot_oscope_original(
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

orig_out_rc = na.plot_oscope_original(
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

orig_out_rl = na.plot_oscope_original(
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

# Input R Load
fft_vin_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_r.index.values,
    values = orig_in_r["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_vin_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_r[0], fft_vin_r[1], 60, 100)
print("THD for Voltage R Load: %s" % (THD))

fft_iin_r = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_r.index.values,
    values = orig_in_r["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_iin_r.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_r[0], fft_iin_r[1], 60, 100)
print("THD for Current R Load: %s" % (THD))
PF = 1/np.sqrt(1 + THD**2)
print("Power Factor R Load: %s\n" % (PF))

# Input RL Load
fft_vin_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rl.index.values,
    values = orig_in_rl["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_vin_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_rl[0], fft_vin_rl[1], 60, 100)
print("THD for Voltage RL Load: %s" % (THD))

fft_iin_rl = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rl.index.values,
    values = orig_in_rl["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_iin_rl.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_rl[0], fft_iin_rl[1], 60, 100)
print("THD for Current RL Load: %s" % (THD))
PF = 1/np.sqrt(1 + THD**2)
print("Power Factor RL Load: %s\n" % (PF))

# Input RC Load
fft_vin_rc = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rc.index.values,
    values = orig_in_rc["Vin (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Entrada do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_vin_rc.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_vin_rc[0], fft_vin_rc[1], 60, 100)
print("THD for Voltage RC Load: %s" % (THD))

fft_iin_rc = na.plot_fourier_transform(
    number_samples = 2500,
    time = orig_in_rc.index.values,
    values = orig_in_rc["Iin (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Entrada do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_iin_rc.png",
    xlimits0 = [-0.012, 0.012],
    xlimits1 = [0, 800]
)
THD = na.calculate_thd(fft_iin_rc[0], fft_iin_rc[1], 60, 100)
print("THD for Current RC Load: %s" % (THD))
PF = 1/np.sqrt(1 + THD**2)
print("Power Factor RC Load: %s\n" % (PF))

# Output R Load
fft_vout_r = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_vout_r.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_vout_r_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_vout_r_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
THD = na.calculate_thd(fft_vout_r[0], fft_vout_r[1], 360, 100)
print("THD for Voltage Output R Load: %s" % (THD))

fft_iout_r = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_iout_r.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_iout_r_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_r.index.values,
    values = orig_out_r["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga R",
    out_path_name = "img/lab4/fft_iout_r_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
print ("Currente Average for Output R Load: %s" % (na.calculate_average(orig_out_r["Iout (A)"].values, 231)/3))
THD = na.calculate_thd(fft_iout_r[0], fft_iout_r[1], 360, 100)
print("THD for Current Output R Load: %s\n" % (THD))

# Output RL Load
fft_vout_rl = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_vout_rl.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_vout_rl_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_vout_rl_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
THD = na.calculate_thd(fft_vout_rl[0], fft_vout_rl[1], 360, 100)
print("THD for Voltage Output RL Load: %s" % (THD))

fft_iout_rl = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_iout_rl.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_iout_rl_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rl.index.values,
    values = orig_out_rl["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RL",
    out_path_name = "img/lab4/fft_iout_rl_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
print ("Currente Average for Output RL Load: %s" % (na.calculate_average(orig_out_rl["Iout (A)"].values, 231)/3))
THD = na.calculate_thd(fft_iout_rl[0], fft_iout_rl[1], 360, 100)
print("THD for Current Output RL Load: %s\n" % (THD))

# Output RC Load
fft_vout_rc = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_vout_rc.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_vout_rc_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Vout (V)"].values,
    y_name = "Tensão (V)",
    title = "Tensão de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_vout_rc_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
THD = na.calculate_thd(fft_vout_rc[0], fft_vout_rc[1], 360, 100)
print("THD for Voltage Output RC Load: %s" % (THD))

fft_iout_rc = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_iout_rc.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800]
)
fft_iout_rc_ylog = na.plot_fourier_transform(
    number_samples = 2083,
    time = orig_out_rc.index.values,
    values = orig_out_rc["Iout (A)"].values,
    y_name = "Corrente (A)",
    title = "Corrente de Saída do Retificador de Onda Completa Trifásico Carga RC",
    out_path_name = "img/lab4/fft_iout_rc_log.png",
    xlimits0 = [-0.003, 0.003],
    xlimits1 = [0, 4800],
    ylog = True
)
THD = na.calculate_thd(fft_iout_rc[0], fft_iout_rc[1], 360, 100)
print("THD for Current Output RC Load: %s\n" % (THD))