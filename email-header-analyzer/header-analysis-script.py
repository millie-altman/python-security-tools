import re

def extract_field(header, field):
    pattern = rf"{field}:\s*(.*)"
    match = re.search(pattern, header, re.IGNORECASE)
    return match.group(1).strip() if match else "Not Found"


def analyze_authentication(header):
    findings = []

    spf = extract_field(header, "spf")
    dkim = extract_field(header, "dkim")
    dmarc = extract_field(header, "dmarc")

    if "fail" in spf.lower():
        findings.append("⚠️ SPF authentication FAILED")

    if "fail" in dkim.lower():
        findings.append("⚠️ DKIM authentication FAILED")

    if "fail" in dmarc.lower():
        findings.append("⚠️ DMARC authentication FAILED")

    return findings


def analyze_from_vs_return(header):
    findings = []

    from_field = extract_field(header, "From")
    return_path = extract_field(header, "Return-Path")

    if from_field != "Not Found" and return_path != "Not Found":
        from_domain = from_field.split("@")[-1].replace(">", "").strip()
        return_domain = return_path.split("@")[-1].replace(">", "").strip()

        if from_domain != return_domain:
            findings.append("⚠️ From domain does NOT match Return-Path domain")

    return findings


def analyze_received_ips(header):
    findings = []

    ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", header)

    private_ranges = ["10.", "192.168", "172.16"]

    for ip in ips:
        if not any(ip.startswith(r) for r in private_ranges):
            findings.append(f"🔎 Public IP found in Received chain: {ip}")

    return findings


def phishing_header_analyzer(header):
    results = []

    print("\n--- Phishing Header Analysis ---\n")

    results.extend(analyze_authentication(header))
    results.extend(analyze_from_vs_return(header))
    results.extend(analyze_received_ips(header))

    if not results:
        print("✅ No obvious phishing indicators found.")
    else:
        for r in results:
            print(r)


def main():
    print("Paste the email header below. Type END on a new line when finished:\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    header = "\n".join(lines)

    phishing_header_analyzer(header)


if __name__ == "__main__":
    main()
