# Introduction
A vec pool for keep track of all PCNB vec for all projects

# Usage
- Use FMSmartVecToDat to convert vec and dat. Vec files are text and dat files are binary. In this repo, we only track vec files.
- Under the root of working directory, `python Utils\pyvec\format -i <input_vec> -o <output_vec>` to sort your vec file.

## Parmaeter
- Pool of project *.vec files
```
├───HP
│   ├───HP_2023
│   ├───HP_2023GNA
│   └───HP_2024
│       └───reference_930
└───Lenovo
```

## Simulator
- Vec should match with the simulator. So, keep track of simulator as well. Put simulator on the SharePoint. Point by link.

## Utilities
- FMSmartVecToDat.exe: Convertor between *.vec and *.dat files
- pyvec: python utils
 - clipboard: extract/merge mode from whole vec file
 - editor: batch process for editing vec file
 - format: sort vec parameters
 - validator: validate vec files with *.cfgx. Refer to valdiator.cfgx for details.
