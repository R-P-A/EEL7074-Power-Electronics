# Using https://www.safaribooksonline.com/library/view/elegant-scipy/9781491922927/ch04.html Tutorial

import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

f = 10  # Frequency, in cycles per second, or Hertz
f_s = 100  # Sampling rate, or number of measurements per second

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(f * 2 * np.pi * t)

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x)
ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Signal amplitude')

X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s

ax[1].stem(freqs, np.abs(X))
ax[1].set_xlabel('Frequency in Hertz [Hz]')
ax[1].set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax[1].set_xlim(-f_s / 2, f_s / 2)
ax[1].set_ylim(-5, 110)

plt.show()