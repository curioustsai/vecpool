## Download simulator
Please download SamSoft simulator.exe from [SharePoint](https://fortemediainc.sharepoint.com/sites/PCNB/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FPCNB%2FShared%20Documents%2FSimulator&viewid=aef52aae%2D12b8%2D469a%2Db96c%2De96b06ecf616)

- [SAMSoftV930_Simulator_v930_93981585_35978](https://fortemediainc.sharepoint.com/:u:/s/PCNB/EeljaVJ1dr5LjfUM7eX6LDEBdCGnVLZvVOxBp_ebKVW3eg?e=Js3pBB)
- [SAMSoftV920_Simulator_v920_v92_98_10_6x_win11](https://fortemediainc.sharepoint.com/:u:/s/PCNB/EQeGXSLyTBxLmtkexCzRhfkBgap2UjLl-Vha8s5UVvjlHQ?e=oCEPuX)

## Run simulation
1. Open "command window".
2. Change path by entering "cd C:\simulator" to this folder.
3. Entering "SAMSoftV920_Simulator_VS2012.exe ARGUMENTS ", according arguments are as followings.
4. "Processing XXX frame(s)" will show on screen.
5. Wait until"Program finished"
6. Processed out will be as defined name in "C:\simulator"

##  Argument setting
```
-c microphone number
-i input
-o output
-v param
-r reference
-S sampling rate(1=16k;4=32k)
-b beginning frame count (frames)
-f ending frame count (frames)

```

##  Sample

ex : 4ch, 32K32Bits
SAMSoftV920_Simulator_VS2012.exe -c4 -i cap_xxxxxx.wav -r ref_xxxxxx.wav -o lout_xxxxxx.wav -v mode3.vec -S 4

ex : 2ch, 32K32Bits
SAMSoftV920_Simulator_VS2012.exe -c2 -i cap_xxxxxx.wav -r ref_xxxxxx.wav -o lout_xxxxxx.wav -v mode3.vec -S 4

ex : 2ch, 16K32Bits
SAMSoftV920_Simulator_VS2012.exe -c2 -i cap_xxxxxx.wav -r ref_xxxxxx.wav -o lout_xxxxxx.wav -v mode3.vec -S 1
