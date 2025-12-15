# $items = @(2023, 2024, 2025, "ooo")

# Set the folder path (current folder in this example)
$folderPath = "C:\Users\Audrey\OneDrive\Pictures\Camera Roll\takeout-20250725T035235Z-1-001\2023"


# Get all non-JSON files in the folder
$nonJsonFiles = Get-ChildItem -Path $folderPath -File | Where-Object { $_.Extension -ne ".json" }

# Counter for total files matched with its .json counterpart.
$matchedFiles = 0

foreach ($file in $nonJsonFiles) {
    # Construct the expected JSON file name
    $jsonFileName = "$($file).supplemental-metadata.json"
    
    # Check if the JSON file exists in the same folder
    $jsonFilePath = Join-Path -Path $folderPath -ChildPath $jsonFileName
    if (Test-Path $jsonFilePath) {
        Write-Output "Match found: $($file.Name) has corresponding JSON: $jsonFileName"
        $matchedFiles++
    } else {
        Write-Output "No JSON match for: $($file.Name)`n`t`t`t`t   $jsonFileName."
    }
}
# needs to account for these edge cases;
# No JSON match for: Screenshot_299.png
#				     Screenshot_299.PNG.supplem
#
# No JSON match for: Screenshot_299.jpg
#				     Screenshot_299.JPG.supplemental-metada

# Optional: Output Summary
$totalFiles = $nonJsonFiles.Count
# $matchedFiles = ($nonJsonFiles | Where-Object { Test-Path (Join-Path $folderPath "$($_.BaseName).json") }).Count
Write-Output "`nSummary: $matchedFiles out of $totalFiles non-JSON files have a corresponding JSON file."