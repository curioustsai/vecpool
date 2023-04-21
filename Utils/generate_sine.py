import numpy as np
import soundfile as sf


def dB2lin(value):
    return pow(10.0, 0.05 * value)


def generate_sine(fs=48000, duration=5, fc=1000, amplitude=0.5):
    total_length = fs * duration
    buf = np.zeros(total_length, dtype=float)
    for i in range(total_length):
        buf[i] = amplitude * np.sin(2 * np.pi * fc * i / fs)

    return buf


if __name__ == "__main__":
    fs = 32000
    amps = np.arange(-60, 0, 3)
    amps = [dB2lin(amp) for amp in amps]
    bufs = [generate_sine(fs=fs, amplitude=amp) for amp in amps]
    buf = np.concatenate(bufs)
    sf.write("amp.wav", buf, fs, subtype='PCM_32')
