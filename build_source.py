
#!/usr/bin/python3
import os

base_path = 'http://digital.library.iit.edu/sites/default/files/voices_fix/'

my_dir = '/home/tfluhr/voices_fix'

#list = open("list.txt", "w")

for dirs, subs, files in os.walk(my_dir):
        for fname in files:
                list = open('list.txt', "a")
                list.write("    - \"" + base_path + fname + "\"\n")
                list.close()

