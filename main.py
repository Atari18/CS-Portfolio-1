# Importing modules
from random import randint
from time import sleep
from PIL import Image

# Constants
ANIMAL_SOUNDS = {"Dog": "Woof!", "Cat": "Meow!", "Snake": "HISS!"}
PET_LIST = ["Dog", "Cat", "Snake"]
LIST_OF_PETS = ["Dog 🐶", "Cat 🐱", "Snake 🐍"]
PET_EMOJIS = {"Dog": "🐶", "Cat": "🐱", "Snake": "🐍"}
LIST_OF_GENDERS = ["Male", "Female"]
# List
care_list = ["Pet"]
# Variable
unlock_counter = 0


def guess_the_number(player_instance):
    """
    Plays the "Guess the Number" minigame with the player.

    The game generates a random number between 1 and 20 (inclusive) using randint. The player must guess the number.
    Feedback is provided if the guess is too high or too low. The game continues until the correct guess is made.

    Once the player guesses correctly, they receive £20 minus the number of attempts made. If the player enters a
    non-numeric guess, an error message is displayed.

    Args:
        player_instance (Player): An instance of the Player class representing the player.

    Returns:
        None
    """
    number_to_guess = randint(1, 20)
    number_of_attempts = 0

    print_letter_by_letter("\n\nWelcome to the 'Guess the Number' game!")
    print_letter_by_letter("I have selected a number between 1 and 20. Can you guess it?")

    while True:
        try:
            user_guess = int(input(print_letter_by_letter("Enter your guess: ", True)))
            number_of_attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                prize = max(0, 20 - number_of_attempts)
                print_letter_by_letter(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
                print_letter_by_letter(f"You earned £20 - £{number_of_attempts} for your attempts!")
                player_instance.update_money(prize)
                break
        except ValueError:
            print("Please enter a valid number.")


def print_letter_by_letter(input_string, no_new_line=False):
    """
    Prints a string letter by letter with a short delay.

    This function prints each character of the provided string with a delay of 0.04 seconds
    between characters. It mimics the effect of old terminal outputs. By default, it adds a
    newline character at the end unless specified otherwise by the `no_new_line` parameter.

    Args:
        input_string (str): The string to be printed character by character.
        no_new_line (bool, optional): If True, the function will not print a newline character at the end.
                                      If False, a newline character will be printed. Default is False.

    Returns:
        str: An empty string.
    """
    for letter in input_string:
        print(letter, end="")
        sleep(0.01)
    if not no_new_line:
        print("\n")
    return ""


class Player:
    """
    Represents a player in the game, including their name, pet details, and amount of money.

    Attributes:
        name (str): The name of the player.
        pet (str): The type of the player's pet.
        pet_name (str): The name of the player's pet.
        pet_gender (str): The gender of the player's pet.
        money (int): The amount of money the player has, default is 0.

    Methods:
        __init__(name, pet, pet_name, pet_gender):
            Initializes the Player object.

        __repr__():
            Returns a string representation of the Player object.

        introduce():
            Prints an introduction of the player.

        update_money(amount):
            Adds a specified amount to the player's money.
    """

    def __init__(self, name, pet, pet_name, pet_gender):
        """Initializes the Player object."""
        self.name = name
        self.pet = pet
        self.pet_name = pet_name
        self.pet_gender = pet_gender
        self.money = 0

    def __repr__(self):
        """Returns a string representation of the Player object."""
        return (f"Name: {self.name}, Money: {self.money}, "
                f"Pet: {self.pet}, Pet Name: {self.pet_name}, Pet Gender: {self.pet_gender}")

    def introduce(self):
        print_letter_by_letter(
            f"👋 Hi, my name is {self.name}! I have a {self.pet_gender} {self.pet} named {self.pet_name}!")

    def update_money(self, amount):
        self.money += amount


class Pet:
    """
    Represents a pet in the game.

    Each pet has a type, gender, name, owner, bond level, and wardrobe. Pets can introduce themselves and
    update their wardrobe.

    Attributes:
        pet_type (str): The type of the pet (e.g., dog, cat).
        gender (str): The gender of the pet (e.g., male, female).
        name (str): The name of the pet.
        owner (str): The name of the pet's owner.
        bond (int): The bond level of the pet with its owner.
        wardrobe (str): The wardrobe item of the pet.

    Methods:
        __init__(pet_type, gender, name, owner):
            Initializes the Pet object.

        __repr__():
            Returns a string representation of the Pet object.

        introduce():
            Prints an introduction from the pet.

        update_wardrobe(item):
            Updates the wardrobe item of the pet.
    """

    def __init__(self, pet_type, gender, name, owner):
        """Initializes the Pet object."""
        self.pet_type = pet_type
        self.gender = gender
        self.name = name
        self.owner = owner
        self.bond = 0
        self.wardrobe = ""

    def __repr__(self):
        """Returns a string representation of the Pet object."""
        return (f"Pet Type: {self.pet_type}, Pet Gender: {self.gender}, Pet Name: {self.name}, "
                f"Bond: {self.bond}, Wardrobe: {self.wardrobe}")

    def introduce(self):
        pet_sound = ANIMAL_SOUNDS[self.pet_type] + " " + ANIMAL_SOUNDS[self.pet_type]
        print(PET_EMOJIS[self.pet_type], end="")
        print_letter_by_letter(f"{pet_sound} I'm {self.name}! My owner is {self.owner}!")

    def update_wardrobe(self, item):
        self.wardrobe = item


class Shop:
    """
    Represents a shop in the game.

    Attributes:
        inventory (dict): The shop's inventory.
        locked_inventory (dict): The shop's locked inventory.
        name (str): The name of the shop.

    Methods:
        __init__(inventory, locked_inventory, name):
            Initializes the Shop object.

        __repr__():
            Returns a string representation of the shop object.

        introduce():
            Prints an introduction of the shop.

        show_stock():
            Prints the shop's stock.

        remove_stock(item):
            Removes an item from the shop's inventory or locked inventory.

        unlock_stock(item):
            Moves an item from the shop's locked inventory to the shop's inventory.
    """

    def __init__(self, inventory, locked_inventory, name):
        self.inventory = inventory
        self.locked_inventory = locked_inventory
        self.name = name

    def __repr__(self):
        return f"Inventory: {self.inventory}, Locked inventory: {self.locked_inventory}, Name: {self.name}"

    def introduce(self):
        print_letter_by_letter(f"\nWelcome to {self.name}!")

    def show_stock(self):
        print_letter_by_letter("This shop sells: ")
        for item, price in self.inventory.items():
            print_letter_by_letter(f"🔓{item}: £{price}")
        for item, price in self.locked_inventory.items():
            print_letter_by_letter(f"🔒{item}: £{price} (Locked)")

    def remove_stock(self, item):
        if item in self.inventory:
            self.inventory.pop(item)
        elif item in self.locked_inventory:
            self.locked_inventory.pop(item)

    def unlock_stock(self, item):
        if item in self.locked_inventory:
            self.inventory[item] = self.locked_inventory.pop(item)


def make_pet(pet_type, gender, name, owner):
    """
    Creates an instance of the Pet class.

    Args:
        pet_type (str): The type of the pet.
        gender (str): The gender of the pet.
        name (str): The name of the pet.
        owner (str): The name of the pet's owner.

    Returns:
        Pet: An instance of the Pet class.
    """
    return Pet(pet_type, gender, name, owner)


def make_player(name, pet, pet_name, gender):
    """
    Creates an instance of the Player class.

    Args:
        name (str): The name of the player.
        pet (str): The type of the player's pet.
        pet_name (str): The name of the player's pet.
        gender (str): The gender of the player's pet.

    Returns:
        Player: An instance of the Player class.
    """
    return Player(name, pet, pet_name, gender)


def pet_selection(pet_list):
    """
    Allows the player to select a pet from a list of available pets.

    This function displays the list of available pets to the player, pausing for 0.01 seconds
    between each pet printed. The player can then choose a pet. If the player inputs a pet
    not included in the provided list, the function will print an error message and prompt
    again until a valid pet is selected.

    Args:
        pet_list (list): A list of available pets.

    Returns:
        str: The selected pet.
    """
    print_letter_by_letter("\nThe list of available pets are:")
    for pet in pet_list:
        sleep(0.01)
        print_letter_by_letter(pet)
    pet = input(print_letter_by_letter("\nPlease select a pet: ", True)).capitalize()
    while pet not in ["Dog", "Cat", "Snake"]:
        print_letter_by_letter("\nInvalid pet, please try again.")
        pet = input(print_letter_by_letter("\nPlease select a pet: ", True)).capitalize()
    return pet


def gender_selection(gender_list):
    """
    Asks the user to select a gender from a list of available genders.

    This function prompts the user to input a gender. If the user inputs a gender
    that is not in the provided gender_list, the function will display an error message
    and ask again until a valid gender is provided.

    Args:
        gender_list (list): A list of available genders.

    Returns:
        str: The selected gender.
    """
    gender = input(print_letter_by_letter("\nPlease select a gender: ", True)).capitalize()
    while gender not in gender_list:
        print(print_letter_by_letter("\nInvalid gender, please try again."))
        gender = input(print_letter_by_letter("\nPlease select a gender: ", True)).capitalize()
    return gender


def display_image(pet_instance, extra=""):
    """
    Displays an image of the pet based on the provided path.

    This function prompts the user to decide if they would like to see an image of their pet. If the user inputs
    anything other than 'Y' or 'N', the function will display an error message and continue to prompt until
    a valid input is received. If the user agrees (inputs 'Y'), the function attempts to display an image using a
    path generated from the given arguments. If the path is not valid or an error occurs while opening the image,
    the error is handled and a message is displayed. The function then pauses for 5 seconds to allow the user to
    view and close the image before the game continues.

    Args:
        pet_instance (instance): An instance of the Pet class containing details required to form the image path.
        extra (str, optional): An additional string to be added to the image path. Defaults to "".

    Returns:
        None
    """
    answer = input(
        print_letter_by_letter(f"Would you like to see an image of {pet_instance.name}? [Y/N] ", True)).upper()
    while answer not in ["Y", "N"]:
        print_letter_by_letter("Invalid option, please try again.")
        answer = input(
            print_letter_by_letter(f"Would you like to see an image of {pet_instance.name}? [Y/N] ", True)).upper()

    image_path = f"pet_images/{pet_instance.pet_type}{extra}.png"

    if answer == "Y":
        try:
            img = Image.open(image_path)
            img.show()
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        sleep(5)


def care(player_instance, pet_instance, shop_instance):
    """
    Performs a caring action towards the pet, affecting the bond level and potentially unlocking rewards.

    This function allows the user to select a caring action for their pet from a predefined list.
    It visually represents the action, waits for it to complete, and then increases the pet's bond level
    based on the selected action. The global variable `unlock_counter` is incremented by 1 after each action.
    Depending on the bond level and `unlock_counter`, the function may print unlock messages for new items
    available in the store. After performing the action, the function calls `game_menu()`.

    Args:
        player_instance (Player): An instance of the Player class.
        pet_instance (Pet): An instance of the Pet class.
        shop_instance (Shop): An instance of the Shop class.

    Returns:
        None
    """
    global unlock_counter
    print_letter_by_letter("\nCare actions:")
    for care_a in care_list:
        print_letter_by_letter(care_a)
    care_type = input(print_letter_by_letter("\nWhich action would you like to do? ", True)).capitalize()
    while care_type not in care_list:
        print_letter_by_letter("\nInvalid care action, please try again.")
        care_type = input(print_letter_by_letter("\nWhich action would you like to do? ", True)).capitalize()

    if care_type == "Walk":
        pet_instance.bond += 80
        print_letter_by_letter("🚶 Walking...")
        sleep(6)
        print_letter_by_letter(f"You walked with {pet_instance.name}!\nGained 80 bond points!")
    elif care_type == "Pet":
        pet_instance.bond += 20
        print_letter_by_letter("❤ Petting...")
        sleep(3)
        print_letter_by_letter(f"You petted {pet_instance.name}!\nGained 20 bond points!")  # Fixed bond points value
    elif care_type == "Feed":
        pet_instance.bond += 100
        print_letter_by_letter("🥫 Feeding...")
        sleep(8)
        print_letter_by_letter(f"You fed {pet_instance.name}!\nGained 100 bond points!")
    else:
        pet_instance.bond += 60
        print_letter_by_letter("🪥 Brushing...")
        sleep(2)
        print_letter_by_letter(f"You brushed {pet_instance.name}!\nGained 60 bond points!")

    if pet_instance.bond >= 100 and unlock_counter == 0:
        print_letter_by_letter("🔓You unlocked Glasses in the store!!!🔓")
        unlock_counter += 1
    if pet_instance.bond >= 200 and unlock_counter < 2:
        print_letter_by_letter("🔓You unlocked Beanie in the store!!!🔓")
        unlock_counter += 1
    if pet_instance.bond >= 400 and unlock_counter < 3:
        print_letter_by_letter("🔓You unlocked Sweater in the store!!!🔓")
        unlock_counter += 1

    game_menu(player_instance, pet_instance, shop_instance)


def buy_from_shop(player_instance, shop_instance, pet_instance):
    """
    Allows the user to purchase items from the shop.

    This function first displays the player's balance. It then checks if the player can afford any items in
    the shop. If the player cannot afford any items, the function exits. If the player can afford items,
    they are prompted to select an item to buy. The function continues to prompt until a valid item is entered.
    Depending on the purchased item, various actions are performed:
    - For "Brush", "Tin Food", or "Lead", a custom message is printed, the item is removed from the shop's inventory,
      and the item-specific care action will be added to `care_list`.
    - For "Sweater", "Glasses", or "Beanie", a custom message will be printed, the item is removed from the shop's inventory,
      the item is added to the pet's wardrobe using `update_wardrobe()`, and the user is given an option to view an image
      of their pet with the new item via `display_image()`.

    The `game_menu()` function is called at the end.

    Args:
        player_instance (Player): An instance of the Player class.
        shop_instance (Shop): An instance of the Shop class.
        pet_instance (Pet): An instance of the Pet class.

    Returns:
        None
    """
    print_letter_by_letter(f"\nYou have £{player_instance.money}")
    counter = 0
    for x in shop_instance.inventory:
        counter += 1
    for item, price in shop_instance.inventory.items():
        if player_instance.money < price:
            counter -= 1
    if counter == 0:
        print_letter_by_letter("You don't have enough money!")
        return
    else:
        pass

    item_to_buy = input(print_letter_by_letter("Which item would you like to buy?", True)).title()
    while item_to_buy not in shop_instance.inventory or player_instance.money < shop_instance.inventory[item_to_buy]:
        print_letter_by_letter("\nInvalid item or insufficient balance, please try again.")
        item_to_buy = input(print_letter_by_letter("Which item would you like to buy? ", True)).title()

    player_instance.money -= shop_instance.inventory[item_to_buy]

    if item_to_buy == "Brush":
        care_list.append("Clean")
        print_letter_by_letter(f"You can now clean {pet_instance.name}!")
        shop_instance.remove_stock("Brush")
    elif item_to_buy == "Tin Food":
        care_list.append("Feed")
        print_letter_by_letter(f"You can now feed {pet_instance.name}!")
        shop_instance.remove_stock("Tin Food")
    elif item_to_buy == "Lead":
        care_list.append("Walk")
        print_letter_by_letter(f"You can now walk with {pet_instance.name}!")
        shop_instance.remove_stock("Lead")
    elif item_to_buy == "Sweater":
        print_letter_by_letter(f"Yay! {pet_instance.name} now has a sweater!")
        shop_instance.remove_stock("Sweater")
        display_image(pet_instance, "sweater")
        pet_instance.update_wardrobe("sweater")
    elif item_to_buy == "Glasses":
        print_letter_by_letter(f"Yay! {pet_instance.name} now has glasses!")
        shop_instance.remove_stock("Glasses")
        display_image(pet_instance, "glasses")
        pet_instance.update_wardrobe("glasses")
    elif item_to_buy == "Beanie":
        print_letter_by_letter(f"Yay! {pet_instance.name} now has a beanie!")
        shop_instance.remove_stock("Beanie")
        display_image(pet_instance, "beanie")
        pet_instance.update_wardrobe("beanie")


def game_menu(player_instance, pet_instance, shop_instance):
    """
    Displays the main menu of the game and handles user input for various actions.

    This function shows the player's balance and the pet's bond level. It then presents four options for the user to
    choose from. The user must type a valid option from the presented list. If the user types an invalid option, an
    error message is shown and the user is prompted again until a valid input is received.

    Depending on the user's choice:
    - If the user selects "Care for pet", the `care()` function is called.
    - If the user selects "Play minigame", the `guess_the_number()` function will be called.
    - If the user selects "Enter shop", bond levels are checked to unlock items in the shop, the `introduce()` and
      `show_stock()` functions are called, followed by the `buy_from_shop()` function.
    - If the user selects "Take picture of pet", the `display_image()` function is called.

    Args:
        player_instance (Player): An instance of the Player class.
        pet_instance (Pet): An instance of the Pet class.
        shop_instance (Shop): An instance of the Shop class.

    Returns:
        None
    """
    print_letter_by_letter(f"\nBalance: £{player_instance.money}  ||  Bond: {pet_instance.bond}")
    option_input = ""
    while option_input not in ["Care for pet", "Play minigame", "Enter shop", "Customise pet"]:
        print_letter_by_letter("\nSelect an option:")
        for option in ["❤ Care for pet ❤", "🎲 Play minigame 🎲", "🏷️ Enter shop 🏷️", "📷 Take picture of pet 📷"]:
            print_letter_by_letter(option)
        option_input = input(print_letter_by_letter("\nOption: ", True)).capitalize()
        if option_input == "Care for pet":
            care(player_instance, pet_instance, shop_instance)
        elif option_input == "Play minigame":
            guess_the_number(player_instance)
        elif option_input == "Enter shop":
            if pet_instance.bond >= 100:
                shop_instance.unlock_stock("Glasses")
            if pet_instance.bond >= 200:
                shop_instance.unlock_stock("Beanie")
            if pet_instance.bond >= 400:
                shop_instance.unlock_stock("Sweater")
            shop_instance.introduce()
            shop_instance.show_stock()
            buy_from_shop(player_instance, shop_instance, pet_instance)
        elif option_input == "Take picture of pet":
            display_image(pet_instance, pet_instance.wardrobe)
        else:
            print_letter_by_letter("Invalid option, please try again.")


def main():
    """
    The main function of the game.

    This function initiates the game by performing the following steps:
    1. Prints a welcome message and the objective of the game.
    2. Prompts the user to enter their name, select a pet, choose the gender of the pet, and provide the pet's name.
    3. Creates `Player` and `Pet` instances by calling `make_player()` and `make_pet()`, respectively.
    4. Creates a `Shop` instance with predefined inventory items.
    5. Introduces the player and pet using their respective `introduce()` methods.
    6. Displays an image of the pet.
    7. Enters an infinite loop calling `game_menu()` to handle game actions.

    Returns:
        None
    """
    print_letter_by_letter("Welcome to my pet game! I hope you enjoy it!")
    print_letter_by_letter(
        "The aim of the game is to earn money and bond with your pet! When you have enough money and bond, "
        "you can buy items from the shop to customize your pet!\n100 Bond unlocks Glasses in the store!\n200 Bond "
        "unlocks Beanie in the store!\n400 Bond unlocks Sweater in the store!"
    )
    name_input = input(print_letter_by_letter("Please enter your name: ", True)).capitalize()
    selected_pet = pet_selection(LIST_OF_PETS)
    selected_gender = gender_selection(LIST_OF_GENDERS)
    pet_name_selection = input(print_letter_by_letter("\nPlease enter the name of your pet: ", True)).capitalize()

    player = make_player(name_input, selected_pet, pet_name_selection, selected_gender)
    pet = make_pet(selected_pet, selected_gender, pet_name_selection, name_input)
    shop = Shop(
        {"Brush": 20, "Tin Food": 100, "Lead": 50},
        {"Glasses": 100, "Beanie": 200, "Sweater": 300},
        "Gregory's Pet Shop"
    )
    print("\n")
    player.introduce()
    pet.introduce()
    display_image(pet)
    while True:
        game_menu(player, pet, shop)


# Calling the main function
if __name__ == '__main__':
    main()

