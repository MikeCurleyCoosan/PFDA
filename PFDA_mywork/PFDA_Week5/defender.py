class Defender:

#This class will be used to create a defender object. The defender object will be used in the game of Risk to defend against an attacker object
#The defender object will have the following attributes:
#1. The number of defending armies
#3. The number of defending dice
#The defender object will have the following methods:
#1. A method to roll the dice
#2. A method to calculate the number of armies lost by the defender
#3. A method to determine the winner of the battle
#4. A method to determine the number of armies remaining for the defender


#Author: Michael Curley
#Date: 24/10/2024

    def __init__(self, defending_armies, defending_dice):
        self.defending_armies = defending_armies
        self.defending_dice = defending_dice

    def roll_dice(self):
        import random
        import numpy as np
        defending_dice_rolls = []
        for i in range(self.defending_dice):
            defending_dice_rolls.append(random.randint(1, 6))
            defending_dice_rolls.sort(reverse=True)
            defending_dice_rolls = np.array(defending_dice_rolls)
        return defending_dice_rolls
    
    
    def calculate_defender_armies_lost(self, attacking_dice_rolls, defending_dice_rolls):
        armies_lost = 0
        for i in range(min(len(attacking_dice_rolls), len(defending_dice_rolls))):
            if attacking_dice_rolls[i] > defending_dice_rolls[i]:
                armies_lost += 1
            elif attacking_dice_rolls[i] == defending_dice_rolls[i]:
                armies_lost += 0
            else:
                armies_lost += 0
        return armies_lost
    
    def determine_winner(self, attacking_armies, defending_armies):
        if attacking_armies == 0:
            return "Defender"
        elif defending_armies == 0:
            return "Attacker"
        else:
            return "Draw"
        
    def armies_remaining_defender(self, defending_armies, defending_armies_lost):
        return defending_armies - defending_armies_lost
    
    def __str__(self):
        return f"Attacker: {self.attacking_armies} armies, {self.attacking_dice} dice\nDefender: {self.defending_armies} armies, {self.defending_dice} dice"