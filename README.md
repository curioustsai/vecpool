# VecPool
This repo keep track of vec files and keep everyone on the same pages.

## Project Structure
- Parameters: keep track of vec files from all projects. Don't keep *.dat file, which is binary. Use `FMSmartVecToDat` to convert.
- Simulator: the directory where your put simulator
- Utils: some useful tool for vec format, convert, etc.

## Parameters
- Pool of project *.vec files
```
├───HP
│   ├───HP_2023
│   ├───HP_2023GNA
│   └───HP_2024
│       └───reference_930
└───Lenovo
```

## Utils
* FMSmartVecToDat.exe: Convertor between *.vec and *.dat files
* pyvec: python utils
  * clipboard: extract/merge mode from whole vec file
  * editor: batch editing for vec files. `No more hands on efforts`. Refer to `editor.cfgx` for more details.
  * format: sort vec parameters. (MPO cases are taken in consideration. Duplicated key will be put at the end of file.)
  * validator: validate vec files with *.cfgx. Refer to `valdiator.cfgx` for details.
* drc_curve: draw a drc curve from command line arguments
* qconvertor: a python script to conver hex, floating number, dB value.
* FMConvertor: a python script to batch convert d2v/v2d and sort parameters.
