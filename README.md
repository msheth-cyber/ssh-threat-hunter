# 🛡️ Linux SSH Threat Hunter & Log Analyzer

A lightweight, defensive cybersecurity tool built to parse Red Hat/Rocky Linux system logs (`/var/log/secure`) to identify and alert on live SSH Brute Force attacks. 

## 🚀 Features
* **Automated Log Parsing:** Scans native Linux authentication logs using regular expressions.
* **Threat Threshold Flagging:** Identifies and aggregates malicious source IPs executing high-frequency password guessing.
* **SecOps Visibility:** Generates clear CLI alerts mimicking a simplified Security Operations Centre (SOC) triage workflow.

## 🛠️ Requirements & Linux Internals Applied
* **OS:** RHEL / Rocky Linux 9
* **Security Context:** Must be run with elevated permissions (`sudo`) to securely access administrative logging structures.
* **Core Skills:** Python, Log Analysis, Regex, System Auditing, Incident Triage.

## 📊 Sample Output
```text
=== 🛡️ SSH THREAT INTELLIGENCE REPORT ===
Analyzing: /var/log/secure
[🚨 ALERT] Potential Brute Force Detected!
Source IP: 192.168.1.45
Failed Attempts: 14
```
