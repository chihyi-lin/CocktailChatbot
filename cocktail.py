import re
import random
import mysql.connector


class CocktailBot:

    yes_response = ('yes', 'y', 'Yes', 'YES', "Y")

    def __init__(self):
        pass

    def sweet_fruity(self):
        hashtag = input(
            "Pick one with your intuition! 1)SUMMERTIME 2)TROPICAL 3)THE QUEEN 4)PARTY 5)GORGEOUS")
        if hashtag.lower() in ("1", "summetime"):
            # Daiquiri
            return
        elif hashtag.lower() in ("2", "tropical"):
            # Jungle bird
            return
        elif hashtag.lower() in ("3", "the queen", "queen"):
            # Margarita
            return
        elif hashtag.lower() in ("4", "party"):
            # Cosmopolitan
            return
        elif hashtag.lower() in ("5", "gorgeous"):
            # Aviation
            return
        else:
            return self.sweet_fruity()

    def sour_syrup(self):
        hashtag = input(
            "Pick one with your intuition! 1)THE QUEEN OF SOUR COCKTAIL 2)REFRESHING ")
        if hashtag.lower() in ("1", "the queen", "the queen of sour cocktail"):
            # margarita
            return
        elif hashtag.lower() in ("2", "refreshing"):
            # aviation
            return
        else:
            return self.sour_syrup()

    def boozy_gin(self):
        hashtag = input("Pick one with your intuition! 1)BOOZY 2)ELEGANT ")
        if hashtag.lower() in ("1", "boozy"):
            # negroni
            return
        elif hashtag.lower() in ("2", "elegant"):
            # dry martini
            return
        else:
            return self.sour_syrup()

    def sweet(self):
        juice = input("Would you like something fruity? 1)Yes 2)No ")
        if juice.lower() in ("1", "yes", "y"):
            # return Daiquiri, Jungle bird, Margarita, Cosmopolitan, Aviation
            return self.sweet_fruity()
        elif juice.lower() in ("2", "no", "n"):
            # return Irish Coffee
            return
        else:
            return self.sweet()

    def sour(self):
        vibe = input(
            "Added syrup or not? 1)YES, PLEASE! 2) NOPE")
        if vibe.lower() in ("1", "y", "yes"):
            # return Margarita, Aviation
            return self.sour_syrup()
        elif vibe.lower() in ("2", "n", "no", "nope"):
            # return Cosmopolitan
            return
        else:
            return self.sour()

    def bitter(self):
        pop = input(
            "Would you like to try the most popular cocktail in 2021? 1)YES 2)NO ")
        if pop.lower() in ("y", "yes"):
            # return old fashion
            return
        elif pop.lower() in ("n", "no"):
            # negroni
            return
        else:
            return self.bitter()

    def boozy(self):
        base = input("Gin base or Rye base? 1)GIN 2)RYE")
        if base.lower() in ("1", "gin"):
            # Negroni, Dry Martini
            return self.boozy_gin()
        elif base.lower() in ("2", "rye"):
            # Manhattan
            return

    def spicy(self):
        prefer = input(
            "Something healthy or something classic? 1)HEALTHY 2)CLASSIC ")
        if prefer.lower() in ("1", "healthy"):
            # bloody mary
            return
        elif prefer.lower() in ("2", "classic"):
            # old fashioned
            return
        else:
            return self.spicy()

    def flavor_preferance(self):
        flavor = input(
            "Do you want something 1)SWEET 2)SOUR 3)BITTER 4)BOOZY? 5)SPICY")
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
        name = input("Hi! Welcome to THE COCKTAIL WORLD! What is your name? ")

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
