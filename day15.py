import re
import itertools


class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def get_decoded_ingredient(line):
    regexp = re.compile('[a-zA-Z]+\: capacity (-?[0-9]+), durability (-?[0-9]+), flavor (-?[0-9]+), texture (-?[0-9]+), calories (-?[0-9]+)')
    m = regexp.match(line)
    return Ingredient(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))


def get_recipe_score(recipe):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for ingredient, spoons in recipe:
        capacity += ingredient.capacity * spoons
        durability += ingredient.durability * spoons
        flavor += ingredient.flavor * spoons
        texture += ingredient.texture * spoons

    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)

    return capacity * durability * flavor * texture


def day15_1():
    total_spoons = 100
    max_score = 0
    ingredients = []
    with open('data/15') as data:
        for line in data:
            ingredient = get_decoded_ingredient(line)
            ingredients.append(ingredient)

    for ing in ingredients:
        recipe = [(ing, total_spoons)]
        score = get_recipe_score(recipe)
        max_score = max(score, max_score)

    for ings in itertools.combinations(ingredients, 2):
        for spoons0 in range(1, total_spoons - 1):
            recipe = [(ings[0], spoons0), (ings[1], total_spoons - spoons0)]
            score = get_recipe_score(recipe)
            max_score = max(score, max_score)

    for ings in itertools.combinations(ingredients, 3):
        for spoons0 in range(1, total_spoons - 2):
            for spoons1 in range(1, total_spoons - spoons0 - 1):
                recipe = [(ings[0], spoons0), (ings[1], spoons1), (ings[2], total_spoons - spoons0 - spoons1)]
                score = get_recipe_score(recipe)
                max_score = max(score, max_score)

    for ings in itertools.combinations(ingredients, 4):
        for spoons0 in range(1, total_spoons - 3):
            for spoons1 in range(1, total_spoons - spoons0 - 1):
                for spoons2 in range(1, total_spoons - spoons0 - spoons1 - 1):
                    recipe = [(ings[0], spoons0), (ings[1], spoons1), (ings[2], spoons2), (ings[3], total_spoons - spoons0 - spoons1 - spoons2)]
                    score = get_recipe_score(recipe)
                    max_score = max(score, max_score)

    print('mscore =', max_score)


day15_1()
