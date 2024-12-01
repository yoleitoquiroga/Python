pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}
print(f'You ordered a {pizza["crust"]}-crust pizza with the following toppings:')
for toppings in pizza['toppings']:
    print(f'\t{toppings}')
