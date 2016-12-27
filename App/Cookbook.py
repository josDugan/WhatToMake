class Recipe:
    def __init__(self, title, ingredients, instructionPath, meal):
        self.title = title
        self.ingredients = ingredients
        self.instructionPath = instructionPath
        self.meal = meal


def readFile(path):
    with open(path, mode='rt') as reader:
        return reader.readlines()

fridgeArr = readFile("/Users/markhauenstein/PycharmProjects/WhatToCook/App/fridge.csv")

cookbookArr = readFile("/Users/markhauenstein/PycharmProjects/WhatToCook/App/cookbook.csv")

fridge = {}
cookbook = []

for item in fridgeArr:
    food = item.split(",")[0]
    amount = item.split(",")[1]
    uom = item.split(",")[2]
    fridge[food] = [amount, uom]



for recipe in cookbookArr:
    x = recipe.split("|")
    y = x[1].split(",")
    ingredientDict = {}
    for z in y:
        ingredientDict[z.split(":")[0]] = z.split(":")[1]
    cookbook.append(Recipe(x[0], ingredientDict, x[2], x[3]))


def updateFridge():
    with open("/Users/markhauenstein/PycharmProjects/WhatToCook/App/fridge.csv", mode='w') as fridgeWriter:
        for item in fridge:
            fridgeWriter.write(item + "," + str(fridge[item][0]) + "," + fridge[item][1] + "/n")

def ICanMake(recipe):
    numIngredientsNeeded = len(recipe.ingredients)
    for ingredient in recipe.ingredients.keys():
        if fridge[ingredient][0] >= recipe.ingredients[ingredient]:
            numIngredientsNeeded -= 1
    if numIngredientsNeeded == 0:
        return True

def printAllICanMake(meal="all"):
    for recipe in cookbook:
        if meal != "all":
            if ICanMake(recipe) & (recipe.meal == meal):
                print(recipe.title)
        elif ICanMake(recipe):
            print(recipe.title)


def makeRecipe(name):
    for recipe in cookbook:
        if recipe.title == name:
            makeThis = recipe
            break
    if ICanMake(makeThis):
        for ingredient in makeThis.ingredients:
            fridge[ingredient[0]] -= makeThis.ingredients[ingredient]
    updateFridge()


def addToFridge(name, amount):
    if fridge.__contains__(name):
        fridge[name][0] += amount
    else:
        uom = input("Unrecognized name '" + name + "' enter Unit of Measurement\n")
        fridge[name] = [int(amount), uom]
    updateFridge()


def printRecipeInstructions(recipeName):
    for recipe in cookbook:
        if recipe.title == recipeName:
            makeThis = recipe
            break
    return "".join(readFile(makeThis.instructionPath))





