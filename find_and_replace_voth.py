#!/usr/bin/python3

# This is a find and replace script that uses a dictionary to replace voth location codes with actual location names.

import os
from locations import loc_dict

home = '/var/www/html/drupal/web/sites/default/files/voices_copy/'

keyword = {
  "#vothL123":"LongLocation",
  "#vothL111":"NoLocation",
  "#vothL12":"ShortLocation",
  "#vothL126":"LongestLocation"
}

my_file = 'wolfI.xml'

#for k in sorted(loc_dict,  key=len, reverse=True):
        #print(k, loc_dict[k])
        #print(f)

for dirs, subs, files in os.walk(home):
  for f in files:
    #print(dirs, f)
    f = (dirs + f)
    if f.endswith('.xml'):
      #print(f)
      # Need to sort dictionary by key length in reverse

      # Read File
      with open(f, 'r') as file:
        filedata = file.read()
        print(filedata)

        for k in sorted(loc_dict,  key=len, reverse=True):
        #print(k, loc_dict[k])
        #print(f)

      # Replace key with value
          filedata = filedata.replace(k, loc_dict[k])

      # Write new file
      with open(f, 'w') as file:
        file.write(filedata)
