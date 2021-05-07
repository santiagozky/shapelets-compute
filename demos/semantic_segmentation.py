# %% 
import math
import numpy as np
import matplotlib.pyplot as plt
import shapelets.compute as sc
from shapelets.data import load_mat, load_dataset 

# %% 
def ending_phase(c, mag):
    angle = math.asin(c[-1] / mag)
    if c[-2] > c[-1]:
        angle = np.pi - angle
    return angle

def next_phase(c, mag):
    ph1 = ending_phase(c[:-1], mag)
    ph2 = ending_phase(c, mag)
    return 2 * ph2 - ph1

def createData(noiseScale = 0.001, freqBase = 5.0, nextFreq = 6.0):
    t = np.linspace(0,1,4000)
    mag = 10.0
    freq = freqBase
    phase = 0.0
    c1 = mag * np.sin(2 * np.pi * freq * t + phase)

    freq = nextFreq
    phase = next_phase(c1, mag)
    c2 = mag * np.sin(2 * np.pi * freq * t + phase)

    data = np.concatenate((c1,c2))
    data = data + np.random.normal(0.0, noiseScale, len(data))
    return data

# %%
wLen = 800
noiseScale = 0.10
freqBase = 5.0
nextFreq = 5.1

data = createData(noiseScale, freqBase, nextFreq)
# %%
plt.plot(data)
plt.show()
# %%

profile, index, _ = sc.matrixprofile.matrix_profile(data, wLen)

# %%
minPoint = sc.matrixprofile.segment(profile, index, wLen, 1)[0]
print(minPoint)
# %%

fig, ax = plt.subplots(2,1, figsize=(18, 8))
ax[0].plot(profile)
ax[1].plot(data)
ax[1].axvspan(minPoint, minPoint+wLen, facecolor="yellow", edgecolor='none', alpha=0.5)
plt.show()

# %%

medts = load_dataset('ecg-heartbeat-av.txt')
wLen = 150
profile, index, _ = sc.matrixprofile.matrix_profile(medts, wLen)
r = sc.matrixprofile.segment(profile, index, wLen)
if len(r) > 0:
    plt.plot(medts,'--g')
    plt.plot(r, medts[sc.array(r)], 'rD')
    plt.show()

# %%
wLen = 800
data = load_mat('ItalianPowerDemand.mat')[10000:15000,2]
profile, index, _ = sc.matrixprofile.matrix_profile(data, wLen)
minPoint = sc.matrixprofile.segment(profile, index, wLen, 1)[0]
fig, ax = plt.subplots(4, 1, figsize=(18, 8))
ax[0].plot(profile)
ax[1].plot(sc.matrixprofile.cac(profile, index, wLen))
ax[2].plot(data)
ax[2].axvspan(minPoint, minPoint+wLen, facecolor="yellow", edgecolor='none', alpha=0.5)
ax[3].plot(data[minPoint-wLen:minPoint+2*wLen])
ax[3].axvspan(wLen, 2*wLen, facecolor="yellow", edgecolor='none', alpha=0.5)
plt.show()

# %%
