# Benchmark Tools
The package of `Benchmark Tools` is a collection of useful audio tools that help your experiment smooth.

**Version: 1.0.0**

## Installation
Please install required package first
```
pip install -r requirement.txt
```

# Tools
Note: if you don't know how use each tool, please execute `python <script name> -h`

## 1. Align

### Align single input file with target file

```
python align_wavfiles.py --target_file .\examples\benchmark_snr\clean\SPEECHDT_602_Female_one_44100Hz.wav --input_file .\examples\benchmark_snr\dut\dut.wav --output_file .\aligned.wav
```

### Batch align the input folder with target file

* Windows:
```
python align_wavfiles.py --target_file=".\source_file\Dyna-Src_P835_4_sentences_4convergence_16000Hz.wav" --batch_input_folder="\path\to\input_folder" --batch_output_folder="\path\to\output_folder"
```

## 2. Root Mean Square (RMS)
usage: rms [-h] [-v] [-f FRAME_SIZE] file [file ...]

Calculate the rms for the entire wave file
---
```
python rms examples\benchmark_erle\DoubleTestSignal-far_end_44100.wav
```
* result:
```
[rms] examples/benchmark_erle/DoubleTestSignal-far end_44100.wav: -23.759493494843756
```

Visualize the rms versus time
---
* Windows:
```
python rms -v examples\benchmark_erle\DoubleTestSignal-far_end_44100.wav
```

Visualize the rms versus time (Multiple soundfile at a time)
---
```
python rms -v examples\benchmark_erle\DoubleTestSignal-far_end_44100.wav examples\benchmark_erle\DoubleTestSignal-near_end_44100.wav
```
