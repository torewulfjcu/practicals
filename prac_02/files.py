# Program that asks the user for their name and stores it in name.txt
name = input("Please enter your name: ")
out_file_username = open("name.txt", "w")
print(name, file=out_file_username)
out_file_username.close()

# Program that opens “name.txt” and reads the name (as above) then prints,
# “Your name is Bob” (or whatever the name is in the file).

in_file_username = open("name.txt", "r")
name = in_file_username.read()
print("Your name is: ", name, sep="")
in_file_username.close()

# Create a text file called “numbers.txt”. Put the numbers 17 and 42 on separate lines in the file and save it:
# 17
# 42
# Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
# result, which should be… 59.
# Now extend your program so that it can print the total for a file containing any number of numbers.

sum = 0
in_file_numbers = open("numbers.txt", "r")
numbers = in_file_numbers.readlines()
for i in range(len(numbers)):
    sum = sum + int(numbers[i])
print(sum)

in_file_numbers.close()