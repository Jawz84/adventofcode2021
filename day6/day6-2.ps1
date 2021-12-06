$l = [int[]](Get-Content $PSScriptRoot\input.txt).trim().split(',')

$hash = @{}
foreach($i in $l) {
    $hash[$i] = $hash[$i] + 1
}

foreach ($day in 1..256) {
    # "after $day days"
    # 0..8 | foreach {
    #     "{0}  {1}" -f $_, $hash[$_]
    # }
    # "---"*6
    $temp0 = $hash[0]
    $temp8 = $hash[8]
    $hash[0] = $hash[1]
    $hash[1] = $hash[2]
    $hash[2] = $hash[3]
    $hash[3] = $hash[4]
    $hash[4] = $hash[5]
    $hash[5] = $hash[6]
    $hash[6] = $hash[7]
    $hash[7] = $temp8
    $hash[8] = $temp0

    $hash[6] = $hash[6] + $temp0
}

$sum = 0
foreach ($i in 0..8) {
    $sum += $hash[$i]
}
$sum