fav_language = {
    'armando' : 'spanish',
    'berenice' : 'italian',
    'camilo' : 'catalan',
    'daniela' : 'french',
    'eduardo' : 'english',
    'felipe': 'greek',
    }
friends = ['armando', 'camilo', 'felipe']
language= fav_language ['armando'].title()
print(f"Armando's favourite language is {language}.")
#accessing a dictionary by providing input trhough terminal
title = "\n\tWe have an exciting data base about peoples' favourites languages!".title()
prompt ="\nEnter the name of your interest: "
active = True
print(title)
while active:
    name = input(prompt)
    if name == 'quit':
        active = False
        break
    if name not in fav_language:
        print(f"\nI'm really sorry but {name.title().rstrip()} is not registered 
        in our database.") #input does not match dictionary content. Loops back to input.
    
    else:
        print(f"{name.title().rstrip()}'s favourite language is {fav_language[name]}.".title())
        #once condition has been met, program ends
        active = False #this flag will cause the program tio end (optional)
        #depending on the requierements of the program this one will end or not.

       