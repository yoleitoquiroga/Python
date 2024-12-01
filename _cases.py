#personal message
name='Eric'
message=f'Hello {name}, would you like to learn some Python today?'
print(message)

#name cases
first_name='LeoNaRdO'
last_name='QuIrOgA'
full_name=f'{first_name} {last_name}'
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

#famous quote
author='Leonardo Quiroga'
quote='once said, "You need to learn how to eat shit but never develop a taste for it."'
final_message=f'{author} {quote}'
print(final_message)

#stripping names
name='    Leonardo Quiroga        '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#file extensions
filename="Phyton_notes.txt"
print(filename)
print(filename.removesuffix('.txt'))

