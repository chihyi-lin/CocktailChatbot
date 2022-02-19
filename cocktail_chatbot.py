# conner database
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jenny152!",
    database="sys",
)
cursor = db.cursor()


class CocktailBot:

    yes_response = ('yes', 'y', 'Yes', 'YES', "Y")
    name = ""

    def __init__(self):
        pass
    # show results with sql queries

    def show(self, ingredient):
        print(f"Hey {self.name}! We recommend '{ingredient[0][0]}' for you!")
        # call base
        print(f"You will have {ingredient[0][1]} as your base.")
        # check if there are one or two more alcohol ingredients
        if len(ingredient[0][2]) > 0:
            if len(ingredient[0][3]) > 0:
                print(
                    f"You'll also need some {ingredient[0][2]} and {ingredient[0][3]}. ")
            else:
                print(f"You'll also need some {ingredient[0][2]}")
        # check if juice is needed in the selected cocktail
        if len(ingredient[0][4]) > 0:
            if len(ingredient[0][5]) > 0:
                print(
                    f"Then prepare some {ingredient[0][4]} and {ingredient[0][5]} juice.")
            else:
                print(f"Prepare some {ingredient[0][4]} juice.")
        # check if syrup is needed in the selected cocktail
        if len(ingredient[0][6]) > 0:
            print(f"And some {ingredient[0][6]} syrup as well.")
        # check if garnish is needed （one or two) in the selected cocktail
        if len(ingredient[0][7]) > 0:
            if len(ingredient[0][8]) > 0:
                print(
                    f"Don't forget to get some {ingredient[0][7]} and {ingredient[0][8]} for garnish.")
            else:
                print(
                    f"Don't forget to get some {ingredient[0][7]} for garnish.")
        # check if there is any other ingredients
        if len(ingredient[0][9]) > 0:
            print(
                f"At last, add some {ingredient[0][9]} and {ingredient[0][10]} to make it perfect!")
        print(
            f"Then you'll have a nice glass of {ingredient[0][0]}. Enjoy your cocktail!")

    # if sweet and juice prefered, ask which hashtag does the user prefer

    def sweet_fruity(self):
        hashtag = input(
            "Pick one with your intuition! 1)CLASSIC 2)TROPICAL 3)THE QUEEN 4)PARTY 5)GORGEOUS ")
        if hashtag.lower() in ("1", "classic"):
            base = input("Which base do you prefer? 1)WHITE RUM  2)TEQUILA ")
            # return sweet taste, juice added, hashtag = classic, white rum  -> Daiquiri
            if base.lower() in ("1", "rum", "white rum"):
                cursor = db.cursor()
                cursor.execute(
                    "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%classic%' OR c.hashtag2 LIKE '%classic%' OR c.hashtag3 LIKE '%classic%' ) AND NOT(i.juice1 = '') AND i.base = 'White Rum';")
                result = cursor.fetchall()
                return self.show(result)
            # return sweet taste, juice added, hashtag = classic, tequila -> Margarita
            elif base.lower() in ("2", "tequila"):
                cursor = db.cursor()
                cursor.execute(
                    "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%classic%' OR c.hashtag2 LIKE '%classic%' OR c.hashtag3 LIKE '%classic%' ) AND NOT(i.juice1 = '') AND i.base = 'Tequila';")
                result = cursor.fetchall()
                return self.show(result)
        elif hashtag.lower() in ("2", "tropical"):
            # return sweet taste, juice added, hashtag = tropical -> Jungle bird
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%tropical%' OR c.hashtag2 LIKE '%tropical%' OR c.hashtag3 LIKE '%tropical%' ) AND NOT(i.juice1 = '');")
            result = cursor.fetchall()
            return self.show(result)
        elif hashtag.lower() in ("3", "the queen", "queen"):
            # return sweet taste, juice added, hashtag = queen -> Margarita
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%queen%' OR c.hashtag2 LIKE '%queen%' OR c.hashtag3 LIKE '%queen%' ) AND NOT(i.juice1 = '');")
            result = cursor.fetchall()
            return self.show(result)
        elif hashtag.lower() in ("4", "party"):
            # return sweet taste, juice added, hashtag = party -> Cosmopolitan
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%party%' OR c.hashtag2 LIKE '%party%' OR c.hashtag3 LIKE '%party%' ) AND NOT(i.juice1 = '');")
            result = cursor.fetchall()
            return self.show(result)
        elif hashtag.lower() in ("5", "gorgeous"):
            # return sweet taste, juice added, hashtag = gorgeous -> Aviation
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sweet' OR f.taste2 = 'sweet') AND (c.hashtag1 LIKE '%gorgeous%' OR c.hashtag2 LIKE '%gorgeous%' OR c.hashtag3 LIKE '%gorgeous%' ) AND NOT(i.juice1 = '');")
            result = cursor.fetchall()
            return self.show(result)
        # if user's answer not related to the question, prompt the quesiton again
        else:
            return self.sweet_fruity()
    # if sour and syrup preferred, ask prefered hashtag

    def sour_syrup(self):
        hashtag = input(
            "Pick one with your intuition! 1)THE QUEEN OF SOUR COCKTAIL 2)REFRESHING ")
        if hashtag.lower() in ("1", "the queen", "the queen of sour cocktail"):
            # return sour taste, syrup added, hashtag = queen -> margarita
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sour' OR f.taste2 = 'sour') AND (c.hashtag1 LIKE '%queen%' OR c.hashtag2 LIKE '%queen%' OR c.hashtag3 LIKE '%queen%') AND NOT(i.syrup = '') ;")
            result = cursor.fetchall()
            return self.show(result)
        elif hashtag.lower() in ("2", "refreshing"):
            # return sour taste, syrup added, hashtag = refreshing -> aviation
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'sour' OR f.taste2 = 'sour') AND (c.hashtag1 LIKE '%refreshing%' OR c.hashtag2 LIKE '%refreshing%' OR c.hashtag3 LIKE '%refreshing%') AND NOT(i.syrup = '') ;")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.sour_syrup()
    # if boozy chosen, ask which base is prefered

    def boozy_gin(self):
        hashtag = input("Would you like dry or sweet vermouth! 1)DRY 2)SWEET ")
        if hashtag.lower() in ("1", "dry"):
            # return bozzy taste, gin added, dry vermouth -> dry martini
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'boozy' OR f.taste2 = 'boozy') AND (i.other1 LIKE '%dry%' OR i.other2 LIKE '%dry%');")
            result = cursor.fetchall()
            return self.show(result)
        elif hashtag.lower() in ("2", "sweet"):
            # return bozzy taste, gin added, sweet vermouth -> Negroni
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'boozy' OR f.taste2 = 'boozy') AND (i.other1 LIKE '%sweet%' OR i.other2 LIKE '%sweet%');")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.boozy_gin()

    # if user prefers sweet taste
    def sweet(self):
        prefer_juice = input("Would you like something fruity? 1)Yes 2)No ")
        if prefer_juice.lower() in ("1", "yes", "y"):
            return self.sweet_fruity()
        elif prefer_juice.lower() in ("2", "no", "n"):
            # return sweet taste, without juice -> Irish Coffee
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN sys.flavor f ON f.name = i.name WHERE i.juice1 = ''  AND f.taste1 = 'sweet' ;")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.sweet()

    # if user prefers sour, ask whether syrup is prefereed
    def sour(self):
        prefer_syrup = input(
            "Added syrup or not? 1)YES, PLEASE! 2)NOPE ")
        if prefer_syrup.lower() in ("1", "y", "yes"):
            return self.sour_syrup()
        elif prefer_syrup.lower() in ("2", "n", "no", "nope"):
            # return sour taste, without syrup -> Cosmopolitan
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN sys.flavor f ON f.name = i.name WHERE i.syrup = ''  AND (f.taste1 = 'sour' OR f.taste2 = 'sour') ;")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.sour()
    # if user prefers bitter

    def bitter(self):
        pop = input(
            "Would you like to try the most popular cocktail in 2021? 1)YES 2)NO ")
        if pop.lower() in ("1", "y", "yes"):
            # return bitter taste, hashtag = popular -> old fashion
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'bitter' OR f.taste2 = 'bitter') AND (c.hashtag1 LIKE '%popular%' OR c.hashtag2 LIKE '%popular%' OR c.hashtag3 LIKE '%popular%' ) ;")
            result = cursor.fetchall()
            return self.show(result)

        elif pop.lower() in ("1", "n", "no"):
            # return bitter taste, hashtag != popular -> negroni
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'bitter' OR f.taste2 = 'bitter') AND NOT(c.hashtag1 LIKE '%popular%' OR c.hashtag2 LIKE '%popular%' OR c.hashtag3 LIKE '%popular%' ) ;")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.bitter()
    # if user prefers boozy

    def boozy(self):
        prefer_base = input("Gin base or Rye base? 1)GIN 2)RYE ")
        if prefer_base.lower() in ("1", "gin"):
            return self.boozy_gin()
        elif prefer_base.lower() in ("2", "rye"):
            # return boozy taste, rye base -> Manhattan
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN sys.flavor f ON f.name = i.name WHERE (f.taste1 = 'boozy' OR f.taste2 = 'boozy') AND i.base = 'rye';")
            result = cursor.fetchall()
            return self.show(result)
    # if user prefers spicy

    def spicy(self):
        prefer = input(
            "Something healthy or something classic? 1)HEALTHY 2)CLASSIC ")
        if prefer.lower() in ("1", "healthy"):
            # return spicy taste, hashtag = health -> bloody mary
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'spicy' OR f.taste2 = 'spicy') AND (c.hashtag1 LIKE '%healthy%' OR c.hashtag2 LIKE '%healthy%' OR c.hashtag3 LIKE '%healthy%');")
            result = cursor.fetchall()
            return self.show(result)
        elif prefer.lower() in ("2", "classic"):
            # return spicy taste, hashtag = classic -> old fashioned
            cursor = db.cursor()
            cursor.execute(
                "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE (f.taste1 = 'spicy' OR f.taste2 = 'spicy') AND NOT (c.hashtag1 LIKE '%healthy%' OR c.hashtag2 LIKE '%healthy%' OR c.hashtag3 LIKE '%healthy%');")
            result = cursor.fetchall()
            return self.show(result)
        else:
            return self.spicy()

    # ask user's flavor preference
    def flavor_preferance(self):
        flavor = input(
            "Do you want something 1)SWEET 2)SOUR 3)BITTER 4)BOOZY 5)SPICY? ")
        if flavor.lower() in ("sweet", "1"):
            return self.sweet()
        elif flavor.lower() in ("sour", "2"):
            return self.sour()
        elif flavor.lower() in ("bitter", "3"):
            return self.bitter()
        elif flavor.lower() in ("boozy", "4"):
            return self.boozy()
        elif flavor.lower() in ("spicy", "5"):
            return self.spicy()

    # greeting to the user
    def greeting(self):
        # asking for user's name
        name = input("Hi! I'm your Sweet Bartender! What is your name? ")
        self.name = name
        ready = input(
            f"Hello, {name}! I will now recommend some cocktails to you base on your answers. Are you ready to start? (y/n) ")

        if ready in self.yes_response:
            print("Let's get started!")
            return self.flavor_preferance()
        else:
            print(f"See you next time, {name}.")
            return


a = CocktailBot()
a.greeting()
