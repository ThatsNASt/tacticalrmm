$x = Get-WMIObject -Namespace "root/CIMV2/Security/MicrosoftVolumeEncryption" -query "SELECT * FROM Win32_EncryptableVolume WHERE DriveLetter='C:'";
$y = $x.GetProtectionStatus().ProtectionStatus
	if ($y -eq 1) {
		Write-Host "OK"; exit 0
	}
	else {
		Write-Host "FAIL $y"; exit 1
	}