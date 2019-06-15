# -*- coding: utf-8 -*-
"""
Spyder Editor

This is some nonsense.
"""
from scipy.io import wavfile as wf
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('tableau-colorblind10')

r, a = wf.read('po33juu.wav')
print(a.shape)
print(r)
N = a.shape[0]
L = N / r

np.fft(a)
print('jaa')
