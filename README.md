# Fruit Collector

The Fruit Collector is a simple command-line application built in Python that allows users to collect and manage a list of fruits. It enables users to add fruits to a collection, view the list of fruits, and save them to a file (`fruits.txt`).

## Features

- **Add a Fruit**: Allows users to add a new fruit to the collection.
- **Display All Fruits**: Displays all the fruits that have been collected.
- **Save Fruits**: The list of fruits is saved to a file (`fruits.txt`) so it persists between runs.
- **Exit Application**: Exit the application.

## Requirements

- Python 3.x

## Installation

1. Ensure you have **Python 3.x** installed on your system. You can download Python from the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Clone or download this repository.

### Clone the Repository

You can clone the project repository using the following command:

```bash
git clone https://github.com/yourusername/FruitCollector.git
```

## How to Run

1. Navigate to the directory containing the project.
2. Open a terminal or command prompt.
3. Run the `fruit_collector.py` script:

   ```bash
   python fruit_collector.py
   ```

This will start the application and show the main menu with available options.

## Usage

Once the application is running, you will be presented with a menu offering the following options:

1. **Add a fruit**: Allows you to add a new fruit to the collection.
2. **Display all fruits**: View all fruits that have been added to the collection.
3. **Exit application**: Exit the application.

### Example:

**Sample Menu Interaction**

```plaintext
Welcome to the Fruit Collector!

Main Menu
---------
1. Add a fruit.
2. Display all fruits.
3. Exit.

# Choose an option from the main menu: 1

Enter fruit to be added: Apple

Fruit added successfully!

Main Menu
---------
1. Add a fruit.
2. Display all fruits.
3. Exit.

# Choose an option from the main menu: 2

Fruits
------
1. Apple
```

## Code Overview

- **`__init__`**: Initializes the FruitCollector with an empty list of fruits.
- **`display_menu()`**: Displays the main menu with options for the user to choose from.
- **`choose_option()`**: Prompts the user to choose an option from the menu and ensures valid input.
- **`add_fruit()`**: Allows the user to add a fruit to the collection and saves it to a file (`fruits.txt`).
- **`show_fruits()`**: Displays all fruits currently in the collection.
- **`run()`**: The main loop of the application, which calls the other methods based on the user’s menu choice.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This README explains how to set up and use your **FruitCollector** app. Let me know if you'd like to add or modify anything!
