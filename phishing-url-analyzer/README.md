# Phishing URL Analyzer
## CTI Analyst Tool | URL Risk Scoring | Domain Intelligence | Phishing Triage

**Author:** Millie Altman
**Language:** Python 3.x  
**Dependencies:** `python-whois`, `re`, `urllib`  
**Status:** v3 — Investigation Grade  

---

## The Problem

During phishing triage, analysts manually evaluate URLs for risk indicators — checking protocols, inspecting domain names for impersonation patterns, and looking up domain registration age via WHOIS. For high-volume alert environments, this process is repetitive and time-consuming.

This tool automates that workflow, producing structured risk scoring output that can be directly referenced in incident reports.

---

## CTI Application

This tool was used directly during the analysis documented in the [Phishing Campaign Intelligence Report (SOC-IR-2026-017)](https://github.com/[yourusername]/threat-intelligence-portfolio/blob/main/finished-intelligence/phishing-triage-report.md).

The suspicious URL `hxxps://login-microsoft-support[.]com/auth` was analyzed using this tool, which flagged domain impersonation patterns, a suspicious credential harvesting path, and a recently registered domain — corroborating manual header analysis findings.

---

## Detection Capabilities

| Check | Description | Risk Weight |
|---|---|---|
| IP address domain | URL uses raw IP instead of domain name | +2 |
| HTTP protocol | Insecure protocol — no TLS | +1 |
| Suspicious keywords | Login, verify, secure, account, bank, password | +1 |
| URL shortener | bit.ly, tinyurl, goo.gl, t.co detected | +1 |
| Very new domain | Registered < 30 days ago (WHOIS) | +2 |
| Recently registered | Registered < 180 days ago (WHOIS) | +1 |

**Risk Scoring:**
- Score 0 → **LOW** — no indicators detected
- Score 1–2 → **MEDIUM** — investigate further
- Score 3+ → **HIGH** — treat as malicious pending confirmation

---

## Tool Versions

This tool was developed in three stages to reflect a real development lifecycle — from basic detection prototype to investigation-grade analyst utility.

### Version 1 — Basic URL Detector
**File:** `phishing_detector.py`

Core detection logic: suspicious keywords, HTTP vs HTTPS, URL shorteners, IP-based domains. Designed as a fast triage filter.

```bash
python phishing_detector.py
```

**Example output:**

![V1 Output](./images/phishing_output_example.png)

---

### Version 2 — Domain Intelligence
**File:** `phishing_detector_expanded.py`

Adds WHOIS domain registration age lookup. Newly registered domains (< 30 days) are a high-confidence phishing indicator — this version surfaces that data automatically.

```bash
pip install python-whois
python phishing_detector_expanded.py
```

**New in V2:**
- Domain age lookup via WHOIS
- Weighted risk scoring (IP address detection weight increased)
- Structured output sections

---

### Version 3 — Investigation-Grade Output
**File:** `phishing_investigation_tool.py`

Full SOC-style investigation report output. Produces structured, labeled sections — Target URL, Domain, Indicators Detected, Domain Intelligence, Threat Assessment — formatted for direct use in incident documentation.

```bash
python phishing_investigation_tool.py
```

**Example output:**

![V3 Investigation Output](./images/phishing_url_investigation_outcome.png)

**New in V3:**
- Full investigation report formatting
- Domain extracted and displayed separately from full URL
- Clear separation of indicator detection, domain intelligence, and threat assessment sections
- Output designed for copy-paste into incident reports

---

## Usage

```bash
# Clone the repo
git clone https://github.com/[yourusername]/python-security-tools.git
cd python-security-tools/phishing-url-analyzer

# Install dependencies
pip install python-whois

# Run V3 (recommended)
python phishing_investigation_tool.py

# Enter URL when prompted
Enter a URL to analyze: https://login-microsoft-support.com/auth
```

**Note:** Always defang malicious URLs before storing or sharing:
`https://login-microsoft-support.com/auth` → `hxxps://login-microsoft-support[.]com/auth`

---

## Planned Improvements

- **Typosquatting detection** — flag domains that use character substitution or brand name concatenation to impersonate known organizations (e.g., `rn` substituted for `m`, `0` for `o`)
- **VirusTotal API integration** — enrich domain reputation data with VT scores and community detections
- **Bulk URL analysis** — accept a list of URLs from a file for batch triage
- **Exportable JSON output** — produce machine-readable investigation results for SIEM or MISP ingestion
- **Entropy scoring** — flag high-entropy domains often associated with DGA (domain generation algorithm) malware C2

---

## Skills Demonstrated

- Python scripting for security automation
- URL parsing and structured analysis (`urllib`)
- Domain intelligence via WHOIS (`python-whois`)
- Risk scoring logic design
- CTI analyst workflow automation
- Iterative tool development lifecycle
