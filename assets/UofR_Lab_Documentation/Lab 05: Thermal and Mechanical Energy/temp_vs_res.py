# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rc('font', family='Palatino', size=14)
mpl.rc('text', usetex=True)

def temp(R):
    return 67.03 - 0.7136*R + 3.801e-3*R**2 - 8.680e-6*R**3

#R1 = np.genfromtxt('c1.txt')
#R2 = np.genfromtxt('c2.txt')
#R3 = np.genfromtxt('c3.txt')
#R = np.concatenate([R1, R2, R3])
T = np.arange(0,101)

R = np.array([351.02, 332.64, 315.32, 298.99, 283.6,   269.08, 255.38,  242.46,
              230.26, 218.73, 207.85, 197.56, 187.84,  178.65, 169.95,  161.73,
              153.95, 146.58, 139.61, 133.,   126.74,  120.81, 115.19,  109.85,
              104.8,  100.,    95.447, 91.126, 87.022,  83.124, 79.422, 75.903,
               72.56,  69.38,  66.356, 63.48,  60.743,  58.138, 55.658, 53.297,
               51.048, 48.905, 46.863, 44.917, 43.062,  41.292, 39.605, 37.995,
               36.458, 34.991, 33.591, 32.253, 30.976,  29.756, 28.59,  27.475,
               26.409, 25.39,  24.415, 23.483, 22.59,   21.736, 20.919, 20.136,
               19.386, 18.668, 17.98,  17.321, 16.689,  16.083, 15.502, 14.945,
               14.41,  13.897, 13.405, 12.932, 12.479,  12.043, 11.625, 11.223,
               10.837, 10.467, 10.11,   9.7672, 9.4377, 9.1208,  8.816, 8.5227,
                8.2406, 7.9691, 7.7077, 7.4562, 7.214,  6.9806, 6.7559, 6.5394,
                6.3308, 6.1298, 5.9361, 5.7493, 5.5693])

for i, (c1, c2, c3, c4, c5) in enumerate(zip(R[:20], R[20:40], R[40:60], R[60:80], R[80:])):
    print(f'{c1:8.3f} & {i:3} & {c2:8.3f} & {i+20:3} & {c3:8.3f} & {i+40:3} & {c4:8.3f} & {i+60:3} & {c5:8.3f} & {i+80:3} \\\\')

fig, ax = plt.subplots(1,1, figsize=(9,4), tight_layout=True)
ax.plot(R, T, label='temperature vs. resistance data')
ax.plot(R, temp(R), ls='--', label='$T(R) = a + bR + cR^2 + dR^3$')
ax.set(xlim=(0,400),
       xlabel='resistance [$\mathrm{k}\Omega$]',
       ylim=(0,50),
       ylabel='temperature [$^\circ$C]')

ax.legend(loc='lower left', fontsize=12, frameon=False)

# Inset axes in subregion
x1, x2, y1, y2 = 70, 120, 20, 32
axins = ax.inset_axes([252,18,140,30], transform=ax.transData)
#axins = ax.inset_axes([0.6,0.3, 0.35,0.65])
axins.plot(R, T)
axins.plot(R, temp(R), ls='--')
axins.set(xlim=(x1,x2),
          xlabel='resistance [$\mathrm{k}\Omega$]',
          ylim=(y1,y2),
          ylabel='temperature [$^\circ$C]'
)

axins.xaxis.label.set_size(10)
axins.yaxis.label.set_size(10)
axins.tick_params(axis='both', which='major', labelsize=10)

rect = mpl.patches.Rectangle([x1,y1], width=x2-x1, height=y2-y1)
rect.set(fc='None', ec='gray', ls=':')
ax.add_artist(rect)

con = mpl.patches.ConnectionPatch(
          xyA=(x2,y2), xyB=(410,258),
          coordsA='data', coordsB='figure points',
          axesA=ax, axesB=axins,
          color='gray', alpha=0.6, lw=1, ls=':')
ax.add_artist(con)

con = mpl.patches.ConnectionPatch(
          xyA=(x2,y1), xyB=(410,131),
          coordsA='data', coordsB='figure points',
          axesA=ax, axesB=axins,
          color='gray', alpha=0.6, lw=1, ls=':')
ax.add_artist(con)

#rect, conns = ax.indicate_inset_zoom(axins, edgecolor='k', transform=ax.transData)
#rect.set(ls=':')
#conns[1].set(ls=':')
#conns[2].set(ls=':')

fig.savefig('temp_vs_res.pdf')
plt.show()
