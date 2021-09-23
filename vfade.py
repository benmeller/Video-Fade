#!/usr/bin/env python3

import sys
from moviepy import *

print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: vfade.py VIDEO-FILENAME")
    raise SystemExit