#!/usr/bin/env python3
import os
import sys

def run_security_pre_checks(log_path):
    """Validates the execution environment before running log analysis logic."""
    print("=== INITIALIZING THREAT HUNTER ENVIRONMENT AUDIT ===")

    # 1. PRIVILEGE CHECK: Ensure the script is running as root/sudo
    if os.geteuid() != 0:
        print("❌ PRIVILEGE ERROR: Administrative permissions required.")
        print("Log data within /var/log/ contains sensitive authentication vectors.")
        print("Please re-run this script utilizing: sudo python3 ssh_hunter.py")
        sys.exit(1)
    print("✅ Administrative privilege check: PASSED")

    # 2. PATH VALIDATION: Verify if the system authentication log file exists
    if not os.path.exists(log_path):
        print(f"❌ COMPATIBILITY ERROR: Target log not found at: {log_path}")
        print("This framework expects a Red Hat Enterprise Linux / Rocky Linux core layout.")
        print("If deploying on Debian/Ubuntu, track '/var/log/auth.log' instead.")
        sys.exit(2)
    print(f"✅ Target log path located: PASSED")

    # 3. READ PERMISSION CHECK: Double-check the file is readable
    if not os.access(log_path, os.R_OK):
        print(f"❌ ACCESS ERROR: File exists but is completely unreadable.")
        print("Verify local ACL matrices or SELinux policies governing access paths.")
        sys.exit(3)
    print("✅ Log readability verification: PASSED")
    print("=== ENVIRONMENT SECURE: COMMENCING SSH THREAT HUNTING ===\n")


def analyze_ssh_failures(log_path):
    """Parses /var/log/secure to extract and tally malicious brute-force IP entries."""
    # A dictionary (key-value pair) to store IP addresses and their failure counts
    failed_attempts = {}

    print(f"Scanning target log space: {log_path}...")
    
    with open(log_path, "r") as file:
        for line in file:
            # We look for standard openSSH failure syntax keywords
            if "Failed password for" in line:
                # Split the text line into individual words
                words = line.strip().split()
                
                try:
                    # In a standard RHEL log line: ... "Failed password for invalid user root from 192.168.1.50 port 54321 ssh2"
                    # Or: ... "Failed password for root from 192.168.1.50 port 54321 ssh2"
                    # We locate the word 'from' and extract the very next word, which is always the IP address.
                    from_index = words.index("from")
                    ip_address = words[from_index + 1]
                    
                    # Add to our dictionary tracking counter
                    if ip_address in failed_attempts:
                        failed_attempts[ip_address] += 1
                    else:
                        failed_attempts[ip_address] = 1
                except (ValueError, IndexError):
                    # Safely skip the line if it has unusual, corrupted formatting
                    continue

    # Display the final summary reports to the console
    if not failed_attempts:
        print("🎉 Clean Audit: No failed SSH password attempts identified in this log cycle.")
    else:
        print("\n[🚨 THREAT DETECTION SUMMARY: SUSPICIOUS BRUTE-FORCE ACTIVITY]")
        print(f"{'IP ADDRESS':<20} | {'FAILED ATTEMPTS'}")
        print("-" * 40)
        
        # Loop through and sort the dictionary to show the highest threat attackers first
        for ip, count in sorted(failed_attempts.items(), key=lambda item: item[1], reverse=True):
            # Flag extreme threats (more than 5 attempts) with a warning icon
            alert_flag = "⚠️" if count >= 5 else "  "
            print(f"{alert_flag} {ip:<17} | {count} attempts")


# Main execution gateway
if __name__ == "__main__":
    TARGET_LOG_FILE = "/var/log/secure"
    
    # 1. Run environment guardrails
    run_security_pre_checks(TARGET_LOG_FILE)
    
    # 2. Execute threat analysis loop
    analyze_ssh_failures(TARGET_LOG_FILE)

