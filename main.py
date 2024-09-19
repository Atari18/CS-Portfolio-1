from random import randint
from time import sleep
from PIL import Image

ANIMAL_SOUNDS = {"Dog": "Woof!", "Cat": "Meow!", "Snake": "HISS!"}
PET_LIST = ["Dog", "Cat", "Snake"]
LIST_OF_PETS = ["Dog 🐶", "Cat 🐱", "Snake 🐍"]
PET_EMOJIS = {"Dog": "🐶", "Cat": "🐱", "Snake": "🐍"}
LIST_OF_GENDERS = ["Male", "Female"]
care_list = ["Pet"]
unlock_counter = 0


def guess_the_number(player_instance):
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
    for letter in input_string:
        print(letter, end="")
        sleep(0.01)
    if not no_new_line:
        print("\n")
    return ""


class Player:

    def __init__(self, name, pet, pet_name, pet_gender):
        self.name = name
        self.pet = pet
        self.pet_name = pet_name
        self.pet_gender = pet_gender
        self.money = 0

    def __repr__(self):
        return (f"Name: {self.name}, Money: {self.money}, "
                f"Pet: {self.pet}, Pet Name: {self.pet_name}, Pet Gender: {self.pet_gender}")

    def introduce(self):
        print_letter_by_letter(
            f"👋 Hi, my name is {self.name}! I have a {self.pet_gender} {self.pet} named {self.pet_name}!")

    def update_money(self, amount):
        self.money += amount


class Pet:

    def __init__(self, pet_type, gender, name, owner):
        self.pet_type = pet_type
        self.gender = gender
        self.name = name
        self.owner = owner
        self.bond = 0
        self.wardrobe = ""

    def __repr__(self):
        return (f"Pet Type: {self.pet_type}, Pet Gender: {self.gender}, Pet Name: {self.name}, "
                f"Bond: {self.bond}, Wardrobe: {self.wardrobe}")

    def introduce(self):
        pet_sound = ANIMAL_SOUNDS[self.pet_type] + " " + ANIMAL_SOUNDS[self.pet_type]
        print(PET_EMOJIS[self.pet_type], end="")
        print_letter_by_letter(f"{pet_sound} I'm {self.name}! My owner is {self.owner}!")

    def update_wardrobe(self, item):
        self.wardrobe = item


class Shop:

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

    return Pet(pet_type, gender, name, owner)


def make_player(name, pet, pet_name, gender):

    return Player(name, pet, pet_name, gender)


def pet_selection(pet_list):

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

    gender = input(print_letter_by_letter("\nPlease select a gender: ", True)).capitalize()
    while gender not in gender_list:
        print(print_letter_by_letter("\nInvalid gender, please try again."))
        gender = input(print_letter_by_letter("\nPlease select a gender: ", True)).capitalize()
    return gender


def display_image(pet_instance, extra=""):

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


if __name__ == '__main__':
    main()
