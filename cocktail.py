import re
import random
import mysql.connector


class CocktailBot:

    yes_response = ('yes', 'y', 'Yes', 'YES', "Y")

    def __init__(self):
        pass

    def sweet(self):
        juice = input("1)LIME or 2)CRANBERRY? ")
        if juice.lower() in ("1", "lime"):
            return
        elif juice.lower() in ("2", "cramberry"):
            return
        else:
            return self.sweet()

    def sour(self):
        vibe = input(
            "Do you want to have the cocktail at a (1 NICE LOUNGE BAR  or 2)SUMMERTIME BEACH PARTY")
        if vibe.lower() in ("1", "bar", "lounge bar"):
            return
        elif vibe.lower() in ("2", "summertime beach party", "summertime", "beach party", "party"):
            return
        else:
            return self.sour()

    def bitter(self):
        juice = input(
            "Would you like some fruit flavor in your drink? 1)YES 2)NO ")
        if juice.lower() in ("y", "yes"):
            return
        elif juice.lower() in ("n", "no"):
            return
        else:
            return self.bitter()

    def boozy(self):
        pass

    def flavor_preferance(self):
        flavor = input(
            "Do you want something 1)SWEET 2)SOUR 3)BITTER 4)BOOZY? ")
        if flavor.lower() in ("sweet", "1"):
            return self.sweet()
        elif flavor.lower() in ("sour", "2"):
            return self.sour()
        elif flavor.lower() in ("bitter", "3"):
            return self.bitter()
        elif flavor.lower() in ("boozy", "4"):
            return self.boozy()

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
