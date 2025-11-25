# # # #test_signal
#%%
import matplotlib.pyplot as plt
import numpy as np
import commpy as cp
import random
from rrc import RootRaisedCosine

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

Nsym = 1000
Nos = 10
M = 4
r = 0.3
cfo_norm = 1e-3


rcos = cp.rrcosfilter(61, r, 1, Nos ) #Länge sample, rollof, Zeit/Sample, samplerate
rcosK = RootRaisedCosine(1,10,0.3,3)
g_tx = rcos[1]/Nos
g_txK = rcosK[0]
sym_tx = np.exp(1j*2*(np.pi/M)*np.random.randint(0,M,(1,Nsym)))*np.exp(1j*np.pi/4)

plt.figure()
plt.scatter(sym_tx.real, sym_tx.imag)
plt.title("Symbole die wir senden")

#Oversampling einführen
sym_tx_os = np.zeros(Nos*Nsym, dtype=complex)
sym_tx_os[0:Nsym*Nos:Nos] = sym_tx
#print(sym_tx_os)

#Faltung sym_tx mit g_tx

x_t = np.convolve(g_tx, sym_tx_os)
plt.figure()
plt.plot(rcos[0], rcos[1]/Nos)


plt.title("Matched Filter commpy")
plt.grid()

plt.figure()

plt.plot(rcosK[1],rcosK[0])
plt.title("Matched Filter Kron")
plt.grid()

plt.figure()
plt.plot(x_t)
plt.title("Symbole gefaltet mit filter")
#noise hinzufügen
noise_scale = 0.01
noise = noise_scale*(np.random.randn(len(x_t)) + 1j*np.random.randn(len(x_t)))
#print(noise)
deg = 10
phase_error_complex = np.exp(1j*(deg/180)*np.pi)



y_t = phase_error_complex*x_t + noise


g_rx = g_tx
z = np.convolve(y_t, g_rx)



plt.figure()
plt.scatter(z.real[0:Nsym:Nos], z.imag[0:Nsym:Nos])
print(z.real[::Nos])
plt.grid()
plt.title("empfangene symbol abgetastet")
plt.show()


# %%
