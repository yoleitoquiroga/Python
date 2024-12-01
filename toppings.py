requested_toppings='mushrooms'
if requested_toppings != 'anchovies': #in this case the expression evaluates to 
    #true since both sides of the inequality operator are different.
    print("Hold the anchovies!")

#checking if a value is IN a list
requiered_toppings=['pineapple','mushrooms','beef','tomatoes','onions']
topping='sausage'
if topping in requiered_toppings:
        print(f'{topping.title()} is in the list.')
else:
        print(f'{topping.title()} is not in the list')

#checking if a value is NOT in a list
requiered_toppings=['pineapple','mushrooms','beef','tomatoes','onions']
topping='sausage'
if topping not in requiered_toppings:
        print(f'Would you like to add {topping.title()} to the list?')
else:
        print(f'{topping.title()} is already in the list')