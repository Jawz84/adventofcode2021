# Browse to adventofcode.com, log in using your preferred auth method.
# Open your browsers development tools, and find the Cookie named 'session'.
# For Chrome / Edge that is: F12 > Application > Storage > Cookies > https://adventofcode.com > session
# Store its value in a file named Cookie in the same folder as this script.
$sessionCookie = Get-Content .\Cookie

$ErrorActionPreference = 'stop'

if ([string]::IsNullOrEmpty($sessionCookie)) {
    Write-Error "Please save the value of the 'session' cookie from your browser and store it in a file named 'Cookie' in this directory. More info in the comments of this script."
}

$date = Get-Date
$year = $date.Year
$day = $date.Day
$month = $date.Month
$fileTemplate = @'
import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

'@


#region functions
function TryGrabAndSaveInput {
    param(
        $Year,
        $Day
    )

    $fileName = GetDayPath -Day $Day -FileName "input.txt"

    if (Test-Path $fileName) {
        if (-not [string]::IsNullOrEmpty((Get-Content $fileName))) {
            Write-Host "Found puzzle input in file for day '$day', no need to grab from url."
            return
        }
    }

    $uri = "$baseUrl/$year/day/$day/input"
    try {
        $in = Invoke-RestMethod -Uri $uri -Headers @{cookie = "session=$sessionCookie"} -ErrorAction stop
        $null = Set-Content -Path $fileName -value $in -ErrorAction stop
        Write-Host "Grabbed puzzle input for day '$day' from url."
    }
    catch {
        Write-Error "Unable to grab and save puzzle input for day '$day' of '$Year'. Error message: `n$($_.Exception.Message)"
    }
}

function GetDayPath {
    param(
        $Day,
        $FileName
    )

    $path = Join-Path -Path $pwd -ChildPath "day$day"
    if ($FileName) {
        Join-Path -Path $path -ChildPath $FileName
    }
    else {
        $path
    }
}

function Setup {
    Write-Host "Setting up default folders and files for each puzzle."
    for ($i = 1; $i -le 25; $i++) {
        $day = "day$i"

        $folderToCreate = GetDayPath -Day $i
        $null = New-Item -Path $folderToCreate -ItemType Directory -ErrorAction SilentlyContinue

        "$day-1.py", "$day-2.py", "input.txt", "exampleinput.txt" | 
            ForEach-Object { 
                $filePath = GetDayPath -Day $i -FileName $_
                $null = New-Item -Path $filePath -ItemType File -ErrorAction SilentlyContinue
            }

        $puzzle1script = GetDayPath -Day $i -FileName "$day-1.py"
        $fileContent = Get-Content $puzzle1script

        if ([string]::IsNullOrEmpty($fileContent)) {
            $null = Set-Content -Path $puzzle1script -Value ("# $baseUrl/$year/day/$i `n`n" + $fileTemplate)
        }
    }
}

#endregion functions

if ($month -lt 12) {
    $year = $year -1
    $days = 1..25
    Write-Warning "Fetching puzzle input for last year: $year, days 1-25."
}
else {
    $days = 1..$day
    Write-Host "Fetching puzzle input for $year, days 1-$day."
}

$parentDirectoryName = (Split-Path $pwd -Leaf)
if ($parentDirectoryName -notmatch "^adventofcode$year$") {
    Write-Error "Parent dir must be named 'adventofcode$year'."
}

$baseUrl = "https://adventofcode.com"

if (-not (Test-Path (GetDayPath -Day 25))) {
    Setup
}

foreach ($d in $days) {
    TryGrabAndSaveInput -year $year -Day $d
}

code "$(GetDayPath -day $day)\day$day-1.py"
Set-Location  "$(GetDayPath -day $day)\"
start-process -path "$baseUrl/$year/day/$day"