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
  
# in our xml file student is the root for all student data.
data2 = tree.findall('cocktail')


# retrieving the data and insert into table
# i value for xml data 
# j value printing number of values that are stored
for i, j in zip(data2, range(1, 31)):
    name = i.find('name').text
    hashtagSet = i.findall('hashtagSet')

    for k, l in zip(hashtagSet, range(1, 6)):
        hashtag1 = k.find('hashtag1').text
        
        try:
            hashtag2 = k.find('hashtag2').text
        except:
            hashtag2 = ""

        try:
            hashtag3 = k.find('hashtag3').text
        except:
            hashtag3 = ""

    # sql query to insert data into database
    data = """INSERT INTO cocktail(name,hashtag1,hashtag2,hashtag3) VALUES(%s,%s,%s,%s)"""
  
    # creating the cursor object
    c = conn.cursor()
      
    # executing cursor object
    c.execute(data, (name, hashtag1, hashtag2, hashtag3))
    conn.commit()
    print("cocktail tabelCocktail No-", j, " stored successfully")