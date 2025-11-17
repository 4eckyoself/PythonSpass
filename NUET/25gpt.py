import numpy as np
from matplotlib import pyplot as plt

# Daten
Nos = 4
sym = np.array([1,1,-1,1,-1])
sym_os = np.ones(20)
# Erzeuge Oversampled-Symbolfolge (wie dein MATLAB x)
sym_os[:] = 1
sym_os[0::Nos] = sym  # ersetzt Indizes 0,4,8,12,16 -> 5 Symbole

h_tx = np.ones(Nos)
h_rx = h_tx / Nos   # matched filter mit Leistungsnormierung (wie MATLAB)

# --- matched filtering auf das Empfangssignal
y = np.array([2.7298,0.3914,0.2629,-0.7499,1.9105,1.8671,0.9201,1.8985,
              -0.8163,-0.7092,-0.8871,-0.5600,1.1017,3.7873,-0.1667,
              -0.8543,-2.1407,-2.0933,-1.4336,-1.1685,-0.2185,0.5413,0.3893])

# Verwende HIER nur h_rx als MF (wie MATLAB z = conv(y,h_rx))
z = np.convolve(y, h_rx)   # full convolution

# richtige Abtastindizes (MATLAB: [Nos:Nos:length(z)] -> Python: NOS-1, NOS-1+NOS, ...)
abtast_idx = np.arange(Nos-1, len(z), Nos)  # z-Indizes, die den Symboltakt entsprechen
d_rx = z[abtast_idx]

# SNR vor MF: Fehler = y(1:length(x)) - x   (MATLAB)
# Wir berechnen äquivalent mit sym_os (20 Samples)
error_signal = y[:len(sym_os)] - sym_os
var_e = np.mean((error_signal)**2)          # mittlere Fehlerleistung
var_sig = np.mean((sym_os)**2)              # mittlere Signal-Leistung
snr_vor_mf_dB = 10 * np.log10(var_sig / var_e)

# SNR nach MF (auf symbol-Ebene)
# im MATLAB-Code vergleichst du d (5 Symbole) mit abgetasteten Symbolen
# hier nehmen wir die ersten 5 abgegriffenen Symbole
d_rx_symbols = d_rx[:len(sym)]
error_symbols = sym - d_rx_symbols
var_e_sym = np.mean((error_symbols)**2)
var_sym = 1.0  # bei bipolaren +/-1 hat Var = 1 (oder Energie 1)
snr_nach_mf_dB = 10 * np.log10(var_sym / var_e_sym)

print("SNR vor MF [dB]:", snr_vor_mf_dB)
print("SNR nach MF  [dB]:", snr_nach_mf_dB)
print("SNR-Gewinn theoretisch [dB]:", 10*np.log10(Nos))

# kurze Visualisierung
plt.figure(); plt.plot(z, '-x', label='z (y gefiltert)')
plt.plot(abtast_idx, d_rx, 'ro', label='Abtastpunkte (Symboltakt)')
plt.legend(); plt.grid(); plt.show()
