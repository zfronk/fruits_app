import os


class FruitCollector:
    # Global instance
    def __init__(self):
        self.fruits = []

    # Main menu
    def display_menu(self):
        print()
        print("Welcome to the Fruit Collector!")
        print()
        print("Main Menu")
        print("---------")
        print("1. Add a fruit.")
        print("2. Display all fruits.")
        print("3. Exit.")

    # Choose option
    def choose_option(self):
        while True:
            try:
                print()
                option = int(input("Choose an option from the main menu: "))
                
                # Null check
                if not option:
                    print()
                    print("Option cannot be empty!")
                    continue
                
                # Invalid option
                elif option < 1 or option > 3:
                    print()
                    print("Invalid option! Choose a valid option.")
                    continue

                # Return option
                else:
                    return option
            
            # Invalid input     
            except ValueError:
                print()
                print("Invalid input! Please enter a number.")

    # Add fruit
    def add_fruit(self):
        try:
            print()
            added_fruit = input("Enter fruit to be added: ")

            if not added_fruit:
                print()
                print("Fruit cannot be empty!")
                return
            else:
                new_fruit = {
                    "fruit":added_fruit
                }

                file_name = "fruits.txt"

                if os.path.exists(file_name):
                    with open(file_name, "a") as file:
                        print(added_fruit, file=file)
                
                else:
                    with open(file_name, "w") as file:
                        print(added_fruit, file=file)

                self.fruits.append(new_fruit)

                print()
                print("Fruit added successfully!")

        except ValueError:
            print("Invalid input!")

    # Show fruits
    def show_fruits(self):
        
        try:
            print()
            print("Fruits")
            print("------")
        
            for index, fruit in enumerate(self.fruits, start=1):
                print(f"{index}. {fruit['fruit']}")


        except ValueError:
            print("Error occurred displaying fruits!")


    # Run application
    def run(self):
        self.display_menu()

        while True:
            try:
                choice = self.choose_option()
                if choice == 1:
                    self.add_fruit()

                elif  choice == 2:
                    self.show_fruits()
                
                elif choice == 3:
                    break

            except ValueError:
                print("Error occured! Running application.")


if __name__ == "__main__":
    app = FruitCollector()
    app.run()

    


                

