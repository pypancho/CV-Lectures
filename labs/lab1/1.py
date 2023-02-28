# Practice 1
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num = input("Enter a number: ")
num = int(num)
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")