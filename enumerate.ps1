#This is a Powershell script that enumerates avaliable Window$ shares and dumps them to a file called shares.txt.
#Written by jakx
#Usage: ./enumerate.ps1

echo "Fetching IP's.."
ipconfig | select-string "ipv4"
$ip= Read-Host 'Enter the IP you want to use'
$subnet=$ip | foreach {$_.split(".")[-4,-3,-2]-join "."}
$valid= 1..255 | % {$ip2=$subnet + "." + $_; "$ip2 : $(Test-Connection -count 1 -comp $ip2 -quiet)"} | select-string "true"
$clean= $valid | foreach-object {$_.tostring()} | foreach-object {$_.split(":")} | select-string "[0-9]."
$clean2= $clean | foreach-object {$_.tostring()} | foreach-object {$_.trim()}
$clean2 | foreach-object{ echo "..$_" ; Get-WmiObject -class win32_share -computer $_ } > shares.txt

