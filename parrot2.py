prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "

message = "" #empty variable to store user's input
while message != 'quit': #while condition
    message = input(prompt) #input
    if message != 'quit': # variable to be compared with the while condition.
        print(message) #print input as long as it does not match condition.

# Using a flag
print("\n\tThis is an example using a flag.".upper())

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "

active = True #starts the program in an active state.
while active:
    message = input(prompt) #input

    if message == 'quit': # comparison made in this stage between input and 
        #value 'quit' rathen that in the while portion.
        #thus allowing for implementation of more conditions that could set the
        #flag to False.
        active = False #in this case if the message is 'quit', the flag becomes 
        #false.
    if message == 'exit':
        active = False
    else:
        print(message) #print input as long as flag remains True.

