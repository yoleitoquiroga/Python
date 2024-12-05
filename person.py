#dictionary nested in a dictionary.
users = {
    'cecilacajita' : {#single key with multiple values.
        'first_name' : 'carmen',
        'last_name' : 'munoz',
        'age' : 74,
        'dob' : 'feb 2, 1950',
        'nationality' : 'colombian',
        },
    'yoleitoquiroga' : {
        'first_name' : 'leonardo',
        'last_name' : 'quiroga',
        'age' : 32,
        'dob' : 'nov 18, 1992',
        'nationality' : 'colombian'
        },
    'ralbog' : {
        'first_name' : 'rodolfo',
        'last_name' : 'bogota',
        'age' : 31,
        'dob' : 'jan 6, 1993',
        'nationality' : 'colombian'
        }
    
    }



#accessing a dictionary by providing input trhough terminal
print("\n\tactive users".title())
name=input("\nEnter the name of your interest: ").lower().strip()

for key, value in users.items():
    if value['first_name'] == name:
        print(f'\nUsername: {key}')
        print(f'full name: {value['first_name']} {value['last_name']}'.title())
        print(f'Age: {value['age']}')
        print(f'date of birth: {value['dob']}'.title())
        print(f'nationality: {value['nationality']}'.title())
        break
else:  
    print(f'The name {name.title()} is not registered.')


#for username, user_info in users.items():#assigning variables for key and values.
#    print(f'\n{username}:')#key
 #   full_name = f'{user_info['first_name']} {user_info['last_name']}'#value
  #  age = user_info['age']#value
   # dob = user_info['dob']#value
    #nationality = user_info['nationality']#value
    
    #since there is more than one value per key, it is necessary to define
    #which value is being called when using the variable user_info

    #dictionary being printed with all of the information enclosed in the key-values set.
#    print(f'\tFull Name: {full_name}'.title())
 #   print(f'\tAge: {age}')
  #  print(f'\tDate Of Birth: {dob}'.title())
   # print(f'\tNationality: {nationality.title()}')
