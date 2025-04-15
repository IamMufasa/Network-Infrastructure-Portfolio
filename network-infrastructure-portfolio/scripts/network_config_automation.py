#!/usr/bin/env python3
"""
Network Automation Script for Configuration Management
Demonstrates Python scripting skills for Network Engineer I position

This script automates the deployment of configurations to multiple network devices
using SSH connections and provides validation of the deployment.
"""

import os
import sys
import time
import argparse
import getpass
import logging
from datetime import datetime

# Simulated imports (would use actual libraries in production)
# import paramiko
# import netmiko
# import textfsm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("network_automation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class NetworkDevice:
    """Class representing a network device with connection and configuration methods"""
    
    def __init__(self, hostname, ip_address, device_type, username=None, password=None):
        """Initialize device with connection parameters"""
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.username = username
        self.password = password
        self.connection = None
        self.config_applied = False
        
    def connect(self, username=None, password=None):
        """Establish SSH connection to device"""
        if username:
            self.username = username
        if password:
            self.password = password
            
        logger.info(f"Connecting to {self.hostname} ({self.ip_address})")
        
        # Simulation of connection (would use actual connection in production)
        time.sleep(1)
        self.connection = True
        logger.info(f"Successfully connected to {self.hostname}")
        return True
        
    def disconnect(self):
        """Close SSH connection to device"""
        if self.connection:
            logger.info(f"Disconnecting from {self.hostname}")
            # Simulation of disconnection
            self.connection = None
            return True
        return False
        
    def send_config(self, config_file):
        """Send configuration commands from file to device"""
        if not self.connection:
            logger.error(f"No active connection to {self.hostname}")
            return False
            
        logger.info(f"Applying configuration from {config_file} to {self.hostname}")
        
        # Simulation of configuration application
        try:
            with open(config_file, 'r') as f:
                config_lines = f.readlines()
                
            logger.info(f"Sending {len(config_lines)} configuration lines to {self.hostname}")
            time.sleep(2)
            self.config_applied = True
            logger.info(f"Configuration successfully applied to {self.hostname}")
            return True
        except Exception as e:
            logger.error(f"Error applying configuration to {self.hostname}: {str(e)}")
            return False
            
    def verify_config(self):
        """Verify configuration was properly applied"""
        if not self.connection:
            logger.error(f"No active connection to {self.hostname}")
            return False
            
        if not self.config_applied:
            logger.warning(f"No configuration has been applied to {self.hostname}")
            return False
            
        logger.info(f"Verifying configuration on {self.hostname}")
        
        # Simulation of verification
        time.sleep(1.5)
        logger.info(f"Configuration verification successful on {self.hostname}")
        return True
        
    def backup_config(self, backup_dir):
        """Backup current device configuration"""
        if not self.connection:
            logger.error(f"No active connection to {self.hostname}")
            return False
            
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"{self.hostname}_{timestamp}.cfg")
        
        logger.info(f"Backing up configuration from {self.hostname} to {backup_file}")
        
        # Simulation of backup
        time.sleep(1)
        with open(backup_file, 'w') as f:
            f.write(f"# Configuration backup for {self.hostname}\n")
            f.write(f"# Timestamp: {timestamp}\n")
            f.write("# This is a simulated backup file\n")
            
        logger.info(f"Configuration backup completed for {self.hostname}")
        return backup_file

def load_devices(inventory_file):
    """Load device inventory from file"""
    devices = []
    
    try:
        with open(inventory_file, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        hostname = parts[0].strip()
                        ip_address = parts[1].strip()
                        device_type = parts[2].strip()
                        
                        device = NetworkDevice(hostname, ip_address, device_type)
                        devices.append(device)
    except Exception as e:
        logger.error(f"Error loading device inventory: {str(e)}")
        
    logger.info(f"Loaded {len(devices)} devices from inventory")
    return devices

def main():
    """Main function to run the script"""
    parser = argparse.ArgumentParser(description="Network Configuration Automation Tool")
    parser.add_argument("--inventory", required=True, help="Path to device inventory file")
    parser.add_argument("--config", required=True, help="Path to configuration template file")
    parser.add_argument("--backup-dir", default="./backups", help="Directory for configuration backups")
    parser.add_argument("--username", help="Username for device authentication")
    parser.add_argument("--no-verify", action="store_true", help="Skip configuration verification")
    
    args = parser.parse_args()
    
    # Get username and password
    username = args.username or input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    # Load devices from inventory
    devices = load_devices(args.inventory)
    if not devices:
        logger.error("No devices loaded from inventory. Exiting.")
        return 1
        
    # Process each device
    success_count = 0
    for device in devices:
        try:
            # Connect to device
            if device.connect(username, password):
                # Backup existing configuration
                device.backup_config(args.backup_dir)
                
                # Apply new configuration
                if device.send_config(args.config):
                    # Verify configuration if not skipped
                    if not args.no_verify:
                        device.verify_config()
                    success_count += 1
                
                # Disconnect from device
                device.disconnect()
        except Exception as e:
            logger.error(f"Error processing device {device.hostname}: {str(e)}")
    
    # Report results
    logger.info(f"Configuration deployment completed. Success: {success_count}/{len(devices)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
