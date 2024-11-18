class Menu:
#Author: Michael Curley
#Date: 24/10/2024
#This class will be used to display a menu to the user, and will run the appropriate code based on the user's choice
    
    #Method to display the menu to the user
    def display_menu():
        print("\t Risk Game Menu")
        print("\t(a). Simulate a battle")
        print("\t(b). Simulate a war")
        print("\t(Q). Exit")

        choice = input("Type one letter (a,b or q):").strip().lower()
        return choice
    
    #Method to simulate a battle
    def simulate_battle():
       print("\t Create a battle simulation")
       from battle import Battle as battle
       battle()
       print("\t Battle simulation complete")
       
       

    #Method to simulate a war
    def simulate_war():
        print("\t Create a war simulation")
        from war import War as war
        war()

    #Dummy method to exit the program nicely
    def do_nothing():
        pass

    #Dictionary to map the user's choice to the appropriate method
    choice_map = {
        "a": simulate_battle,
        "b": simulate_war,
        "q": do_nothing
    }

    