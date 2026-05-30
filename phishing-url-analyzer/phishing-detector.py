###
Phishing Detection & URL Risk Analysis Tool

Author: Millie Altman
Description: This script analyzes URLs for common phishing indicators such as suspicious keywords, insecure protocols,
IP-based domains and URL shorteners.

The tool assigns a risk score and provides warnings for potentially malicious links. 
###

import re
from urllib.parse import urlparse

# Words commonly used in phishing URLs
suspicious_keywords = [
    "login", "verify", "secure", "update", "account", "bank", "password"
]

# Common URL shorteners (hide real link)
url_shorteners = ["bit.ly", "tinyurl.com", "goo.gl", "t.co"]

def analyze_url(url):
    risk_score = 0
    warnings = []

    parsed = urlparse(url)
    domain = parsed.netloc

    # Check for IP address
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        warnings.append("URL uses an IP address instead of a domain")
        risk_score += 1

    # Check for HTTP instead of HTTPS
    if parsed.scheme == "http":
        warnings.append("URL uses HTTP instead of HTTPS")
        risk_score += 1

    # Check for suspicious keywords
    for word in suspicious_keywords:
        if word in url.lower():
            warnings.append(f"Suspicious keyword found: {word}")
            risk_score += 1
            break

    # Check for URL shorteners
    for shortener in url_shorteners:
        if shortener in domain:
            warnings.append("URL shortener detected")
            risk_score += 1

    return risk_score, warnings

def main():
    url = input("Enter a URL to analyze: ")

    score, warnings = analyze_url(url)

    print("\nAnalysis Results:")
    for warning in warnings:
        print("⚠️", warning)

    if score == 0:
        print("✅ No obvious phishing indicators found")
    elif score <= 2:
        print("⚠️ Medium Risk")
    else:
        print("🚨 HIGH PHISHING RISK")

if __name__ == "__main__":
    main()
