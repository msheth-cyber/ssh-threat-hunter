# 🛡️ Linux SSH Threat Hunter & Log Analyzer

A lightweight, defensive cybersecurity tool built to parse Red Hat/Rocky Linux system logs (`/var/log/secure`) to identify, aggregate, and alert on live SSH Brute Force attacks.

## 🚀 Features
* **Defensive Architecture Checks:** Enforces root execution privileges (`UID 0`) and validates log pathways before executing to protect system stability.
* **Automated Log Parsing:** Efficiently filters dense, unstructured Linux authentication log matrices without heavy external dependencies.
* **Threat Threshold Flagging:** Aggregates malicious source IPs executing high-frequency password guessing and sorts them by risk level.
* **SecOps Visibility:** Generates clear CLI alerts mimicking a simplified Security Operations Centre (SOC) triage workflow.

## 🛠️ Requirements & Linux Internals Applied
* **OS Distribution:** RHEL / Rocky Linux 9 Core Footprint.
* **Security Context:** Must be run with elevated permissions (`sudo`) to securely access administrative logging structures.
* **Core Skills:** Python 3 Systems Engineering, Log Analysis, System Auditing, Incident Triage, File I/O Handling.

## 📊 Sample Output
```text
=== INITIALIZING THREAT HUNTER ENVIRONMENT AUDIT ===
    ✅ Administrative privilege check: PASSED
    ✅ Target log path located (/var/log/secure): PASSED
    ✅ Log readability verification: PASSED
=== ENVIRONMENT SECURE: COMMENCING SSH THREAT HUNTING ===

Scanning target log space: /var/log/secure...

[🚨 THREAT DETECTION SUMMARY: SUSPICIOUS BRUTE-FORCE ACTIVITY]
IP ADDRESS           | FAILED ATTEMPTS
----------------------------------------
⚠️ 192.168.1.45       | 14 attempts
   10.0.0.12         | 2 attempts
```

## ⚙️ Script Deployment & Execution
To deploy and test this threat analysis engine inside a private Linux testing node:

```bash
# Clone the repository asset down onto your node
git clone https://github.com
cd ssh-threat-hunter

# Elevate script execution permissions
chmod +x ssh_hunter.py

# Launch the engine utilizing administrative privilege tiers
sudo ./ssh_hunter.py
```

## 📄 Licensing
Distributed under the protective terms of the MIT Open Source Framework License.

