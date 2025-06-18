print("Hello World")
x = 1
y = 2
Unit_Price = 3

print("Hello World")

course = "Python Programming"
print(len(course))

# For Loop

for number in range(1, 4):
    print("number", number + 1, (number + 1) * ".")

# count even number under 10
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")
