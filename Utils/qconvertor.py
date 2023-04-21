import argparse
from numpy import log10, power


if __name__ == "__main__":
    description = "Convert among hex, float value, db value based on Qformat\n"
    argpars = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    argpars.add_argument("--value", "-v", required=True, default="", type=str)
    argpars.add_argument("--mode", "-m", required=True, choices=["h2f", "h2d", "f2d", "f2h", "d2f", "d2h"],
                         help="abbreviation, h: hex, f: float, d: dB")
    argpars.add_argument("--qformat", "-q", default=15, type=int, help="int, default is set to 15")
    argv = argpars.parse_args()
    mode = argv.mode
    value = argv.value
    qformat = argv.qformat
    qbase = 2 ** qformat

    if mode.startswith('h'):
        if not value.startswith('0x0'):
            value = '0x{}'.format(value)

        value = int(value, 16) / qbase
        if mode == "h2f":
            print("{:.2f}".format(value))
        elif mode == "h2d":
            db_value = 20 * log10(value)
            print("{:.2f} dB".format(db_value))

    elif mode.startswith('f'):
        if mode == "f2h":
            value = int(round(float(value) * qbase))
            print("{:X}".format(value))
        elif mode == "f2d":
            value = 20 * log10(value)
            print("{:.2f} dB".format(value))

    elif mode.startswith('d'):
        value = power(10, float(value) / 20)
        if mode == 'd2f':
            print("{:.2f}".format(value))
        elif mode == "d2h":
            hex_value = int(round(value * qbase))
            print("{:X}".format(hex_value))
