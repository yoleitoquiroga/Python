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
print("\nWe have an exciting data base about peoples' favourites languages!".title())
name=input("\nEnter the name of your interest: ").lower()
if name in fav_language:
    print(f"{name.title().rstrip()}'s favourite language is {fav_language[name]}.")
else:
    print(f"I'm really sorry but {name.title().rstrip()} is not registered in our database.")
#both methods will print the keys, the difference is hot the information will be presented.
print(fav_language.keys())
for key in fav_language:
    print(key)

for key, value in fav_language.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for key in fav_language.keys():
    print(f'Hi {key.title()}!')
    if key in friends:
        #lang_ = fav_language[key].title()
        print(f'\t{key.title()}, thank you for taking the survey.')

#organizing keys in alphabetical and reverse alphabetical order.
for key in sorted(fav_language.keys()):
    print (key)
for key in sorted(fav_language.keys(), reverse=True):
    print(key)