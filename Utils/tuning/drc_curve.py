import argparse
import numpy as np
import matplotlib.pyplot as plt

eps = 1e-12


def dB2lin(value):
    return pow(10.0, 0.05 * value)


def lin2dB(value):
    return 20.0 * np.log10(value + eps)


def hexifydb(value):
    qbase = 2 ** 15
    value = np.power(10, float(value) / 20)
    hex_value = int(round(value * qbase))

    return hex_value


def hexify(value):
    qbase = 2 ** 15
    hex_value = int(round(value * qbase))

    return hex_value


def compute(x, th1_linear, slop1, th2_linear, slop2):
    if x < th1_linear:
        y = x
    else:
        # compressor 1
        if x < th2_linear:
            gain = th1_linear / (th1_linear + (x - th1_linear) * slop1)
        # compressor 2 (aggressive)
        else:
            drc_th22 = th1_linear / (th1_linear + (th2_linear - th1_linear) * slop1) * th2_linear
            gain = drc_th22 / (th2_linear + (x - th2_linear) * slop2)

        y = x * gain
    return y


def plot_figure(threshold1=-24.0, slop1=0.1, threshold2=-12.0, slop2=0.2):
    # caculate marker point
    th1_linear = dB2lin(threshold1)
    th2_linear = dB2lin(threshold2)
    th1_y = compute(th1_linear, th1_linear, slop1, th2_linear, slop2)
    th2_y = compute(th2_linear, th1_linear, slop1, th2_linear, slop2)
    origin_y = compute(1.0, th1_linear, slop1, th2_linear, slop2)

    th1_ydB = lin2dB(th1_y)
    th2_ydB = lin2dB(th2_y)
    origin_ydB = lin2dB(origin_y)

    plt.annotate("[Th1] x: {:2.2f}, y:{:2.2f}".format(threshold1, th1_ydB), (threshold1, th1_ydB))
    plt.annotate("[Th2] x: {:2.2f}, y:{:2.2f}".format(threshold2, th2_ydB), (threshold2, th2_ydB))
    plt.annotate("[Org] x: {:2.2f}, y:{:2.2f}".format(0, origin_ydB), (0, origin_ydB))

    # calulate curve
    x_dB = np.arange(-96, 1, 1, dtype=float)
    x_linear = [dB2lin(x) for x in x_dB]
    y_linear = [compute(x, th1_linear, slop1, th2_linear, slop2) for x in x_linear]
    y_dB = [lin2dB(y) for y in y_linear]

    dBFS_max = 6
    dBFS_min = -66

    plt.rcParams["figure.figsize"] = (18, 14.4)
    plt.plot(x_dB, y_dB)
    plt.xlim([dBFS_min, dBFS_max])
    plt.xlabel("input dBFS")
    plt.xticks(np.arange(dBFS_min, dBFS_max, 3))

    plt.ylim([dBFS_min, dBFS_max])
    plt.ylabel("output dBFS")
    plt.yticks(np.arange(dBFS_min, dBFS_max, 3))

    # reference line
    plt.plot(x_dB, x_dB, 'r--')

    plt.title("Dynamic Range Compressor\n"
              "threshold1: {:2.2f}, threshold2 {:2.2f}\n"
              "slop1: {:2.2f}, slop2: {:2.2f}".format(
                  threshold1, threshold2, slop1, slop2))
    description = "threshold1: {0:#0{1}x}\n".format(hexifydb(threshold1), 6)
    description += "threshold2: {0:#0{1}x}\n".format(hexifydb(threshold2), 6)
    description += "slop1: {0:#0{1}x}\n".format(hexify(slop1), 6)
    description += "slop2: {0:#0{1}x}".format(hexify(slop2), 6)
    plt.text(dBFS_min, -3, description, bbox=dict(boxstyle="square,pad=0.1", ec="lightblue"))
    plt.grid()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Dynamic Range Compressor Curve")
    parser.add_argument("--threshold1", type=float, default=-24.0)
    parser.add_argument("--slop1", type=float, default=0.1)
    parser.add_argument("--threshold2", type=float, default=-12.0)
    parser.add_argument("--slop2", type=float, default=0.2)

    args = parser.parse_args()
    threshold1 = args.threshold1
    slop1 = args.slop1
    threshold2 = args.threshold2
    slop2 = args.slop2

    plot_figure(threshold1, slop1, threshold2, slop2)


if __name__ == "__main__":
    main()
