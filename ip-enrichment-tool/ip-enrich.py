cat << 'EOF' > ip_enrich.py
import os
import sys
import requests

def check_ip():
    key = os.environ.get("ABUSEIPDB_API_KEY")
    ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Accept": "application/json", "Key": key}
    params = {"ipAddress": ip}
    
    try:
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            d = r.json()["data"]
            print(f"\n[+] Results for {d['ipAddress']}:")
            print(f"    - Score: {d['abuseConfidenceScore']}/100")
            print(f"    - Country: {d['countryCode']}")
            print(f"    - ISP: {d['isp']}")
        else:
            print(f"[!] Error: {r.status_code}")
    except Exception as e:
        print(f"[!] Request failed: {e}")

if __name__ == "__main__":
    check_ip()
EOF
