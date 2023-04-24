from format import VecFormat
import os
import argparse
from glob import glob

version = "1.0.0"


class VecEditor(VecFormat):
    def __init__(self, workdir, packages, input, output, config):
        VecFormat.__init__(self)
        self.input = input
        self.output = output
        self.config = config
        self.actions = []
        self.workdir = workdir
        self.package_list = packages

    def run(self):
        if self.config.endswith("cfg"):
            self.read(self.input)
            self.apply_cfg(self.config)
            self.write(self.output)

        elif self.config.endswith("cfgx"):
            # inplace overwrite
            self.apply_cfgx(self.config)

    def parse_cfg(self, cfg_path):
        if not cfg_path.endswith(".cfg"):
            print("Not support format, please use .cfg")
            return False

        config = open(cfg_path, "r")

        for line in config.readlines():
            if line.startswith("#") or line.strip() == "":
                continue
            else:
                entries = line.split(',')
                if len(entries) == 3:
                    entry = {
                        "mode": entries[0].strip().upper(),
                        "key": entries[1].strip().upper(),
                        "value": entries[2].strip().upper()
                        }
                    self.actions.append(entry)
                elif len(entries) == 4:
                    entry = {
                        "mode": entries[0].strip().upper(),
                        "key": entries[1].strip().upper(),
                        "act": entries[2].strip(),
                        "bitoffset": entries[3].strip()
                        }
                    self.actions.append(entry)

        config.close()
        return True

    def parse_cfgx(self, cfg_path):
        if not cfg_path.endswith(".cfgx"):
            print("Not support format, please use .cfgx")
            return False

        config = open(cfg_path, "r")

        for line in config.readlines():
            if line.startswith("#") or line.strip() == "":
                continue
            else:
                entries = line.split(',')
                if len(entries) == 4:
                    entry = {
                        "ssid": entries[0].strip(),
                        "mode": entries[1].strip().upper(),
                        "key": entries[2].strip().upper(),
                        "value": entries[3].strip().upper()
                        }
                    self.actions.append(entry)
                elif len(entries) == 5:
                    entry = {
                        "ssid": entries[0].strip(),
                        "mode": entries[1].strip().upper(),
                        "key": entries[2].strip().upper(),
                        "act": entries[3].strip(),
                        "bitoffset": entries[4].strip()
                        }
                    self.actions.append(entry)

        config.close()
        return True

    def execute_action(self, act):
        if len(act) == 3:
            if act["mode"] == "*":
                mode_list = self.data.keys()
            else:
                mode_list = ["MODE {}".format(act["mode"])]

            for mode in mode_list:
                key = act["key"]
                value = act["value"]
                self.data[mode][key] = int(value, 16)

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

                    if action.lower() == 'set':
                        value = value | (1 << bitoffset)
                    elif action.lower() == 'clear':
                        value = value & ~(1 << bitoffset)
                    elif action.lower() == 'toggle':
                        value = value ^ (1 << bitoffset)

                    self.data[mode][key] = value
                else:
                    if action.lower() == 'set' or action.lower() == 'toggle':
                        self.data[mode][key] = (1 << bitoffset)

    def apply_cfg(self, cfg_path):
        if not self.parse_cfg(cfg_path):
            return False

        for act in self.actions:
            self.execute_action(act)

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
                self.read(vec_file)
                self.execute_action(act)
                self.write(vec_file)


if __name__ == "__main__":
    description = "VecEditor {}".format(version)
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

    editor = VecEditor(workdir, packages, input, output, config)
    editor.run()
