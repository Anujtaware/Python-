#8) accept a character and display whether it is upper case or lower case or not an alphabet.

char=input("enter a character")
uppercase=char.upper()
lowercase=char.lower()
if char==uppercase:
    print("it is a upper case")
elif char==lowercase:
    print("it is a lower case")
    