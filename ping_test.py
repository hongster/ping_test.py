#!/usr/bin/env python

import csv
from email.Utils import formatdate
import re
import subprocess
import time

# Configurations
ping_host = 'example.com'
ping_count = 4
log_file = '/tmp/ping_test.log'

# Perform ping
timestamp = formatdate(time.time(), True)
output = subprocess.Popen(['ping', '-c', str(ping_count), ping_host], stdout=subprocess.PIPE).stdout.read()

# MAC OS X: 4 packets transmitted, 4 packets received, 0.0% packet loss
# Linux: 4 packets transmitted, 4 received, 0% packet loss, time 3207ms
match = re.search('(\d+) (?:packets )?received', output)

# Check success rate
success = 0
if match is not None:
	success = int(match.group(1))

# Log result in CSV format
writer = csv.writer(open(log_file, 'a'))
writer.writerow([timestamp, success, ping_count])
