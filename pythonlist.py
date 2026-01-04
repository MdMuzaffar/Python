
values = [x + 1 for x in range(10)]
print(values)


# find even values from list

envens = []
for number in range(10):
    is_even = number % 2 == 0
    if is_even:
        envens.append(number)
        print(number)

evens = [number for number in range(10) if number % 2 == 0]
print(evens)

# filter the list with starting with 'A' and end with 'Y'

options = ["any", "apple", "boy", "ant", "camel", ""]
valid_string = []

for string in options:
    if len(string) <= 1:
        continue
    if string[0] != 'a':
        continue
    if string[-1] != 'y':
        continue
    valid_string.append(string)

# print(valid_string)

valid_string = [string for string in options
                if len(string) >= 2
                if string[0] == 'a'
                if string[-1] == 'y'
                ]
print(valid_string)


# nested list comprehension - Flattening a Matrix(list of lists)


matrix = [[1, 2, 3], [2, 4, 5], [2, 4, 7]]
flatterend = []

for row in matrix:
    for num in row:
        flatterend.append(num)

flatterend = [num for row in matrix for num in row]

print("comprehension ", flatterend)
