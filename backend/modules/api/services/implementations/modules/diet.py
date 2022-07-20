import pyomo.environ as pyo
import json


def solve_diet(min1, api_input):

    '''
    Creacion modelo
    '''

    model = pyo.ConcreteModel()

    # Conjuntos

    model.m = pyo.Set(initialize=api_input['nutrients'])
    model.n = pyo.Set(initialize=api_input['foods'])

    # Parametros

    a = {}
    for i in model.m:
        for j in model.n:
            a[i, j] = api_input['nutrients_per_food'][i][j]
    model.a = pyo.Param(model.m, model.n, initialize=a)

    b = {}
    for i in model.m:
        b[i] = api_input['min_nutrients_units'][i]
    model.b = pyo.Param(model.m, initialize=b)

    c = {}
    for j in model.n:
        c[j] = api_input['food_weight'][j]
    model.c = pyo.Param(model.n, initialize=c)

    # Variables

    model.x = pyo.Var(model.n, domain=pyo.NonNegativeIntegers)

    # Funcion objetivo

    model.obj = pyo.Objective(rule=pyo.summation(model.c, model.x))

    # Restricciones

    def restriccion0(modelo, i):
        return sum(modelo.a[i, j] * modelo.x[j] for j in model.n) >= modelo.b[i]

    model.constraint1 = pyo.Constraint(model.m, rule=restriccion0)

    """If there is input of wanting to have a minimum of 1 unit per food type,
    the restriction will be added."""
    if min1:
        def restriccion1(modelo, j):
            return modelo.x[j] >= 1

        model.constraint2 = pyo.Constraint(model.n, rule=restriccion1)

    # Ejecutar el modelo

    opt = pyo.SolverFactory('glpk')
    opt.solve(model)

    # Imprimir resultados
    """
    print('# de unidades por comida en la dieta:')
    for j in model.n:
        print('{}\t{}'.format(j, model.x[j].value))
    """

    return {
        j: int(model.x[j].value) for j in model.n
    }

'''
test = {
    'nutrients': ['a', 'b'],
    'foods': ['I', 'II', 'III'],
    'nutrients_per_food': {
        'a': {
            'I': 20,
            'II': 16,
            'III': 30
        },
        'b': {
            'I': 38,
            'II': 1,
            'III': 23
        }
    },
    'min_nutrients_units': {
        'a': 100,
        'b': 250
    },
    'food_weight': {
        'I': 4000,
        'II': 5500,
        'III': 1000
    }
}

print(json.dumps(solve_diet(False, test), indent=4))
'''