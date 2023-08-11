from .editor import VecEditor
import os
import argparse

version = "1.0.0"


class Validator(VecEditor):
    def __init__(self, workdir, packages, input, output, config):
        super().__init__(workdir, packages, input, output, config)

    def execute_action(self, act):
        status = True
        if len(act) == 3:
            if act["mode"] == "*":
                mode_list = self.data.keys()
            else:
                mode_list = ["MODE {}".format(act["mode"])]

            for mode in mode_list:
                key = act["key"]
                value = act["value"]
                if key in self.data[mode]:
                    if self.data[mode][key] != int(value, 16):
                        print("Eror: [{}] key: {}, {:X} != {}".format(mode, key, self.data[mode][key], value))
                        status = False
                else:
                    print("Warning: [{}] key: {} doesn't exist. Check its default value".format(mode, key))
                    status = False
        elif len(act) == 4:
            if act["mode"] == "*":
                mode_list = self.data.keys()
            else:
                mode_list = ["MODE {}".format(act["mode"])]

            for mode in mode_list:
                key = act["key"]
                action = act["act"]
                bitoffset = int(act["bitoffset"])

                if key in self.data[mode]:
                    value = self.data[mode][key]
                    value = (value >> bitoffset) & 1

                    if action.lower() == 'enable' and (value != 1):
                        print("Error: [{}] key: {}, bit: {} should be enabled".format(mode, key, bitoffset))
                        status = False
                    elif action.lower() == 'disable' and (value != 0):
                        print("Error: [{}] key: {}, bit: {} should be disabled".format(mode, key, bitoffset))
                        status = False
                else:
                    print("Warning: [{}] key: {} doesn't exist. Check its default value".format(mode, key))
                    status = False
        return status

    def run(self):
        if self.config.endswith("cfg"):
            self.read(self.input)
            self.apply_cfg(self.config)
            self.write(self.output)

        elif self.config.endswith("cfgx"):
            # inplace overwrite
            self.apply_cfgx(self.config, False)


def main():
    description = "Validatoer {}".format(version)
    argpars = argparse.ArgumentParser(description=description)
    argpars.add_argument("--input", "-i", default="", type=str)
    argpars.add_argument("--output", "-o", default="", type=str)
    argpars.add_argument("--config", "-c", required=True, help="*.cfg or *.cfgx")
    argpars.add_argument("--customer", default="hp", choices=['hp', 'lenovo'],
                         help="vec root directory of your project")
    parse_value = argpars.parse_args()

    input = parse_value.input
    output = parse_value.output
    config = parse_value.config
    customer = parse_value.customer
    # Customer except HP are NIY
    rootdir = os.path.join(os.path.dirname(__file__), '..', '..')
    workdir = os.path.join(rootdir, 'Parameters', 'HP')
    packages = os.listdir(os.path.join(workdir))

    # Not Implement Yet (NIY)
    # if parse_value.customer == "hp":
    # elif parse_value.customer == "lenovo":
    #     workdir = os.path.join(rootdir, 'Parameters', 'Lenovo')

    validator = Validator(workdir, packages, input, output, config)
    validator.run()


if __name__ == "__main__":
    main()
