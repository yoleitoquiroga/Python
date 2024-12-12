toppings = []


title = "\n\tenter your desired toppings, once youre finish type 'done'!".title()
prompt ="\nEnter your desired toppings: "
active = True
print(title)
while active:
    topping = input(prompt)
    if topping == 'done':
        print(f'\nyour pizza will have the following toppings: '.title())
        for item in toppings:
            print(f'{item.title()}')
        break
    if topping == '':
        continue
    
        
    
    else:
        toppings.append(topping)
        continue
     
       