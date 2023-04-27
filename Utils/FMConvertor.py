import argparse
import os
import subprocess
import shutil
from pyvec.format import VecFormat


def converter(package, mode, sort):
    rootdir = os.path.join(os.path.dirname(__file__), '..')
    workdir = os.path.join(rootdir, 'Parameters', 'HP')
    packages = os.listdir(workdir)

    if package not in packages:
        print("Invalid specified package: {}".format(package))
        return

    package_path = os.path.join(workdir, package)
    for f in os.listdir(package_path):
        if f.lower().startswith("sam"):
            if mode == "d2v":
                ext = ".dat"
                suffix = "_d2v.vec"
                ext_new = ".vec"
            else:
                ext = ".vec"
                suffix = "_v2d.dat"
                ext_new = ".dat"

            filepath = os.path.join(package_path, f)
            temppath = filepath.replace(ext, suffix)
            finalpath = filepath.replace(ext, ext_new)

            cmd = ["FMSmartVecToDat.exe", '-' + mode, filepath]
            subprocess.call(cmd)
            shutil.move(temppath, finalpath)

            if mode == "d2v" and sort:
                format = VecFormat()
                format.read(finalpath)
                format.sort()
                format.write(finalpath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract vec from whql zip")
    parser.add_argument("--pack", "-p", required=True, type=str, help="package name in Paramet/HP")
    parser.add_argument("--mode", "-m", required=True, choices=["d2v", "v2d"])
    parser.add_argument("--sort", type=bool, default=True)

    args = parser.parse_args()
    converter(args.pack, args.mode, args.sort)
