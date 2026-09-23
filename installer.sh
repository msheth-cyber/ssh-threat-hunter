#!/bin/sh
# Automated Zero-Touch Deployment Wrapper for Linux SSH Threat Hunter

echo "=== 📥 STARTING AUTOMATED INFRASTRUCTURE DEPLOYMENT ==="

# 1. Verify administrative execution rights immediately
if [ "$(id -u)" -ne 0 ]; then
    echo "❌ ERROR: Root privileges required to run network installers."
    echo "Please re-execute using: curl -sSL ... | sudo sh"
    exit 1
fi

# 2. Establish temporary execution space
DEPLOY_DIR="/tmp/ssh-threat-hunter-deployment"
rm -rf "$DEPLOY_DIR" # Clear any stale previous loops
mkdir -p "$DEPLOY_DIR"
cd "$DEPLOY_DIR" || exit 1

# 3. Pull the code assets silently down from GitHub
echo "Connecting to GitHub asset tracking lines..."
if ! git clone -q https://github.com .; then
    echo "❌ ERROR: Failed to clone codebase repository from GitHub network."
    exit 2
fi

# 4. Automate file optimization and execution permissions
chmod +x ssh_hunter.py

echo "✅ Deployment compilation successful. Launching core engine..."
echo "=========================================================\n"

# 5. Hand execution focus off to the secure Python application engine
./ssh_hunter.py

