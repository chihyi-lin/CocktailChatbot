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

# in our xml file cocktail is the root for all cocktail data.
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

for i, j in zip(data2, range(1, 31)):
    name = i.find('name').text
    ingredient = i.findall('ingredient')

    for k, l in zip(ingredient, range(1, 5)):
        alcohol = k.findall('alcohol')

        for m, n in zip(alcohol, range(1, 7)):
            base = m.find('base').text
            try:
                other1 = m.find('other1').text
            except:
                other1 = ""

            try:
                other2 = m.find('other2').text
            except:
                other2 = ""

        additional = k.findall('additional')

        for o, p in zip(additional, range(1, 8)):
            try:
                juice1 = o.find('juice1').text
            except:
                juice1 = ""

            try:
                juice2 = o.find('juice2').text
            except:
                juice2 = ""

            try:
                syrup = o.find('syrup').text
            except:
                syrup = ""

            try:
                garnish1 = o.find('garnish1').text
            except:
                garnish1 = ""

            try:
                garnish2 = o.find('garnish2').text
            except:
                garnish2 = ""

            try:
                other_add1 = o.find('other_additional1').text
            except:
                other_add1 = ""

            try:
                other_add2 = o.find('other_additional2').text
            except:
                other_add2 = ""

    data = """INSERT INTO ingredient(name,base,other1,other2,juice1,juice2,syrup,garnish1,garnish2,other_add1,other_add2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    c = conn.cursor()

    c.execute(data, (name, base, other1, other2, juice1, juice2, syrup, garnish1, garnish2, other_add1, other_add2))
    conn.commit()
    print("cocktail tableIngredient No-", j, " stored successfully")

for i, j in zip(data2, range(1, 31)):
    name = i.find('name').text
    flavor = i.findall('flavor')

    for k, l in zip(flavor, range(1, 6)):
        taste1 = k.find('taste1').text

        try:
            taste2 = k.find('taste2').text
        except:
            taste2 = ""

    data = """INSERT INTO flavor(name,taste1,taste2) VALUES(%s,%s,%s)"""

    c = conn.cursor()

    c.execute(data, (name, taste1, taste2))
    conn.commit()
    print("cocktail tabelflavor No-", j, " stored successfully")

for i, j in zip(data2, range(1, 31)):
    name = i.find('name').text
    flavor = i.findall('flavor')

    for k, l in zip(flavor, range(1, 6)):
        try:
            taste3 = k.find('taste3').text
        except:
            taste3 = ""

        try:
            taste4 = k.find('taste4').text
        except:
            taste4 = ""

    data = """INSERT INTO flavor_minor(name,taste3,taste4) VALUES(%s,%s,%s)"""

    c = conn.cursor()

    c.execute(data, (name, taste3, taste4))
    conn.commit()
    print("cocktail tabelflavor_minor No-", j, " stored successfully")
