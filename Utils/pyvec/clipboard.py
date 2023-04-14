from format import VecFormat
from os.path import exists
import argparse

version = "1.0.0"


class VecClipBoard(VecFormat):
    def __init__(self):
        VecFormat.__init__(self)
        # super.__init__()

    def extract(self, in_vfile, modes, out_vfile):
        self.read(in_vfile)
        data = dict()
        for m in modes:
            key = "MODE " + str(m)
            data[key] = self.data[key]

        output_file = open(out_vfile, "w")
        output_file.write(self.headings)
        output_file.write("\n")

        for mode, vec in data.items():
            output_file.write("#SEGMENT SEGMENT_SIZE 0 {}\n\n#PARAMS\n".format(mode))

            for key, value in vec.items():
                value = "{0:#0{1}X}".format(value, 6)[2:]
                if key.startswith('m'):
                    key = key[-4:]  # remove subffix of duplicate address
                output_file.write("{} {}\n".format(key, value))

            output_file.write("\n")
        output_file.close()

    def merge(self, org, params, output):
        org_format = VecFormat()
        param_format = VecFormat()
        org_format.read(org)
        param_format.read(params)

        for mode in param_format.data.keys():
            org_format.data[mode] = param_format.data[mode]
        org_format.write(output)


if __name__ == "__main__":
    usage_extract = "Extract Mode: specify input vec, mode, output vec to extract param."
    usage_merge = "Merge Mode: specify input vec, param vec, output. Paste param vec onto input vec as output vec."
    description = "VecClipBoard {}.\n\n{}\n{}".format(version, usage_extract, usage_merge)
    argpars = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    argpars.add_argument("--input", "-i", default="", type=str)
    argpars.add_argument("--output", "-o", default="", type=str)
    argpars.add_argument("--param", "-p", default="", type=str)
    argpars.add_argument("--mode", "-m", nargs="+", type=int)
    args = argpars.parse_args()

    if not exists(args.input):
        print("input file doesn't exist")
        exit()

    clipboard = VecClipBoard()

    if args.param:
        clipboard.merge(args.input, args.param, args.output)
    else:
        clipboard.extract(args.input, args.mode, args.output)
