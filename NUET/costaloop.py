import numpy as np

def costaLoop(y, kp):
    N = len(y)
    phase_ist = 0

    phase_array = np.zeros(N)
    error_array = np.zeros(N)
    z_out = np.zeros(N, dtype=complex)

    for i in range(N):
        phi = np.exp(-1j*phase_ist)
        z = y[i]*phi
        z_out[i] = z
        error = np.real(z) * np.imag(z)
        phase_ist = phase_ist + kp*error
        phase_ist = np.mod(phase_ist, np.pi*2)

        
    return z_out

        
        
