## Write-Host "GitHub IP 주소를 확인하는 중..." -ForegroundColor Cyan
# github.com의 현재 IP 주소들을 자동으로 가져옴
$githubIPs = (Resolve-DnsName github.com -ErrorAction SilentlyContinue).IPAddress
$gitlabIPs = (Resolve-DnsName gitlab.com -ErrorAction SilentlyContinue).IPAddress

if ($githubIPs) {
    Remove-NetFirewallRule -Name "Block_GitHub_SSH" -ErrorAction SilentlyContinue
    Remove-NetFirewallRule -Name "Block_GitHub_HTTPS" -ErrorAction SilentlyContinue


    New-NetFirewallRule -DisplayName "Block_GitHub_SSH" -Direction Outbound -Action Block -Protocol TCP -RemoteAddress $githubIPs -RemotePort 22 -ErrorAction SilentlyContinue | Out-Null
    New-NetFirewallRule -DisplayName "Block_GitHub_HTTPS" -Direction Outbound -Action Block -Protocol TCP -RemoteAddress $githubIPs -RemotePort 443 -ErrorAction SilentlyContinue | Out-Null
}
else {
    Write-Host "Github IP 조회 실패"
}

if ($gitlabIPs) {
    Remove-NetFirewallRule -Name "Block_GitLab_SSH" -ErrorAction SilentlyContinue
    Remove-NetFirewallRule -Name "Block_GitLab_HTTPS" -ErrorAction SilentlyContinue


    New-NetFirewallRule -DisplayName "Block_GitLab_SSH" -Direction Outbound -Action Block -Protocol TCP -RemoteAddress $gitlabIPs -RemotePort 22 -ErrorAction SilentlyContinue | Out-Null
    New-NetFirewallRule -DisplayName "Block_GitLab_HTTPS" -Direction Outbound -Action Block -Protocol TCP -RemoteAddress $gitlabIPs -RemotePort 443 -ErrorAction SilentlyContinue | Out-Null
}
else {
    Write-Host "GitLab IP 조회 실패"
}