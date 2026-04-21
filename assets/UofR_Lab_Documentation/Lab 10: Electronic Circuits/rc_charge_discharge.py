# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rc('font', family='Palatino', size=16)
mpl.rc('text', usetex=True)

VB = 1.
R = 1.
C = 1.
tau = R*C
Q = VB*C
I0 = VB/R
dt = 0.01*tau

def q_charge(t):
    return Q*(1 - np.exp(-t/tau))

def I_charge(t):
    return I0 * np.exp(-t/tau)

def q_discharge(t):
    return Q*np.exp(-t/tau)

def I_discharge(t):
    return -Q/tau * np.exp(-t/tau)

def Vsquare(t, T):
    V = VB*0.5*(1 + np.sign(np.sin(2*np.pi*t/T)))
    V[0] = 0
    return V

def Vrc(t, T):
    phase = np.sign(np.sin(2*np.pi*t/T))
    chg = phase >= 0
    dch = ~chg
    V = np.zeros_like(phase)
    V[chg] = VB*(1 - np.exp(-(t[chg] % T)/tau))
    V[dch] = VB*np.exp(-(t[dch] % (T/2))/tau)
    i = np.where(t % T == 0)
    V[i] = 0
    return V

t = np.arange(0, 5*tau + dt, dt)
timelabels = ['0', r'$\tau$'] + [rf'${n}\tau$' for n in np.arange(2,6)]

# RC charge
fig, axes = plt.subplots(1,2, figsize=(12,3.5), sharex=True, tight_layout=True)

ax = axes[0]
ax.plot(t, q_charge(t), color='royalblue', lw=2)
ax.set(xlabel='time [s]',
       xlim=(t[0], t[-1]),
       xticklabels=timelabels,
       ylim=(0, 1.1*Q),
       yticks=(0, 0.5*Q, Q*(1-np.exp(-1)), Q),
       yticklabels=('0', '', f'${Q*(1-np.exp(-1)):.3f}CV_B$', '$CV_B$'),
       ylabel='$q(t)$ [C]',
       title='capacitor charge')
ax.axhline(Q, ls=':', color='red')
ax.plot((0, tau), (Q*(1-np.exp(-1)), Q*(1-np.exp(-1))), ls=':', color='red')
ax.plot((tau, tau), (0, Q*(1-np.exp(-1))), ls=':', color='red')

ax = axes[1]
ax.plot(t, I_charge(t), color='royalblue', lw=2)
ax.set(xlabel='time [s]',
       ylim=(0, 1.1*I0),
       yticks=(0, 0.5*I0, I0*(np.exp(-1)), I0),
       yticklabels=('0', '', rf'${I0*np.exp(-1):.3f}\frac{{V_B}}{{R}}$', r'$\frac{V_B}{R}$'),
       ylabel='$I(t)$ [A]',
       title='current')
ax.plot((0, tau), (I0*np.exp(-1), I0*np.exp(-1)), ls=':', color='red')
ax.plot((tau, tau), (0, I0*np.exp(-1)), ls=':', color='red')

fig.savefig('rc_charging.pdf')

# RC discharge
fig, axes = plt.subplots(1,2, figsize=(12,3.5), sharex=True, tight_layout=True)

ax = axes[0]
ax.plot(t, q_discharge(t), color='royalblue', lw=2)
ax.set(xlabel='time [s]',
       xlim=(t[0], t[-1]),
       xticklabels=timelabels,
       ylim=(0, 1.1*Q),
       yticks=(0, 0.5*Q, Q*np.exp(-1), Q),
       yticklabels=('0', '', f'${Q*np.exp(-1):.3f}CV_B$', '$CV_B$'),
       ylabel='$q(t)$ [C]',
       title='capacitor charge')
ax.plot((0, tau), (Q*np.exp(-1), Q*np.exp(-1)), ls=':', color='red')
ax.plot((tau, tau), (0, Q*np.exp(-1)), ls=':', color='red')

ax = axes[1]
ax.plot(t, I_discharge(t), color='royalblue', lw=2)
ax.set(xlabel='time [s]',
       ylim=(-1.1*I0, 0),
       yticks=(0, -0.5*I0, -I0*(np.exp(-1)), -I0),
       yticklabels=('0', '', rf'$-{I0*np.exp(-1):.3f}\frac{{V_B}}{{R}}$', r'$-\frac{V_B}{R}$'),
       ylabel='$I(t)$ [A]',
       title='current')
ax.plot((0, tau), (-I0*np.exp(-1), -I0*np.exp(-1)), ls=':', color='red')
ax.plot((tau, tau), (0, -I0*np.exp(-1)), ls=':', color='red')

fig.savefig('rc_discharging.pdf')

# Square wave input and RC charge/discharged output
T = 10*tau
t = np.arange(0, 2*T+dt, dt)

timelabels = ['$0$'] + [rf'${n:g}\tau$' for n in np.arange(5,25,5)]
print(timelabels)

fig, axes = plt.subplots(1,2, figsize=(12,3.5), sharex=True, tight_layout=True)

ax = axes[0]
ax.plot(t, Vsquare(t, T), color='royalblue', lw=2)
ax.set(xlabel='time [s]',
       xlim=(0, t[-1]),
       xticklabels=timelabels,
       yticks=(0, 0.25*VB, 0.5*VB, 0.75*VB, VB),
       yticklabels=('$0$', '', '', '', '$V_s$'),
       title='supply voltage'
)

ax = axes[1]
ax.plot(t, Vrc(t, T), color='royalblue', lw=2)
ax.plot(t, Vsquare(t, T), color='red', ls=':')
ax.set(xlabel='time [s]',
       yticks=(0, 0.25*VB, 0.5*VB, 0.75*VB, VB),
       yticklabels=('$0$', '', '', '', '$V_C$'),
       title='capacitor voltage'
)
fig.savefig('rc_charge_discharge_cycle.pdf')

plt.show()
