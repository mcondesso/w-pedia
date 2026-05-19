def show_welcome():

    print("=" * 50)
    print("Welcome".center(50))
    print("To".center(50))
    print("W".center(50))
    print("Pedia".center(50))
    print("=" * 50)

    player_name = input("\nWhat would you like to be adddressed as: ")

    print(f"\nWelcome, {player_name}!")
    print("\nWhere curiosity turns into knowledge,")
    print("time turns into wisdome,")
    print("and lerning becommes an unforgetable adventure.\n")

def show_menu():

    print("\nMain Menu")
    print("1. Start the game")
    print("2. Instructions")
    print("3. Settiongs")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    return choice


def start_game():

    print("\nWhich 'Mode' would you like to play today?\n")


    print("1. Who")
    print("2. What")
    print("3. When")
    print("4. Where")

    mode = input("\nWhich 'Mode' would you like to play today? ")

        print("\nAmazing choice!")
        print("Welcome to WHO mode!")
        print("Here we will dive into the lives of remarkable women and men")
        print("whose names shaped history, science, art, leadership, and discovery.")
        print("Prepare to uncover inspiring stories, legendary achievements,")
        print("and the fascinating journeys behind some of the world's greatest names!")

        print("\nExcellent choice!")
        print("Welcome to WHAT mode!")
        print("Here you will explore incredible objects, inventions, ideas,")
        print("mysteries, and discoveries from around the world.")
        print("Get ready to challenge your curiosity and learn amazing facts")
        print("about things that changed humanity forever!")

    if mode == "1":

    elif mode == "3":

    elif mode == "2":

        print("\nFantastic choice!")
        print("Welcome to WHEN mode!")
        print("Travel through time and uncover the dates behind major events,")
        print("ancient civilizations, groundbreaking discoveries, and epic moments in history.")
        print("Every question is a journey into the timeline of humanity!")

    elif mode == "4":

        print("\nWonderful choice!")
        print("Welcome to WHERE mode!")
        print("Get ready to explore countreis, cities, landmarks, oceans,")
        print("mountains, and hidden places across the globe.")
        print("Adventure, geography, culture, and exploration await you!")

    else:

        print("\nInvalid choice.")
        print("Please select 1, 2, 3, or 4.")


show_welcome()

while True:

    choice = show_menu()

    if choice == "1":
        start_game()

    elif choice == "2":

        print("\nInstructions:")
        print("This manu is under construction.")
        print("Learn while having fun and exploring new ideas!")

    elif choice == "3":

        print("\nSettings menu coming soon!")
        print("Here you will later customize your game experience.")

    elif choice == "4":

        print("\nThank you for playing W-Pedia!")
        print("See you again soon, explorer!\n")
        break

    else:

        print("\nInvalid choice.")
        print("Please enter 1, 2, 3, or 4.")