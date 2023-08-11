"""
Created on April 15, 2020

@author : Richard Tsai

"""

import argparse
import soundfile
import numpy as np
from .signals import rms
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="Spectrum Analyzer")
    parser.add_argument("file", type=argparse.FileType('r'), nargs='+')
    parser.add_argument("-v", "--visualize", action='store_true',
                        help="visualize")
    parser.add_argument("-f", "--frame_size", type=int,
                        default=256,
                        help="samples in a frame")
    args = parser.parse_args()
    frame_size = args.frame_size

    if not args.visualize:
        for f in args.file:
            data, rate = soundfile.read(f.name)
            print("[rms] {}: {}".format(f.name, rms(data, frame_size=frame_size)))
    else:
        rates = []
        wavs = []
        names = []

        for f in args.file:
            data, rate = soundfile.read(f.name)
            if data.ndim > 1:
                for ch in range(data.ndim):
                    names.append('{} (ch{})'.format(f.name, ch))
                    rates.append(rate)
                    wavs.append(data[:, ch])
            else:
                names.append(f.name)
                rates.append(rate)
                wavs.append(data)

        num_samples_all = [len(data) for data in wavs]
        num_samples = min(num_samples_all)
        num_frames = int(num_samples / frame_size)

        rates = np.array(rates)
        if not np.all(rates == rates[0]):
            print("not all samples are the same")
            exit()
        rate = rates[0]

        timeticks_sec = np.arange(0, int(num_samples / rate), 1)
        timeticks_frame = timeticks_sec * rate / frame_size
        timeticks_sample = timeticks_sec * rate

        plt.subplot(2, 1, 1)
        for name, data in zip(names, wavs):
            plt.plot(data, label=name)

        plt.xlim([0, num_samples])
        plt.ylim([-1, 1])
        plt.xticks(timeticks_sample, timeticks_sec, rotation=45)
        plt.yticks(np.arange(-1, 1.1, 0.1))
        plt.grid()
        plt.xlabel('time (sec)')
        plt.ylabel('sample value')
        plt.legend()

        plt.subplot(2, 1, 2)
        for name, data in zip(names, wavs):
            rms_per_frame = []
            for i in range(num_frames):
                s, e = i * frame_size, (i + 1) * frame_size
                rms_per_frame.append(rms(data[s:e], frame_size))

            plt.plot(rms_per_frame, label=name)

        plt.xlim([0, num_frames])
        plt.ylim([-96, 0])
        plt.xticks(timeticks_frame, timeticks_sec, rotation=45)
        plt.yticks(np.arange(-96, 0, 3))
        plt.grid()
        plt.xlabel('time (sec)')
        plt.ylabel('rms (dB)')
        plt.legend()

        plt.show()


if __name__ == "__main__":
    main()
