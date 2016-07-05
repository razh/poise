from __future__ import division

import numpy as np
import sounddevice as sd

fs = 44100
sd.default.samplerate = fs


def noise(duration):
    data = np.random.uniform(-1, 1, fs * duration)
    sd.play(data, blocking=True)


def to_frequency(note):
    return 2 ** ((note - 69) / 12) * 440


A4 = to_frequency(69)
C4 = to_frequency(73)
E4 = to_frequency(76)


# http://stackoverflow.com/questions/10357992/how-to-generate-audio-from-a-numpy-array
def sin(frequency, duration):
    samples = np.arange(fs * duration) / fs
    waveform = np.sin(2 * np.pi * frequency * samples)
    sd.play(waveform, blocking=True)


for _ in range(3):
    sin(A4, 1 / 8)
    sin(C4, 1 / 8)
    sin(E4, 1 / 8)
