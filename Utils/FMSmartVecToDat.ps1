param(
    [Parameter(Mandatory)]
    [ValidateSet('d2v', 'v2d')]
    [string]$mode,

    [Parameter(Mandatory)]
    [string]$filename
    )

$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition

if ($mode -eq 'd2v') {
  $artifacts=$filename -replace ".dat", "_d2v.vec"

  Get-ChildItem $filename | ForEach-Object {FMSmartVecToDat.exe -d2v $_.fullname}
  Get-ChildItem $artifacts | ForEach-Object { python $scriptPath/pyvec/format.py -i $_ -o $_ }
  Get-ChildItem $artifacts | ForEach-Object {
    $newname = $_.fullname -replace '_d2v.vec', '.vec'
    if (Test-Path -Path $newname) { Remove-Item -Path $newname }
    Rename-Item -Path $_.FullName -NewName $newname
    }

} elseif ($mode -eq 'v2d') {
  $artifacts=$filename -replace ".vec", "_v2d.dat"

  Get-ChildItem $filename | ForEach-Object {FMSmartVecToDat.exe -v2d $_.fullname}
  Get-ChildItem $artifacts | ForEach-Object {
    $newname = $_.fullname -replace '_v2d.dat', '.dat'
    if (Test-Path -Path $newname) { Remove-Item -Path $newname }
    Rename-Item -Path $_.FullName -NewName $newname
    }
}
