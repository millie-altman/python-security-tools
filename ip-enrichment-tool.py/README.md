# IP Enrichment Tool
## CTI Analyst Tool | AbuseIPDB API | IOC Reputation Lookup

**Author:** Millie Altman
**Language:** Python 3.x  
**Dependencies:** `requests`, `os`, `sys`  
**Status:** v1  

---

## The Problem

During incident triage, analysts frequently encounter suspicious IP addresses in SIEM alerts, firewall logs, and authentication records that require rapid reputation assessment. Manual lookups against threat intelligence databases are time-consuming at volume and introduce inconsistency in how results are recorded.

This tool automates the lookup workflow — querying AbuseIPDB in real time and returning structured reputation data formatted for direct use in investigation notes and incident reports.

---

## CTI Application

Developed during threat intelligence enrichment operations in the [CTI Research Lab](https://github.com/millie-altman/cti-research-lab). Used to enrich IP addresses observed in Wazuh SIEM alerts and cross-reference against open-source threat intelligence feeds.

**Example workflow:**
```
Suspicious IP flagged in Wazuh alert
              ↓
python3 ip_enrich.py <IP_ADDRESS>
              ↓
AbuseIPDB returns: confidence score / country / ISP
              ↓
Analyst assessment → document in investigation notes
```

---

## Usage

```bash
# Set API key as environment variable — never hardcode credentials
export ABUSEIPDB_API_KEY="your_api_key_here"

# Run lookup against target IP
python3 ip_enrich.py <TARGET_IP>
```

**Get a free AbuseIPDB API key:** [abuseipdb.com](https://www.abuseipdb.com)

---

## Example Output

```
[+] Results for 1.0.164.165:
    - Score: 100/100
    - Country: TH
    - ISP: TOT Public Company Limited
```

![Live Lookup Output](./images/live-lookup-100.png)

**Interpreting results:**
- **Score 0–25:** Low risk — likely benign, monitor if context warrants
- **Score 26–75:** Medium risk — investigate further before actioning
- **Score 76–100:** High confidence malicious — appropriate for immediate block and SIEM rule addition

---

## Security Design

API credentials are loaded exclusively from OS environment variables (`ABUSEIPDB_API_KEY`) — never hardcoded into source code. This follows standard secure credential management practices for tools deployed in analyst environments or shared repositories.

---

## Planned Improvements

- Bulk IP analysis — accept a file of IPs for batch triage
- Multi-source enrichment — add VirusTotal and Shodan lookups in a single query
- Structured JSON output — machine-readable results for SIEM or MISP ingestion
- Confidence threshold alerting — flag IPs above a configurable score threshold automatically
