#!/usr/bin/env python

import subprocess, sys

try:    file = str(sys.argv[2])
except: file = "dist/SleekCordDev.theme.css"

subprocess.run(["sass", "src/import.scss", "dist/import.css"], capture_output=True, text=True, check=True)
subprocess.run(["sass", "src/main/easterEggs.scss", "dist/easterEggs.css"], capture_output=True, text=True, check=True)

if sys.argv[1] == "--dev":
    subprocess.run(["sass", "src/dev.scss", file], capture_output=True, text=True, check=True)
