# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rc('font', family='Palatino', size=16)
mpl.rc('text', usetex=True)

Vs = 1.
R = 1. 
L = 9.
C = 1.
Q = 1/R * np.sqrt(L/C)

w0 = np.sqrt(1/(L*C))
dw = 1e-3 * w0
w  = np.arange(dw, 3*w0+dw, dw)
Z  = np.sqrt(R**2 + (w*L - 1/(w*C))**2)
ampl = Vs*R / Z

# Max amplitude and amplitude at FWHM power
Vmax = Vs*R
Vhmx = Vmax / np.sqrt(2)

# Frequencies of FWHM (below and above w0):
idx = np.argmin(np.abs(w - w0))
i = np.argmin(np.abs(ampl[w < w0] - Vhmx))
j = np.argmin(np.abs(ampl[w > w0] - Vhmx)) + idx
print(idx, w[idx], w[idx]/w0)
print(i, j, w[i]/w0, w[j]/w0)
print(Q, w0 / (w[j] - w[i]))

fig, ax = plt.subplots(1,1, figsize=(5,3.5), sharex=True, tight_layout=True)
ax.plot(w/w0, ampl)
ax.set(xlim=(0, w[-1]/w0),
       xticks=(0, 1, 2, 3),
       xticklabels=('$0$', r'$\omega_0$', r'$2\omega_0$', r'$3\omega_0$'),
       xlabel=r'input frequency $\omega$',
       yticks=(0, Vhmx, Vmax),
       yticklabels=('$0$', r'$\frac{V_\mathrm{max}}{\sqrt{2}}$', r'$V_\mathrm{max}$'),
       ylabel=r'amplitude of $V_R$',
       ylim=(0, 1.1*Vmax)
       )
ax.axvline(1, color='red', ls=':')
ax.axhline(Vmax, color='gray', ls=':')
ax.axhline(Vhmx, color='gray', ls=':')

ax.annotate('', 
            xy=(w[i]/w0, Vhmx), xytext=(w[j]/w0, Vhmx),
            arrowprops=dict(arrowstyle='<|-|>', fc='black'),
            color='red')

ax.text(1.05*w[j]/w0, 1.05*Vhmx, r'$\Delta\omega$')
fig.savefig('qfactor.pdf')

plt.show()
