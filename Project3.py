# Contact management list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for i in range(len(fruits)):
#     fruits[i] = fruits[i].upper()
#     # print(i)
# print(fruits)

# names = []
# ages = []
# emails = []

# for i in range(3):
#     print("Enter contact", i + 1)
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     email = input("Enter your email: ")

#     names.append(name)
#     ages.append(age)
#     emails.append(email)
# print("Name:", names, "Age:", ages, "Email:", emails)

def add_contact():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    contact = {
        "name": name,
        "age": age,
        "email": email
    }
    return contact


people = []

while True:
    command = input("Do you want to add contact? (yes/no): ").lower()
    if command == "yes":
        contact = add_contact()
        people.append(contact)
        print("Contact added successfully!")
    elif command == "no":
        print("No contact added.")
