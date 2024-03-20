from enum import Enum


class BrewMethod(Enum):
    DRIP = 1
    FRENCH_PRESS = 2
    ESPRESSO = 3


class BrewStrength(Enum):
    MILD = 18
    STANDARD = 15
    STRONG = 13
        

class Brew:
    def __init__(this,  serving=None, ratio=None):
        this.method = ""
        this.serving = serving or 150
        this.brew_ratio = ratio.value or 15
        this.water_absorption_amount = 2.3


    def get_recipe(this):
        coffee_amount = round(this.serving / this.brew_ratio, 1)
        total_water = round(this.serving + (coffee_amount * this.water_absorption_amount))
        
        return this.method, this.serving, coffee_amount, total_water, this.brew_ratio


    def __str__(this):
        recipe = this.get_recipe()
        return f"\n{recipe[0]} Recipe ({recipe[1]}ml)\n-------------------------------\nCoffee: {recipe[2]}g\nWater: {recipe[3]}ml\n"
    

class BrewDrip(Brew):
    pass

class BrewEspress(Brew):
    pass

class BrewFrenchPress(Brew):
    def __init__(this, serving, ratio):
        super().__init__(serving, ratio)
        this.method = "French Press"



class BrewFactory:
    @staticmethod
    def create_brew(method:BrewMethod, serving:int, strengh:BrewStrength):

        if method == BrewMethod.DRIP:
            return Brew(serving, strengh)
        
        elif method == BrewMethod.FRENCH_PRESS:
            return BrewFrenchPress(serving, strengh)
        
