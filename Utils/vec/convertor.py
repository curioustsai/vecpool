import argparse
import subprocess
import shutil
from glob import glob
from .format import VecFormat


def convert(pattern):
    for f in glob(pattern):
        if f.endswith('.dat'):
            mode = 'd2v'
            ext = ".dat"
            suffix = "_d2v.vec"
            ext_new = ".vec"
        elif f.endswith('.vec'):
            mode = 'v2d'
            ext = ".vec"
            suffix = "_v2d.dat"
            ext_new = ".dat"
        else:
            print("supposed to be dat/vec files")
            return

        filepath = f
        temppath = filepath.replace(ext, suffix)
        finalpath = filepath.replace(ext, ext_new)

        cmd = ["FMSmartVecToDat.exe", '-' + mode, filepath]
        subprocess.call(cmd)
        shutil.move(temppath, finalpath)

        if f.endswith('.dat'):
            format = VecFormat()
            format.read(finalpath)
            format.sort()
            format.write(finalpath)


def main():
    parser = argparse.ArgumentParser(description="FM vec/dat convertor")
    parser.add_argument("pattern", nargs='+')
    args = parser.parse_args()

    for pattern in args.pattern:
        convert(pattern)


if __name__ == "__main__":
    main()
