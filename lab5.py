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
    orig_path_ch1 = "src_img/lab5/in_30_r_load/CH1.CSV",
    orig_path_ch2 = "src_img/lab5/in_30_r_load/CH2.CSV",
    orig_path_mth = "src_img/lab5/in_30_r_load/MTH.CSV",
    output_path = "img/lab5/orig_30_in_r.png"
)