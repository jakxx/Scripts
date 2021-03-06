function Hash($textToHash)
<#  
.SYNOPSIS  
    PowerShell function to generate/retrieve unique local administrator passwords.        
.DESCRIPTION  
    Takes an MD5 hash of a (optional) unique string, a hardcoded string, and the hostname in which
    the function is run on.
.NOTES   
    Author: jakx_
.EXAMPLE  
    hash testing  
#>
{
	$hostname = hostname

	$s = "foobar"

	$new = "$hostname" + "$s" + "$texttoHash"

	$hashme = new-object System.Security.Cryptography.MD5CryptoServiceProvider

	$tohash = [System.Text.Encoding]::UTF8.GetBytes($new)

	$ByteArray = $hashme.ComputeHash($tohash)

	foreach($byte in $ByteArray)

	{

		$pass += $byte.ToString()

	}

	return $pass;

}
