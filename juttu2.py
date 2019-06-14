# -*- coding: utf-8 -*-
"""
Spyder Editor

This is some nonsense.
"""
from scipy.io import wavfile as wf
import numpy as np
import matplotlib.pyplot as plt

r, a = wf.read('po33juu.wav')
a = np.mean(a, axis=1)
N = a.shape[0]
L = N / r

f, ax = plt.subplots()
ax.plot(np.arange(N) / r, a);