param(
     [Parameter()]
     [string]$whql_folder,

     [Parameter()]
     [string]$dest
 )

Get-ChildItem "$whql_folder\sam*.dat" | ForEach-Object {FMSmartVecToDat.exe -d2v $_.fullname}
Get-ChildItem "$whql_folder\sam*.vec" | Rename-Item -NewName {$_.fullname -replace "_d2v", ""}
Get-ChildItem "$whql_folder\sam*.vec" | ForEach-Object {
  $filename=$dest + $_.basename + ".vec"
  python .\Utils\pyvec\format.py -i $_.fullname -o $filename
  }
