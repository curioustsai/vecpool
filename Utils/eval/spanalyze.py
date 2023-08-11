"""
Created on June 14, 2022

@author : Richard Tsai

"""

import numpy as np
import argparse
from scipy import signal
from scipy.io import wavfile
from matplotlib import pyplot as plt


def parse_marker(marker_csv):
    list = []
    with open(marker_csv) as f:
        for line in f.readlines():
            s = line.split('\t')[0].strip()
            e = line.split('\t')[1].strip()
            list.append((s, e))
    return list


def main():
    parser = argparse.ArgumentParser(description="Spectrum Analyzer")
    parser.add_argument("file", type=argparse.FileType('r'), nargs='+')
    parser.add_argument("-m", "--marker", type=str, default=None)
    args = parser.parse_args()

    plt.rcParams['figure.figsize'] = [12.4, 9.6]
    fftlen_map = {"48000": 512, "44100": 512, "32000": 512, "16000": 256, "8000": 256}

    for f in args.file:
        fs, data = wavfile.read(f.name)
        if data.dtype == 'int16':
            data = data / 32768
        if data.ndim > 1:
            print("only show left channel")
            data = data[:, 0]

        fftlen = fftlen_map[str(fs)]

        if args.marker is not None:
            markers = parse_marker(args.marker)
        else:
            markers = [(0, len(data) / fs)]

        for s, e in markers:
            start = int(float(s) * fs)
            end = int(float(e) * fs)

            noverlap = fftlen // 2
            freq, Pxx = signal.welch(data[start:end],          # signal
                                     fs=fs,                    # sample rate
                                     nperseg=fftlen,           # segment size
                                     window='hann',         # window type to use
                                     nfft=fftlen,              # num. of samples in FFT
                                     detrend=False,            # remove DC part
                                     scaling='spectrum',       # return power spectrum [V^2]
                                     noverlap=noverlap)        # overlap between segments

            Pxx_dB = 10 * np.log10(Pxx)
            plt.plot(freq, Pxx_dB, label="{}, {}".format(s, e))

        plt.xlim([freq[2], freq[-1]])
        plt.ylim([-96, 0])
        # plt.xscale('log')   # uncomment if you want log scale on x-axis
        plt.yticks(np.arange(-96, 0, 6))
        plt.xlabel('f, Hz')
        plt.ylabel('Power spectrum, dB')
        plt.grid()
        plt.legend()

        plt.show()


if __name__ == "__main__":
    main()
