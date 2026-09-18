#!/usr/bin/env python3
import re
from collections import Counter

# Path to Red Hat/Rocky Linux authentication logs
LOG_FILE = "/var/log/secure"
THRESHOLD = 5  # Number of failed attempts before flagging an IP

def analyze_ssh_failures():
    failed_ips = []
    

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                # Look for failed password attempts in the log line
                if "Failed password" in line:
                    # Extract the IP address using regular expressions
                    ip_match = re.search(r"from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
                    if ip_match:
                        failed_ips.append(ip_match.group(1))
                        
        # Count occurrences of each malicious IP
        ip_counts = Counter(failed_ips)
        
        print("=== 🛡️ SSH THREAT INTELLIGENCE REPORT ===")
        print(f"Analyzing: {LOG_FILE}\n")
        
        has_threats = False
        for ip, count in ip_counts.items():
            if count >= THRESHOLD:
                print(f"[🚨 ALERT] Potential Brute Force Detected!")
                print(f"   Source IP: {ip}")
                print(f"   Failed Attempts: {count}\n")
                has_threats = True
                
        if not has_threats:
            print("[✅ CLEAR] No malicious brute force patterns detected.")
            
    except PermissionError:
        print("[❌ ERROR] Run this script with 'sudo' to read system authentication logs.")

if __name__ == "__main__":
    analyze_ssh_failures()
