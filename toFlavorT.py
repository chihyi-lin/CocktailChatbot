# import xml element tree
import xml.etree.ElementTree as ET
  
# import mysql connector
import mysql.connector
  
# give the connection parameters 
# user name is root
# password is empty
# server is localhost
# database name is database
conn = mysql.connector.connect(user='root', 
                               password='', 
                               host='localhost', 
                               database='database')
  
if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

# reading xml file , file name is cocktail.xml
tree = ET.parse('cocktails.xml')
  
# in our xml file flavor is the root for all flavor data.
data2 = tree.findall('cocktail')

# retrieving the data and insert into table
# i value for xml data 
# j value printing number of values that are stored
for i, j in zip(data2, range(1, 31)):
    name = i.find('name').text
    flavor = i.findall('flavor')

    for k, l in zip(flavor, range(1, 6)):
        taste1 = k.find('taste1').text
        
        try:
            taste2 = k.find('taste2').text
        except:
            taste2 = ""
        
        try:
            taste3 = k.find('taste3').text
        except:
            taste3 = ""

    # sql query to insert data into database
    data = """INSERT INTO flavor(name,taste1,taste2,taste3) VALUES(%s,%s,%s,%s)"""
  
    # creating the cursor object
    c = conn.cursor()
      
    # executing cursor object
    c.execute(data, (name, taste1, taste2, taste3))
    conn.commit()
    print("cocktail tabelflavor No-", j, " stored successfully")