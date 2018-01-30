<#  
.SYNOPSIS  
    PowerShell function to count number of instances of critical, high, and medium severity nessus findings       
.DESCRIPTION  
    Takes a filepath for a Nessus CSV file
.NOTES   
    Author: jakx_
.EXAMPLE  
    count .\nessus.csv
#>

function count()
{
	Param (
		[ValidateScript({Test-Path $_})]
		[string]$csvfile
	)
	
	#import csv
	$impcsv = import-csv $csvfile
	
	#define risks we care about
	$risks = @("Critical","High","Medium")
	
	foreach ($risk in $risks){
		$count = $impcsv | select -unique risk, "plugin id" | where risk -eq $risk | measure-object | select -expandproperty count
		$props += @{
		$risk = $count
		}
	}
	$obj = @(new-object pscustomobject -Property $props)
	$obj
}
	