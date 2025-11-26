import numpy as np

def RootRaisedCosine(Fd, Fs, r, delay):
    Td = 1 / Fd
    Ts = 1 / Fs

    # Zeitvektor wie in MATLAB
    t = np.arange(-np.floor(delay * Td / Ts), np.ceil(delay * Td / Ts) + 1) * Ts

    num = np.zeros(len(t), dtype=float)

    for idx in range(len(t)):
        ti = t[idx]

        if ti == 0:
            num[idx] = 1 - r + 4 * r / np.pi

        elif abs(ti) == Td / (4 * r):
            num[idx] = (r / np.sqrt(2)) * (
                (1 + 2 / np.pi) * np.sin(np.pi / (4 * r)) +
                (1 - 2 / np.pi) * np.cos(np.pi / (4 * r))
            )

        else:
            numerator = (
                np.sin(np.pi * (ti / Td) * (1 - r)) +
                4 * r * (ti / Td) * np.cos(np.pi * (ti / Td) * (1 + r))
            )
            denominator = (
                np.pi * (ti / Td) * (1 - (4 * r * (ti / Td))**2)
            )
            num[idx] = numerator / denominator

    # Normierung wie in MATLAB
    num = num / np.sum(num)

    return num, t
