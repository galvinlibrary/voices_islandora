#!/usr/bin/python3

## Removing xml namespaces to make xpath search easier for drupal migrate module

import os
import shutil

my_dir = '/home/tfluhr/voices_fix'
ns_rem = '<TEI xmlns:xi="http://www.w3.org/2001/XInclude" xmlns="http://www.tei-c.org/ns/1.0">'
replacement = ""

#print('hello')

for dirs, subs, files in os.walk(my_dir):
        for fname in files:
                fpath = os.path.join(dirs, fname)
                with open(fpath) as f:
                        s = f.read()
                s = s.replace("xml:", replacement)
                s = s.replace("xi:", replacement)
                s = s.replace(ns_rem, '<TEI>')
                with open(fpath, "w") as f:
                        f.write(s)
