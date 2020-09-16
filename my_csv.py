import csv
import pandas as pd
from csv import reader

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fnn8voub",
  database="drupal8"
)



rows = pd.read_csv('alt_names.csv')
row_l = (len(rows))

my_list = []
queries = []
counter = 0


# open file in read mode
with open('alt_names.csv', 'r') as read_obj:
  # pass the file object to reader() to get the reader objec
  csv_reader = reader(read_obj)
  # Iterate over each row in the csv using reader object
  for row in csv_reader:
    # row variable is a list that represents a row in csv
    list_item =((row[1]),(row[5]))
    #print(list_item)
    my_list.append(list_item)

for i in my_list:
  q = ("INSERT INTO taxonomy_term__field_authority_link VALUES('geo_location','0'," + '\'' + i[0] + '\'' + "," + '\'' + i[0] + '\'' + "," + "'en','98','http://vocab.getty.edu/page/tgn/7001314','http://vocab.getty.edu/page/tgn/7001314','a:0:{}','other');")
  queries.append(q)

#print(queries[1])

for q in queries[1:]:
  cursor = mydb.cursor()
  cursor.execute(q)
  mydb.commit()

  print(cursor.rowcount, "Record inserted successfully into Laptop table")
  cursor.close()
