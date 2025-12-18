#%%

import numpy as np
import matplotlib.pyplot as plt
import pysmithchart 


Za = 0
Zb = 23.98*50
Zc = 1*50
Zd = 0.5*50
Ze = 2*50
plt.figure(figsize=(6,6))

plt.subplot(1,1,1, projection="smith",
             grid_major_fancy=False,
             grid_minor_enable=True,
             grid_minor_fancy=False)

plt.plot(Za,"b", label="Kurzschluss")
plt.plot(Zb,"r", label="Leerlauf")
plt.plot(Zc,"g", label="Anpassung")
plt.plot(Zd,"y", label="R1 = 100")
plt.plot(Ze,"c", label="R2 = 400")
plt.legend()


Zf = -0.83j*50
Zg = -0.18j*50
Zh = 0.65j*50
Zi = 1.36j*50
plt.figure(figsize=(6,6))

plt.subplot(1,1,1, projection="smith",
             grid_major_fancy=False,
             grid_minor_enable=True,
             grid_minor_fancy=False)

plt.plot(Zf,"b", label="C1 = 2.2pF")
plt.plot(Zg,"r", label="C2 = 10pF")
plt.plot(Zh,"y", label="L1 = 47nH")
plt.plot(Zi,"c", label="L2 = 100nH")
plt.legend()
plt.show()


Zj = (0.5 + 1.1j)*50
Ztestreal = (0.5 + 1j * np.linspace(-10,10,100))*50
Ztestimag = (np.linspace(-10,10,100) + 1.1j)*50
plt.figure(figsize=(6,6))

plt.subplot(1,1,1, projection="smith",
             grid_major_fancy=False,
             grid_minor_enable=True,
             grid_minor_fancy=False)

plt.plot(Ztestreal,"b", label="Realteil")
plt.plot(Ztestimag,"r", label="Imaginärteil")
plt.plot((0.5 + 1.1j)*50, "c", label="schnittpunkt")


plt.legend()
plt.show()


R0 = 200
R = 100
C = 4.8e-12
f = 422.92e6
w = 2*np.pi*f

r = np.sqrt(((R-R0)**2+(w*C)**2)/((R+R0)**2+(w*C)**2))
Y = 1/R + 1j*w*C
Z = 1/Y



Yn = Y*200
Zn = Z/200

Yjreal = (2 + 1j * np.linspace(-10,10,1000))*50
Yjimag = (np.linspace(-10,10,100) + 2.55j)*50

Zjreal = (np.real(Zn) + 1j*np.linspace(-10,10,1000))*50
Zjimag = (np.linspace(-10,10,100) +1j*np.imag(Zn))*50


plt.figure(figsize=(6,6))

plt.subplot(1,1,1, projection="smith",
             grid_major_fancy=False,
             grid_minor_enable=True,
             grid_minor_fancy=False)

plt.plot(Yjreal, markersize=1)
plt.plot(Yjimag, markersize=1)

plt.plot(Zjreal, markersize=1)
plt.plot(Zjimag, markersize=1)

plt.plot([Yn*50, (50)],label="r = 0.7")
plt.plot([Zn*50, (50)],label="r = 0.7")
plt.plot(Yn*50,label="Admittanz")
plt.plot(Zn*50, "r", label="Impedanz")
plt.legend()
plt.show()

print(np.real(Zn))

#r = z-1/z+1
r = np.sqrt(((np.real(Z)-R0)**2+(w*C)**2)/((np.real(Z)+R0)**2+(w*C)**2))
r = (Zn-1)/(Zn+1)
print(np.abs(r))

# %%
