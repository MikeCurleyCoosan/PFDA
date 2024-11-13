class Menu:

    def print_menu():
        print("Risk Game Menu:")
        print("1. Run a battle between two armies of size 1000")
        print("2. Run a battle between armies of arbitrary size")
        print("3. Exit")

  
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("You are running a balle between two armies of size 1000")
            from battle1000 import Battle1000 as battle
            battle()
            print("\t Battle simulation complete")
            break
        elif choice == '2':
            print("You are running a battle between armies of arbitrary size")
            from battle import Battle as battle
            battle()
            print("\t Battle simulation complete")
            break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    Menu()
