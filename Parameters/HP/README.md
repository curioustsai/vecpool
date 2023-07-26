# HP projects
- Earphone (Mode 0)
- Conference Mode (Mode 1)
- Personal Mode (Mode 3)
- Conference Mode with VDNA (Mode 10)
- Personal Mode with VDNA (Mode 13)
- Enroll Mode (Mode 14)
- Cortana (Mode 19)

## GNA/CPU dll switch
Uplink:
Reg 0x00FE = 0x0092, load fmaudvf.dll (cpu version dll)
Reg 0x00FE = 0x1092, load fmausvfa.dll (gna version dll)

Downlink:
Reg 0x40FE = 0x4092, load fmaudvf.dll (cpu version dll)
Reg 0x40FE = 0x5092, load fmausvfa.dll (gna version dll)

It can check uplink cpu or gna lib using parameter 0x00EC
GNA lib : parameter 0x00EC = 0x1
CPU lib : parameter 0x00EC = 0x0

## Version Number:
- key (0x75) of all mode by George

## HP_2023(GNA) General requirement
- Conference mode: 0x081F
- Personal mode: 0xA0F

