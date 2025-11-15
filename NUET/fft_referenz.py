import numpy as np
from scipy.fft import fft, fftshift, fftfreq
import matplotlib.pyplot as plt

# Parameter
fs = 10000       # Abtastrate [Hz]
T = 1        # Signaldauer [s]
f0 = 500         # Sinusfrequenz [Hz]

# Zeitachse
t = np.arange(0, T, 1/fs)

# Signal
x = np.sin(2*np.pi*f0*t)

# FFT
N = len(x)
X = fft(x)
X_shifted = fftshift(X)

# Frequenzachse
freqs = fftshift(fftfreq(N, d=1/fs))

# Betragsspektrum (absolut)
X_mag = np.abs(X_shifted) / N    # Normalisierung wie Matlab
X_dB = 20*np.log10(X_mag)
# Plot
plt.figure(figsize=(10,4))
plt.plot(freqs, X_dB)
plt.xlabel("Frequenz [Hz]")
plt.ylabel("|X(f)|")
plt.title("Saubere FFT mit fftshift, Normalisierung, Frequenzachse")
plt.grid()
plt.show()
