message = input("Tell me something, and I will repeat it back to you: ")
#the variable "message" is created to store the users input.
print(message)
#variable "message" is called in the print call.

prompt = "This will be a two line prompt, let me welcome you."
prompt += "\nFirst of, what is your name: "
name  = input(prompt).lower().strip()
print(f"Nice to have you here with us {name.title()}")