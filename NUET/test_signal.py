# # # #test_signal
#%%
import matplotlib.pyplot as plt
import numpy as np
import commpy as cp
import random

from costaloop import costaLoop




Nsym = 1000
Nos = 10
M = 2
r = 0.3
cfo_norm = 1e-3


rcos = cp.rrcosfilter(61, r, 1, Nos ) #Länge sample, rollof, Zeit/Sample, samplerate

g_tx = (rcos[1]/Nos).astype(complex)


sym_tx = np.exp(1j*2*(np.pi/M)*np.random.randint(0,M,(1,Nsym)))

plt.figure()
plt.scatter(sym_tx.real, sym_tx.imag)
plt.title("Symbole die wir senden")

#Oversampling einführen
sym_tx_os = np.zeros(Nos*Nsym, dtype=complex)
sym_tx_os[0:Nsym*Nos:Nos] = sym_tx.astype(complex)
#print(sym_tx_os)

#Faltung sym_tx mit g_tx

x_t = np.convolve(g_tx, sym_tx_os).astype(complex)

plt.figure()
plt.plot(rcos[0], rcos[1])


plt.title("Matched Filter commpy")
plt.grid()



plt.figure()
plt.plot(x_t)
plt.title("Symbole gefaltet mit filter")
#noise hinzufügen
noise_scale = 0.01
noise = noise_scale*(np.random.randn(len(x_t)) + 1j*np.random.randn(len(x_t))).astype(complex)
#print(noise)
deg = 10
phase_error_complex = np.exp(1j*(deg/180)*np.pi)



y_t = (phase_error_complex*x_t + noise).astype(complex)
y_cfo = y_t*np.exp(1j*2*np.pi*cfo_norm*np.arange(len(y_t))/Nos)


###costa loop

y_corrected = costaLoop(y_cfo, 0.4)

phasearray = np.zeros(len(y_cfo))
errorarray = np.zeros(len(y_cfo))



###


g_rx = g_tx.astype(complex)

z = np.convolve(y_t, g_rx)
zcfo = np.convolve(y_cfo, g_rx)
zcorr = np.convolve(y_corrected[0], g_rx)



plt.figure()
plt.scatter(z.real[1:Nsym:Nos], z.imag[1:Nsym:Nos])

plt.grid()
plt.title("empfangene symbol abgetastet")


plt.figure()
plt.scatter(zcfo.real[1:Nsym:Nos], zcfo.imag[1:Nsym:Nos])
plt.grid()
plt.title("empfangene symbol abgetastet, cfo")



plt.figure()
plt.scatter(zcorr.real[1:Nsym:Nos], zcorr.imag[1:Nsym:Nos])
plt.grid()
plt.title("phase corrected")


plt.show()

# for i in np.arange(0,Nos):
#     plt.figure()
#     plt.scatter(z[i::Nos].real, z[i::Nos].imag)
#     plt.title(str(i))
#     plt.show()
#     print(i)

# %%
