function FindProxyForURL(url, host)
{
    if (
        dnsDomainIs(host, "github.com") ||
        shExpMatch(host, "*.github.com") ||
        dnsDomainIs(host, "githubusercontent.com") ||
        shExpMatch(host, "*.githubusercontent.com") ||
        dnsDomainIs(host, "githubassets.com") ||
        shExpMatch(host, "*.githubassets.com")
    )
    {
        return "PROXY 127.0.0.1:9999";
    }

    return "DIRECT";
}