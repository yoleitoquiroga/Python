#newline and tab spaces
print("Python")
print("\tPython")
print("languages:\nPython\nC\nJavaScript")
print("languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping whitespace
favourite_language='python '
print(favourite_language)
print(favourite_language.rstrip())
favourite_language=favourite_language.rstrip() #associating the variable with the stripped value of the variable, this is done to eliminate the whitespace at the end npermanently.
print(favourite_language.title().rstrip()) #uppercase letter for Python
