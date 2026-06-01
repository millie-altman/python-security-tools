# Python Security Tools

**Analyst & Developer:** Millie Altman

![Python](https://img.shields.io/badge/Language-Python%203.x-blue)
![CTI Tooling](https://img.shields.io/badge/Focus-CTI%20Analyst%20Tooling-purple)
![Phishing Detection](https://img.shields.io/badge/Tool-Phishing%20Detection-orange)
![IOC Enrichment](https://img.shields.io/badge/Tool-IOC%20Enrichment-red)
![AbuseIPDB](https://img.shields.io/badge/API-AbuseIPDB-darkblue)
![OSINT](https://img.shields.io/badge/Skill-OSINT%20Automation-blue)

**Focus:** CTI Analyst Tooling | Phishing Detection | IOC Enrichment | OSINT Automation  
**Language:** Python 3.x  

---

## Overview

Python tools built to automate analyst workflows in cyber threat intelligence and security operations. Each tool addresses a specific investigative problem — reducing manual effort, accelerating triage, and producing structured output suitable for documentation and reporting.

Tools are developed iteratively, reflecting a real-world development lifecycle from prototype to investigation-grade utility. All tools are built around CTI and SOC analyst use cases.

---

## Tool Index

| Tool | Problem It Solves | Version |
|---|---|---|
| [Phishing URL Analyzer](./phishing-url-analyzer/) | Automates URL risk scoring and domain intelligence during phishing triage | v3 |
| [Email Header Analyzer](./email-header-analyzer/) | Automates SPF/DKIM/DMARC inspection and sender infrastructure analysis | v1 |
| [IP Enrichment Tool](./ip-enrichment-tool/) | Automates AbuseIPDB reputation lookups against suspicious IPs observed in SIEM alerts | v1 |

---

## Phishing URL Analyzer

**Problem:** Phishing triage requires manual inspection of URLs for risk indicators — a repetitive process that benefits from automation.

**Solution:** Parses URLs, scores phishing risk indicators, queries WHOIS for domain registration age, and produces structured investigation output formatted for analyst reporting.

**CTI Application:** Used in the [Phishing Campaign Intelligence Report](https://github.com/millie-altman/threat-intelligence-portfolio/blob/main/finished-intelligence/phishing-triage-report.md) to analyze a credential harvesting URL during investigation SOC-IR-2026-017.

→ [`phishing-url-analyzer/`](./phishing-url-analyzer/)

---

## Email Header Analyzer

**Problem:** Manual email header inspection — checking SPF, DKIM, DMARC, sender/return-path mismatches, and originating IPs — is error-prone and slow at volume.

**Solution:** Parses raw email headers, evaluates authentication results, flags domain mismatches between From and Return-Path fields, and extracts public IPs from the received chain.

**CTI Application:** Used in the [Phishing Campaign Intelligence Report](https://github.com/millie-altman/threat-intelligence-portfolio/blob/main/finished-intelligence/phishing-triage-report.md) to confirm spoofed sender infrastructure during investigation SOC-IR-2026-017.

→ [`email-header-analyzer/`](./email-header-analyzer/)

---

## IP Enrichment Tool

**Problem:** Suspicious IPs appear constantly in SIEM alerts, firewall logs, and authentication records. Manual reputation lookups are inconsistent and slow at volume.

**Solution:** Queries the AbuseIPDB API in real time and returns a structured reputation report — abuse confidence score, country of origin, and ISP — formatted for direct use in investigation notes.

**CTI Application:** Developed during threat intelligence enrichment operations in the [CTI Research Lab](https://github.com/millie-altman/cti-research-lab) to enrich IPs observed in Wazuh SIEM alerts.

→ [`ip-enrichment-tool/`](./ip-enrichment-tool/)

---

## Development Philosophy

**Analyst-first output** — every tool produces output structured for documentation, not just terminal readability. Results should be usable directly in incident reports without reformatting.

**Iterative development** — tools are versioned to reflect real development cycles. The phishing URL analyzer shows deliberate progression from basic detection logic to full investigation-grade output across three versions.

**CTI-grounded problems** — Every tool exists because a real analyst workflow needs to be automated. The problem drives the tool, not the other way around.

---

## Planned Tools

| Tool | Problem | Status |
|---|---|---|
| IOC Enrichment Script | Bulk IOC lookup against VirusTotal, AbuseIPDB, and Shodan APIs in a single query | Planned |
| OSINT Domain Profiler | Automates WHOIS, DNS history, and passive DNS lookups for domain investigation | Planned |
| STIX IOC Formatter | Converts extracted IOCs into STIX 2.1 format for threat intelligence platform ingestion | Planned |
| Threat Feed Aggregator | Pulls and normalizes IOCs from open-source threat feeds (MISP, OTX, URLhaus) | Planned |

---

## Setup

```bash
git clone https://github.com/[yourusername]/python-security-tools.git
cd python-security-tools
pip install -r requirements.txt
```

**Dependencies:**
```
requests
python-whois
```

---

## Related Repositories

| Repository | Description |
|---|---|
| [threat-intelligence-portfolio](https://github.com/millie-altman/threat-intelligence-portfolio) | Finished intelligence products where these tools were applied |
| [threat-actor-profiles](https://github.com/millie-altman/threat-actor-profiles) | Structured threat actor research and TTP analysis |
| [cti-research-lab](https://github.com/millie-altman/cti-research-lab) | Threat research lab where several tools were developed and tested |

---

## Contact

Open to CTI analyst, threat researcher, and security engineering roles.  
Connect on [LinkedIn](https://linkedin.com/in/millieealtman)
