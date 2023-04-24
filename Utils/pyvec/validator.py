from editor import VecEditor
from glob import glob
import os
import argparse

version = "1.0.0"


class Validator(VecEditor):
    def __init__(self, workdir, packages, input, output, config):
        super().__init__(workdir, packages, input, output, config)

    def execute_action(self, act):
        if len(act) == 3:
            if act["mode"] == "*":
                mode_list = self.data.keys()
            else:
                mode_list = ["MODE {}".format(act["mode"])]

            for mode in mode_list:
                key = act["key"]
                value = act["value"]
                if self.data[mode][key] != int(value, 16):
                    print("Eror: [{}] key: {}, {:X} != {}".format(mode, key, self.data[mode][key], value))

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

                    if action.lower() == 'enable':
                        value = value & (1 << bitoffset)
                        if (value != 1):
                            print("Error: [{}] key: {}, should be enable".format(mode, key))
                    elif action.lower() == 'disable':
                        value = value & (1 << bitoffset)
                        if (value != 0):
                            print("Error: [{}] key: {}, should be disable".format(mode, key))
                else:
                    print("Error: {} {} doesn't specify".format(mode, key))

    def apply_cfgx(self, cfg_path):
        if not self.parse_cfgx(cfg_path):
            return False

        vec_list = []
        for act in self.actions:
            ssid = act["ssid"]
            if ssid in self.package_list:
                pack = ssid
                ssid = "*.vec"
                pattern = os.path.join(self.workdir, pack, ssid)
            elif ssid == "*":
                pack = "*"
                ssid = "*.vec"
                pattern = os.path.join(self.workdir, pack, ssid)
            elif '\\' in ssid:
                ssid = ssid + ".vec"
                pattern = os.path.join(self.workdir, ssid)
            else:
                pack = "*"
                ssid = ssid + ".vec"
                pattern = os.path.join(self.workdir, pack, ssid)

            vec_list = glob(pattern)
            if len(vec_list) == 0:
                print("cannot match any file")
                continue

            del (act["ssid"])

            for vec_file in vec_list:
                print(vec_file)
                self.read(vec_file)
                self.execute_action(act)


if __name__ == "__main__":
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
    packages = ["HP_890", "HP_920", "HP_920GNA", "HP_2023", "HP_2023GNA"]

    # Not Implement Yet (NIY)
    # if parse_value.customer == "hp":
    # elif parse_value.customer == "lenovo":
    #     workdir = os.path.join(rootdir, 'Parameters', 'Lenovo')

    validator = Validator(workdir, packages, input, output, config)
    validator.run()
