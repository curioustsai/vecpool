param(
     [Parameter()]
     [string]$datname
 )
 

 $scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
 $artifacts=$datname -replace ".dat", "_d2v.vec"
 $vecs=$datname -replace ".dat", ".vec"


Get-ChildItem $datname | ForEach-Object {FMSmartVecToDat.exe -d2v $_.fullname}
Get-ChildItem $artifacts | Rename-Item -NewName {$_.fullname -replace "_d2v", ""}
Get-ChildItem $vecs | ForEach-Object { python $scriptPath/pyvec/format.py -i $_ -o $_ }
