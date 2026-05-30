"""
Phishing Detection & URL Risk Analysis Tool (Expanded Version)

This script analyzes URLs for common phishing indicators including:
- Suspicious keywords
- HTTP vs HTTPS
- IP address domains
- URL shorteners
- Domain registration age (WHOIS)

Author: Millie Altman
"""

import re
from urllib.parse import urlparse
import whois
from datetime import datetime

# Common phishing keywords
suspicious_keywords = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "password"
]

# Common URL shorteners attackers use
url_shorteners = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co"
]


def check_domain_age(domain):
    """Check how old a domain is using WHOIS."""
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        # Sometimes WHOIS returns multiple dates
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        age = (datetime.now() - creation_date).days
        return age

    except:
        return None


def analyze_url(url):

    risk_score = 0
    warnings = []

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.", "")

    # Check for IP address domains
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        warnings.append("URL uses an IP address instead of a domain")
        risk_score += 2

    # Check HTTP instead of HTTPS
    if parsed_url.scheme == "http":
        warnings.append("URL uses HTTP instead of HTTPS")
        risk_score += 1

    # Check suspicious keywords
    for word in suspicious_keywords:
        if word in url.lower():
            warnings.append(f"Suspicious keyword detected: {word}")
            risk_score += 1
            break

    # Check URL shorteners
    for shortener in url_shorteners:
        if shortener in domain:
            warnings.append("URL shortener detected")
            risk_score += 1

    # Check domain age
    domain_age = check_domain_age(domain)

    if domain_age is not None:

        if domain_age < 30:
            warnings.append(f"Domain is VERY new ({domain_age} days old)")
            risk_score += 2

        elif domain_age < 180:
            warnings.append(f"Domain is relatively new ({domain_age} days old)")
            risk_score += 1

    return risk_score, warnings, domain_age

def main():

    url = input("Enter a URL to analyze: ")

    score, warnings, age = analyze_url(url)

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.", "")

    print("\n==============================")
    print(" PHISHING URL INVESTIGATION")
    print("==============================\n")

    print(f"Target URL: {url}")
    print(f"Domain: {domain}")

    print("\n--- Indicators Detected ---")

    if warnings:
        for warning in warnings:
            print(f"• {warning}")
    else:
        print("No obvious phishing indicators detected")

    print("\n--- Domain Intelligence ---")

    if age:
        print(f"Domain age: {age} days")
    else:
        print("Domain age: Unable to determine")

    print("\n--- Threat Assessment ---")

    if score == 0:
        print("Risk Score:", score)
        print("Threat Level: LOW")

    elif score <= 2:
        print("Risk Score:", score)
        print("Threat Level: MEDIUM")

    else:
        print("Risk Score:", score)
        print("Threat Level: HIGH 🚨")

    print("\nInvestigation Complete\n")

if __name__ == "__main__":
    main()
