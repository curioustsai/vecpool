# HP projects
- Conference Mode (0x1)
- Personal Mode (0x3)
- Conference Mode with VDNA (0x0A)
- Personal Mode with VDNA (0x0D)
- Enroll Mode (0xE)

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

