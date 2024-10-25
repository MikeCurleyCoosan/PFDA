class Risk:

#This class will be used to create a Risk object. The Risk object will be used to simulate a game of Risk
#The Risk object will have the following attributes:
#1. The number of attacking armies
#2. The number of defending armies
#3. The number of attacking dice
#4. The number of defending dice
#The Risk object will have the following methods:
#1. A method to simulate a battle
#2. A method to simulate a war
#3. A method to determine the winner of the battle
#4. A method to determine the winner of the war
#5. A method to determine the number of armies remaining for the attacker
#6. A method to determine the number of armies remaining for the defender

    import random as random
    import numpy as np

    try:
        from PFDA_Week5.menu import Menu as m
        import pandas as pd
        import random as random
        import numpy as np
    except ImportError as e:
        print("The following import error occurred: ", e)
        exit()


    choice = m.display_menu()

    while choice != 0:

        if choice in m.choice_map
            m.choice_map[choice]()
        else:
            print("Invalid choice. Please try again.")
        choice = m.display_menu()



    def __init__(self, attacking_armies, defending_armies, attacking_dice, defending_dice):
        self.attacking_armies = attacking_armies
        self.defending_armies = defending_armies
        self.attacking_dice = attacking_dice
        self.defending_dice = defending_dice

    def simulate_battle(self):
        import attacker as attacker
        import defender as defender
        attacking = attacker.Attacker(self.attacking_armies, self.attacking_dice)
        defending = defender.Defender(self.defending_armies, self.defending_dice)
        attacking_dice_rolls = attacking.roll_dice()
        defending_dice_rolls = defending.roll_dice()
        attacking_armies_lost = attacking.calculate_attacker_armies_lost(attacking_dice_rolls, defending_dice_rolls)
        defending_armies_lost = defending.calculate_defender_armies_lost(attacking_dice_rolls, defending_dice_rolls)
        winner = defending.determine_winner(self.attacking_armies, self.defending_armies)
        attacking_armies_remaining = attacking.armies_remaining_attacker(self.attacking_armies, attacking_armies_lost)
        defending_armies_remaining = defending.armies_remaining_defender(self.defending_armies, defending_armies_lost)
        return winner, attacking_armies_remaining, defending_armies_remaining
    
    def simulate_war(self):
        import attacker as attacker
        import defender as defender
        attacking = attacker.Attacker(self.attacking_armies, self.attacking_dice)
        defending = defender.Defender(self.defending_armies, self.defending_dice)
        attacking_dice_rolls = attacking.roll_dice()
        defending_dice_rolls = defending.roll_dice()
        attacking_armies_lost = attacking.calculate_attacker_armies_lost(attacking_dice_rolls, defending_dice_rolls)
        defending_armies_lost = defending.calculate_defender_armies_lost(attacking_dice_rolls, defending_dice_rolls)
        winner = defending.determine_winner(self.attacking_armies, self.defending_armies)
        attacking_armies_remaining = attacking.armies_remaining_attacker(self.attacking_armies, attacking_armies_lost)
        defending_armies_remaining = defending.armies_remaining_defender(self.defending_armies, defending_armies_lost)
        return winner, attacking_armies_remaining, defending_armies_remaining
    
    def determine_winner_battle(self):
        winner, attacking_armies_remaining, defending_armies_remaining = self.simulate_battle()
        if winner == "Attacker":
            return "Attacker"
        else:
            return "Defender"
        
    def determine_winner_war(self):
        winner, attacking_armies_remaining, defending_armies_remaining = self.simulate_war()
        if winner == "Attacker":
            return "Attacker"
        else:
            return "Defender"
        
    def armies_remaining_attacker(self):
        winner, attacking_armies_remaining, defending_armies_remaining = self.simulate_battle()
        return attacking_armies_remaining
    
    def armies_remaining_defender(self):
        winner, attacking_armies_remaining, defending_armies_remaining = self.simulate_battle()
        return defending_armies_remaining
    
