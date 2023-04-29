#!/usr/bin/env python3

import subprocess
output = subprocess.getoutput("ls -l")
print(output)

