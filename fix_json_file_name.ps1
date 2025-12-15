# $items = @(2023, 2024, 2025, "ooo")

# Set the folder path (current folder in this example)
$folderPath = "C:\Users\Audrey\OneDrive\Pictures\Camera Roll\takeout-20250725T035235Z-1-001\2023"

$brokenfilename = 'supplementa', 's', 'supplem'


foreach ($name in $brokenfilename){
    Write-Host "[$name]"

    Get-ChildItem $folderPath -Recurse -File |
    Where-Object { $_.Name -like "*.$name.json*" } |
    ForEach-Object { 
        Write-Host "$($_.Name)"
        $newName = $_.Name -replace "\.$name\.json", ".supplemental-metadata.json"
        Write-Host "$($_.Name) will be renamed as $newName"
        Rename-Item $_.FullName -NewName $newName
    }
}

