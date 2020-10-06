import xml.etree.ElementTree as ET
import csv
import os

int_places = []
my_dir = r'C:\Users\tfluhr\Desktop\voices_no_ns'

#my_file =r'C:\Users\tfluhr\Desktop\voices_no_ns\billiT.xml'

# iterate all elements
#for elem in root.iter():    
#    print(elem.tag)

def get_places(x):
    tree = ET.parse(x)
    root = tree.getroot()
    
    places = []    

    
    # use xpath to target place names.  use get method to select attribute values
    scratch = []
    for place in root.findall("./text/body/div/div/u/placeName"):
        voth = place.get('ref')
        if voth not in scratch:
            scratch.append(voth)    
        #print(place.text, voth)
        
    long_string = ';'.join(scratch)
    places.append(long_string)
    
    scratch = []
        #print (long_string)
        
    #print(places)
    int_places.append(places)
    #int_places.append(long_string)

# get element attribute value. append to list
    for uid in root.iter('recording'):
        #uid = (uid.attrib)
        id = uid.get('id')
        places.append(id)
    
for dirs, subs, files in os.walk(my_dir):
    for f in files:
        fname = (my_dir + '\\' + f)
        get_places(fname)

# write to csv

file = open(r'C:\Users\tfluhr\Desktop\places2.csv', 'a+', newline = '')
with file:
    write = csv.writer(file)
    write.writerows(int_places)

print(int_places)
#for i in int_places:
#    print(i)
