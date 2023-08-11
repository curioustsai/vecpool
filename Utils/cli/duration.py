#!/home/richard/anaconda3/bin/python
import os
import argparse
from pathlib import Path
import datetime
import soundfile


def getDuration(folder):
    sum = 0
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith('.wav'):
                samples, rate = soundfile.read(os.path.join(root, f))
                length = len(samples) / rate
                sum += (length)

                print("{}, {:.2f} sec".format(f, length))

    print(str(datetime.timedelta(seconds=sum)))


def main():
    parser = argparse.ArgumentParser(description="calculate wav durations under folder")
    parser.add_argument("dir", type=Path, default=os.getcwd(), nargs='?')
    args = parser.parse_args()

    folder = args.dir
    getDuration(folder)


if __name__ == "__main__":
    main()
