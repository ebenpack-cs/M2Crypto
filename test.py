#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from M2Crypto.BIO import openfile

f = openfile('/tmp/test.txt', 'w')
ret = f.write('Zemské desky')
f.close()
size = os.path.getsize('/tmp/test.txt')
if size == 0:
    sys.exit(1)
