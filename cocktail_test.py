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
    param = {}

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

    def result(self):
        result_query = "SELECT i.* FROM sys.ingredient i INNER JOIN  sys.flavor f ON f.name = i.name INNER JOIN sys.cocktail c ON i.name = c.name WHERE"
        if "taste" in self.param.keys():
            result_query += "(f.taste1 = '{}' OR f.taste2 = '{}')".format(
                self.param.get('taste'), self.param.get('taste'))
        if "hashtag" in self.param.keys():
            result_query += "AND (c.hashtag1 LIKE '%{}%' OR c.hashtag2 LIKE '%{}%' OR c.hashtag3 LIKE '%{}%')".format(
                self.param.get('hashtag'), self.param.get('hashtag'), self.param.get('hashtag'))
        if "not hashtag" in self.param.keys():
            result_query += "AND NOT (c.hashtag1 LIKE '%{}%' OR c.hashtag2 LIKE '%{}%' OR c.hashtag3 LIKE '%{}%')".format(
                self.param.get('not hashtag'), self.param.get('not hashtag'), self.param.get('not hashtag'))
        if "base" in self.param.keys():
            result_query += "AND i.base = '{}'".format(self.param.get("base"))
        if "syrup" in self.param.keys():
            if self.param.get("syrup") == "no":
                result_query += "AND i.syrup = ''"
            else:
                result_query += "AND NOT i.syrup = ''"
        if "juice" in self.param.keys():
            if self.param.get("juice") == "no":
                result_query += "AND i.juice1 = ''"
            else:
                result_query += "AND NOT i.juice1 = ''"
        if "other" in self.param.keys():
            result_query += "AND (i.other1 LIKE '%{}%' OR i.other2 LIKE '%{}%')".format(
                self.param.get("other"), self.param.get("other"))
        cursor = db.cursor()
        cursor.execute(result_query)
        result = cursor.fetchall()
        return self.show(result)

    # if sweet and juice prefered, ask which hashtag does the user prefer

    def sweet_fruity(self):
        hashtag = input(
            "Pick one with your intuition! 1)CLASSIC 2)TROPICAL 3)THE QUEEN 4)PARTY 5)GORGEOUS ")
        if hashtag.lower() in ("1", "classic"):
            self.param['hashtag'] = "classic"
            base = input("Which base do you prefer? 1)WHITE RUM  2)TEQUILA ")
            # return sweet taste, juice added, hashtag = classic, white rum  -> Daiquiri
            if base.lower() in ("1", "rum", "white rum"):
                self.param["base"] = "White rum"
                return self.result()
            # return sweet taste, juice added, hashtag = classic, tequila -> Margarita
            elif base.lower() in ("2", "tequila"):
                self.param['base'] = "tequila"
                return self.result()
        elif hashtag.lower() in ("2", "tropical"):
            # return sweet taste, juice added, hashtag = tropical -> Jungle bird
            self.param["hashtag"] = "tropical"
            return self.result()
        elif hashtag.lower() in ("3", "the queen", "queen"):
            # return sweet taste, juice added, hashtag = queen -> Margarita
            self.param['hashtag'] = "queen"
            return self.result()
        elif hashtag.lower() in ("4", "party"):
            # return sweet taste, juice added, hashtag = party -> Cosmopolitan
            self.param['hashtag'] = "party"
            return self.result()
        elif hashtag.lower() in ("5", "gorgeous"):
            # return sweet taste, juice added, hashtag = gorgeous -> Aviation
            self.param["hashtag"] = "gorgeous"
            return self.result()
        # if user's answer not related to the question, prompt the quesiton again
        else:
            return self.sweet_fruity()
    # if sour and syrup preferred, ask prefered hashtag

    def sour_syrup(self):
        hashtag = input(
            "Pick one with your intuition! 1)THE QUEEN OF SOUR COCKTAIL 2)REFRESHING ")
        if hashtag.lower() in ("1", "the queen", "the queen of sour cocktail"):
            # return sour taste, syrup added, hashtag = queen -> margarita
            self.param["hashtag"] = "queen"
            return self.result()
        elif hashtag.lower() in ("2", "refreshing"):
            self.param["hashtag"] = "refreshing"
            return self.result()
        else:
            return self.sour_syrup()
    # if boozy chosen, ask which base is prefered

    def boozy_gin(self):
        hashtag = input("Would you like dry or sweet vermouth! 1)DRY 2)SWEET ")
        if hashtag.lower() in ("1", "dry"):
            # return bozzy taste, gin added, dry vermouth -> dry martini
            self.param['other'] = "dry"
            return self.result()
        elif hashtag.lower() in ("2", "sweet"):
            # return bozzy taste, gin added, sweet vermouth -> Negroni
            self.param['other'] = "sweet"
            return self.result()
        else:
            return self.boozy_gin()

    # if user prefers sweet taste
    def sweet(self):
        prefer_juice = input("Would you like something fruity? 1)Yes 2)No ")
        if prefer_juice.lower() in ("1", "yes", "y"):
            self.param["juice"] = "yes"
            return self.sweet_fruity()
        elif prefer_juice.lower() in ("2", "no", "n"):
            # return sweet taste, without juice -> Irish Coffee
            self.param["juice"] = "no"
            return self.result()
        else:
            return self.sweet()

    # if user prefers sour, ask whether syrup is prefereed
    def sour(self):
        prefer_syrup = input(
            "Added syrup or not? 1)YES, PLEASE! 2)NOPE ")
        if prefer_syrup.lower() in ("1", "y", "yes"):
            self.param['syrup'] = "yes"
            return self.sour_syrup()
        elif prefer_syrup.lower() in ("2", "n", "no", "nope"):
            # return sour taste, without syrup -> Cosmopolitan
            self.param['syrup'] = "no"
            return self.result()
        else:
            return self.sour()
    # if user prefers bitter

    def bitter(self):
        pop = input(
            "Would you like to try the most popular cocktail in 2021? 1)YES 2)NO ")
        if pop.lower() in ("1", "y", "yes"):
            # return bitter taste, hashtag = popular -> old fashion
            self.param['hashtag'] = 'popular'
            return self.result()

        elif pop.lower() in ("2", "n", "no"):
            # return bitter taste, hashtag != popular -> negroni
            self.param['not hashtag'] = 'popular'
            return self.result()
        else:
            return self.bitter()
    # if user prefers boozy

    def boozy(self):
        prefer_base = input("Gin base or Rye base? 1)GIN 2)RYE ")
        if prefer_base.lower() in ("1", "gin"):
            self.param['base'] = "gin"
            return self.boozy_gin()
        elif prefer_base.lower() in ("2", "rye"):
            # return boozy taste, rye base -> Manhattan
            self.param['base'] = 'rye'
            return self.result()
    # if user prefers spicy

    def spicy(self):
        prefer = input(
            "Something healthy or something classic? 1)HEALTHY 2)CLASSIC ")
        if prefer.lower() in ("1", "healthy"):
            self.param["hashtag"] = "healthy"
            # return spicy taste, hashtag = health -> bloody mary
            return self.result()
        elif prefer.lower() in ("2", "classic"):
            self.param["hashtag"] = "classic"
            # return spicy taste, hashtag = classic -> old fashioned
            return self.result()
        else:
            return self.spicy()

    # ask user's flavor preference
    def flavor_preferance(self):
        flavor = input(
            "Do you want something 1)SWEET 2)SOUR 3)BITTER 4)BOOZY 5)SPICY? ")
        if flavor.lower() in ("sweet", "1"):
            self.param['taste'] = "sweet"
            return self.sweet()
        elif flavor.lower() in ("sour", "2"):
            self.param['taste'] = "sour"
            return self.sour()
        elif flavor.lower() in ("bitter", "3"):
            self.param['taste'] = "bitter"
            return self.bitter()
        elif flavor.lower() in ("boozy", "4"):
            self.param['taste'] = "boozy"
            return self.boozy()
        elif flavor.lower() in ("spicy", "5"):
            self.param['taste'] = "spicy"
            return self.spicy()
        else:
            return self.flavor_preferance()
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
