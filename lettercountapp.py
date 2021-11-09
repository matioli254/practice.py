#Letter count app
print("welcome to the letter count app")

#Get user input.
name = input("\nEnter your name: ").title().strip()
print("Hello, " + name)

#goal of the program
print("I can count the occurence of a letter in a given message.")
message = input("Enter the message: ")
letter = input("What letter would you like to count: ")

#standardize 
message = message.lower()
letter = letter.lower()

#count the letter
letter_count = message.count(letter)

#output
print(name + "your message has " + str(letter_count) + "letters in it.")






