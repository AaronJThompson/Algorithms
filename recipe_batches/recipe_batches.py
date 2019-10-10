#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  lowest_num = None
  for key in recipe:
    if key in ingredients.keys():
      amt = math.floor(ingredients[key] / recipe[key])
      if lowest_num is None:
        lowest_num = amt
      elif lowest_num > amt:
        lowest_num = amt
    else:
      return 0
  return lowest_num



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))