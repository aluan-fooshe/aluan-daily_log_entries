$dirpath = "C:\Users\Audrey\OneDrive\Pictures\Camera Roll\takeout-20250725T035235Z-1-001"

$dirpath = "C:\Users\folder"

$items = @(2023, 2024, 2025, "ooo")
$json_files = @()
$pair_files = @()
$i = 0

ForEach ($item in $items){
    $currpath = "$dirpath\$item"
    if (-not (Test-Path $currpath)) {
        Write-Host 'File [$item] does not exist.'
    } else {
        Write-Host "Directory: $currpath"
        $json_files += Get-ChildItem -File -Name -Path $currpath -Filter "*.json"
        $pair_files += Get-ChildItem -File -Name -Path $currpath -Exclude "*.json"
    }
   
}


# i and j increment for array counting if one array is off compared to the other.
# array1 = @(1, 2, 3, 4, 5, 6, 8, 10, 11, 12)
# array2 = @(2, 3, 4, 5, 6, 7, 8, 10, 11, 12)
# -eq -> equality

$i = 0
$j = 0
for ($i = 0; $i -lt $pair_files.Count){
    if (-not ($pair_files[$i] -eq $json_files[$j])){
        Write-Output "NOT EQUAL File: $($pair_files[$i])`t`t$($json_files[$j])"
        $j++
    } else {
        Write-Output "EQUAL File: $($pair_files[$i])`t`t$($json_files[$i])"
        $i++
    }
}

