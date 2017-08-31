# standard way of doing while loops
number_of_items = int(input("Please enter the number of items: "))
while number_of_items <= 0:
    print("Invalid number of items! Try again.")
    number_of_items = int(input("Please enter the number of items: "))

total_price = 0

# use for loops for a fixed number of iterations
for i in range(number_of_items):
    total_price = total_price + float(input("Please enter price of item: $"))

if total_price > 100:
    total_price = total_price * 0.9

print("In total that amounts to: ${:.2f}".format(total_price))
