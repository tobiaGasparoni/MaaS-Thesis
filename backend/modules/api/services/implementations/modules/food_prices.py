from sys import maxsize
from random import randrange

GLOBAL = 'Global'
LOCAL_1 = 'Local 1'
LOCAL_2 = 'Local 2'

"""
dictionary = {
    'source': COMPANY,
    'foods': ['I', 'II', 'III']
}
"""

def total_price(food_quantities, unit_price):
    tot = 0

    for prod_name in food_quantities.keys():
        tot += food_quantities[prod_name] * unit_price[prod_name]

    return tot

def get_prices(foods):
    min_price = maxsize
    provider = ''
    min_unit_prices = dict()

    unit_prices = [
        (GLOBAL, get_prices_global(foods)),
        (LOCAL_1, get_prices_local_1(foods)),
        (LOCAL_2, get_prices_local_2(foods))
    ]

    for unit_price in unit_prices:
        total = total_price(foods, unit_price[1])
        if total < min_price:
            min_price = total
            provider = unit_price[0]
            min_unit_prices = unit_price[1]

    return {
      'total_price': min_price,
      'provider': provider,
      'unit_prices': min_unit_prices
    }

# Replaces web scraping over the prices for the products in the global market
def get_prices_global(foods):
    global_prices = {
        'I': randrange(250, 400),
        'II': randrange(350, 500),
        'III': randrange(150, 300),
        'IV': randrange(400, 600),
        'V': randrange(80, 150),
        'VI': randrange(700, 830)
    }
    return {key: value for key, value in global_prices.items() if key in foods}

# Replaces web scraping over the prices for the products in one local market
def get_prices_local_1(foods):
    local_prices = {
        'I': randrange(300, 400),
        'II': randrange(350, 450),
        'III': randrange(175, 275),
        'IV': randrange(400, 450),
        'V': randrange(195, 245),
        'VI': randrange(700, 800)
    }
    return {key: value for key, value in local_prices.items() if key in foods}

# Replaces web scraping over the prices for the products in another local market
def get_prices_local_2(foods):
    personal_prices = {
        'I': randrange(250, 350),
        'II': randrange(400, 500),
        'III': randrange(175, 275),
        'IV': randrange(450, 550),
        'V': randrange(95, 195),
        'VI': randrange(730, 830)
    }
    return {key: value for key, value in personal_prices.items() if key in foods}
