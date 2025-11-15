#%%

import numpy as np
from numpy.fft import fft, fftshift, fftfreq
from matplotlib import pyplot as plt


def Plot(x,xlabel,ylabel,label, type):
    plt.figure()
    if type == "plot":
        plt.plot(x, label="label")
    if type == "stem":
        plt.stem(x, label="label")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    

sym = np.array([1,1,-1,1,-1])

NOS =4
sym_os = np.array([1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1])
gtx = np.ones(NOS)

sym_os[0::NOS] = sym

Plot(sym_os,"Ts", "Symbole","Symbole", "stem")
h_tx = gtx
h_rx = gtx / NOS


MF = np.convolve(h_tx,h_rx)


y = np.array([2.7298,0.3914,0.2629,-0.7499,1.9105,1.8671,0.9201,1.8985,-0.8163,-0.7092,
   -0.8871,-0.5600,1.1017,3.7873,-0.1667,-0.8543,-2.1407,-2.0933,-1.4336,-1.1685,-0.2185,0.5413,0.3893])


#Plot(y, "Ts", "verrauschtes Signal","verrauschtes signal", "plot")

y_trans = np.convolve(y,MF)
#Plot(y_trans, "", "","empfang durch MF", "plot")
fehler = y[:len(sym_os)]-sym_os
##Fehler = empfangenes - symbole abgetastet
##SNR = ox² / oe² = signal/fehler
var_sig = np.mean(np.abs(sym_os))
var_e = np.mean(np.abs(fehler**2))
snr_vorher_db = np.log10(var_sig/var_e)

print("snr vor MF: ", snr_vorher_db )



z = np.convolve(y,MF)
#Plot(z, "zeit", "y nach MF", "y nach MF", "plot")

figure, ax = plt.subplots()
ax.plot(y, color="red",label="verrauscht")

ax.plot(sym_os,color="green", label="symbole ohne Rauschen")
plt.legend()


nrows = 3
ncols = 1
plt.grid()


plt.figure()
plt.plot(z)
plt.title("z -> y nach MF")


##z abtasten

abtast = np.arange(NOS,len(z)-1,NOS)



plt.figure()

plt.plot(z)
plt.plot(abtast, z[abtast], "rp")
plt.grid()


d_rx = z[abtast]
plt.figure()
plt.stem(sym, "rp",label="original" )
plt.stem(d_rx, label="nach MF")

plt.legend()

plt.show()

print(d_rx)
print(z)

# %%
