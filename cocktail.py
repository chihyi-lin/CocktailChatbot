import re
import random
import mysql.connector


class CocktailBot:

    yes_response = ('yes', 'y', 'Yes', 'YES', "Y")

    def __init__(self):
        pass

    def sweet(self):
        pass

    def sour(self):
        pass

    def bitter(self):
        pass

    def fresh(self):
        pass

    def flavor_preferance(self):
        flavor = input("Do you want something 1)SWEET 2)SOUR 3)BITTER 4)FRESH")
        if flavor == "1":
            return self.sweet()
        elif flavor == "2":
            return self.sour()
        elif flavor == "3":
            return self.bitter()
        elif flavor == "4":
            return self.fresh()

    # greeting to the user
    def greeting(self):
        name = input("Hi! Welcome to THE COCKTAIL WORLD! What is your name?")

        ready = input(
            f"Hello, {name}! I will now recommend some cocktails to you base on your answers. Are you ready to start? (y/n)")

        if ready in self.yes_response:
            print("Let's get started!")
            return self.flavor_preferance()
        else:
            print("See you next time!")
            return
