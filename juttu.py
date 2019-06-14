# -*- coding: utf-8 -*-
"""
Spyder Editor

This is some nonsense.
"""
from scipy.io import wavfile as wf

r, a = wf.read('po33juu.wav')
print(a.shape)
print(r)
