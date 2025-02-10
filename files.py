import os

file_name = "fruits.txt"

# Check directory

if os.path.exists(file_name):
    print()
    print("File exists!")

else:
    print()
    print("Opps file does not exist!")

print()
print("File options")
print("1. Read file")
print("2. Append file")


def read_file():
    with open (file_name, "r") as file:
        content = file.read()

        if content == "":
            print()
            print("No content!")

        else:
            print()
            print("Printing content...")
            print(content)

def append_file():
    with open(file_name, "a") as file:
        fruit_added = input("Enter fruit to add: ")

        print(fruit_added, file=file)

        print("Fruit added successfully!")



while True:
    print()
    option = input("Choose option from file options: ")

    if option == "1":
        read_file()
        continue

    elif option == "2":
        append_file()
        continue


    elif option == "3":
        print("Exiting application...")
        break

    else:
        print("Invalid option! Try again.")
        continue
    



