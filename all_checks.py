#!/usr/bin/env python3
import shutil
import sys
import os 

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, otherwise false"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of the free space
    percent_free = 100* du.free/du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free/2*30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, false otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)
# check for at least 2 GB and 10% free
def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    if check_disk_full ():
        print('Root partition full')
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)
