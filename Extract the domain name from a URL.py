# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]