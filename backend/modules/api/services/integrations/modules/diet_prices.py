from api.services.implementations.modules import diet, food_prices

def solve(answers, data):

    # First the food quantities need to be determined
    foods_quantities = diet.solve_diet(answers["min1"], data)

    # Then, with the quantities calculated, it is
    # possible to determine the prices from the most convenient source
    chosen_prices = food_prices.get_prices(foods_quantities)

    result = {
        'quant': foods_quantities,
        **chosen_prices
    }

    '''
    {
        "quant": {
            "I": 0,
            "II": 0,
            "III": 11
        },
        "total_price": 2409,
        "provider": "Local 1",
        "unit_prices": {
            "I": 321,
            "II": 391,
            "III": 219
        }
    }
    '''

    return result