# Windows Powershell code used to format the daily logs. They were also used to format lecture notes for the classes 
# I took in university during that time of year;

# $refday calculates the difference of days between April 1, 2025 to current day.
# Modified from the original code that was used on Septermber 24, 2025.

Clear-Host

$targetDate = Get-Date "April 1, 2025"
$today = Get-Date
$refday_num = ($targetDate-$today).Days
$refday = (Get-Date).AddDays($refday_num).ToString("dddd, MMMM d, yyyy")

Write-Output($refday_num, "`n")

for ($i = $refday_num; $i -lt $refday_num+57; $i += 7) {

    $TIM170 = "`n3:20PM - 4:55PM`n• Professor Subhas Desa mentioned the following topics in the TIM 170 lecture;"
    $ECE118 = "`n11:40AM - 1:15PM`n• Today, Professor Tae Myung Huh went over these things in the ECE 118 lecture;"
    $endofDay = "`n--------------------`n`n"

    # $i + 1 is a Tuesday.
    (Get-Date).AddDays($i + 0).ToString("dddd, MMMM d, yyyy"); "$ECE118$endofDay";
    (Get-Date).AddDays($i + 1).ToString("dddd, MMMM d, yyyy"); "$endofDay";
    (Get-Date).AddDays($i + 2).ToString("dddd, MMMM d, yyyy"); "$ECE118$TIM170$endofDay";
    (Get-Date).AddDays($i + 3).ToString("dddd, MMMM d, yyyy"); "$endofDay";
    (Get-Date).AddDays($i + 4).ToString("dddd, MMMM d, yyyy"); "$endofDay";
    (Get-Date).AddDays($i + 5).ToString("dddd, MMMM d, yyyy"); "$endofDay";
    (Get-Date).AddDays($i + 6).ToString("dddd, MMMM d, yyyy"); "$endofDay";
}
