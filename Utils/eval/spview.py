"""
Created on April 15, 2020

@author : Richard Tsai

"""

import numpy as np
import argparse
from scipy.io import wavfile
from matplotlib import pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="Spectrum Analyzer")
    parser.add_argument("file", type=argparse.FileType('r'), nargs='+')
    args = parser.parse_args()

    for f in args.file:
        fftlen_map = {"48000": 512, "44100": 512, "32000": 512, "16000": 256, "8000": 256}

        fs, data = wavfile.read(f.name)
        if data.dtype == 'int16':
            data = data / 32768

        if data.ndim > 1:
            print("only show left channel")
            data = data[:, 0]

        plt.subplot(211)
        plt.rcParams['figure.figsize'] = [24.8, 19.2]
        plt.plot(data)
        plt.xlim(0, len(data))
        plt.ylim(-1, 1)
        xticks = np.arange(0, len(data) // fs)
        xticks_samples = xticks * fs
        plt.xticks(xticks_samples, xticks)
        plt.grid()

        plt.subplot(212)
        fftlen = fftlen_map[str(fs)]
        Pxx, freqs, bins, im = plt.specgram(data, NFFT=fftlen, Fs=fs, noverlap=fftlen//2)

        plt.title(f.name)
        plt.show()


if __name__ == "__main__":
    main()
