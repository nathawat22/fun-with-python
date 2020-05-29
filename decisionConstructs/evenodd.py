# take user input for a positive number
userInput = input("Enter a positive number: ")

# convert user input to an integer
value = int(userInput)

# check and print if the value is an even or an odd number
if(value % 2 == 0):
    print(value, "is an even number.")
else:
    print(value, "is an odd number.")