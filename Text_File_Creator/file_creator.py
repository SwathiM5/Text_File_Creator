name = input("What's your name? \n")
color = input("Favorite color: ")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")
with open('example.txt', 'w') as file:
    file.write(f"{color} created this file")