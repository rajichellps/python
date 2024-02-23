item_name = input("enter name of the item here: ")
item_cost = float(input("enter cost of the item here: "))
item_number = int(input("enter number of the item here: "))

total_cost = item_cost * item_number

#print(total_cost)

print(f'The total cost of {item_number} {item_name}s is {total_cost:.2f}')

if total_cost > 100:
    total_cost *= 0.75
    print(f'The discounted cost of {item_number} {item_name}s is {total_cost:.2f}')
   
elif total_cost > 90:
    total_cost *= 0.9
    print(f'The discounted cost of {item_number} {item_name}s is {total_cost:.2f}')
   
else:
    total_cost *= 0.95
    print(f'The discounted cost of {item_number} {item_name}s is {total_cost:.2f}')
   
entered_name = input("Enter your name here: ")
entered_age = int(input("Enter your age here: "))

print(f"Your name is {entered_name.upper():=^20} and your age is {entered_age:.4f}")

floating_number = 12345.5678
print(f"Comma as thousand separators and two decimals: {floating_number:,.2f}")

#f" makes everything string,
#.upper() makes everything caps,
#:=^ followed by number puts word in center of hyphens,
#:.2f means the decimals are limited to 2 or the number specified
