#!/usr/bin/env python3

import shutil
import psutil

def check_diskusage(disk):
	du = shutil.disk_usage(disk)
	free = du.free/du.total*100
	return free > 20
def check_cpuusage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_diskusage("/") or not check_cpuusage():
	print("ERROR")
else:
	print("Everything is ok")
