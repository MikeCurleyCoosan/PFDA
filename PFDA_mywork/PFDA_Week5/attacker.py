class Attacker:

#This class will be used to create an attacker object. The attacker object will be used in the game of Risk to attack a defender object
#The attacker object will have the following attributes:
#1. The number of attacking armies
#3. The number of attacking dice
#The attacker object will have the following methods:
#1. A method to roll the dice
#2. A method to calculate the number of armies lost by the attacker
#3. A method to determine the winner of the battle
#4. A method to determine the number of armies remaining for the attacker

#Author: Michael Curley
#Date: 24/10/2024
   

    def __init__(self, attacking_armies, attacking_dice):
        self.attacking_armies = attacking_armies
        self.attacking_dice = attacking_dice

    def roll_dice(self):
        import random
        import numpy as np
        attacking_dice_rolls = []
        defending_dice_rolls = []
        for i in range(self.attacking_dice):
            attacking_dice_rolls.append(random.randint(1, 6))
        attacking_dice_rolls.sort(reverse=True)
        attacking_dice_rolls = np.array(attacking_dice_rolls)
        return attacking_dice_rolls 
    
    def calculate_attacker_armies_lost(self, attacking_dice_rolls, defending_dice_rolls):
        armies_lost = 0
        for i in range(min(len(attacking_dice_rolls), len(defending_dice_rolls))):
            if attacking_dice_rolls[i] > defending_dice_rolls[i]:
                armies_lost += 0
            elif attacking_dice_rolls[i] == defending_dice_rolls[i]:
                armies_lost += 1
            else:
                armies_lost += 1
        return armies_lost
    
    def determine_winner(self, attacking_armies, defending_armies):
        if attacking_armies == 0:
            return "Defender"
        elif defending_armies == 0:
            return "Attacker"
        else:
            return "Draw"
        
    def armies_remaining_attacker(self, attacking_armies, attacking_armies_lost):
        return attacking_armies - attacking_armies_lost

    
    def __str__(self):
        return f"Attacker: {self.attacking_armies} armies, {self.attacking_dice} dice\nDefender: {self.defending_armies} armies, {self.defending_dice} dice"


