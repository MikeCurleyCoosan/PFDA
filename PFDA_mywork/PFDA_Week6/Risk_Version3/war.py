class War:

#This class will be used to simulate a game of Risk until one of the players has no armies left.
#The class will have the following attributes:
#attack_army - the number of armies the attacker has
#defence_army - the number of armies the defender has
#result - a numpy array that will store the results of each round of the game
#The class will have the following methods:
#play_until_winner - this method will simulate a game of Risk until one of the players has no armies left
#play_round - this method will simulate a round of Risk
#The play_round method will have the following steps:
#Generate the attack throws
#Sort the attack throws in descending order
#Take the two highest attack throws
#Generate the defence throws
#Sort the defence throws in descending order
#Take the highest defence throw
#Calculate the number of armies lost by the attacker and the defender
#Update the number of armies the attacker and defender have
#Update the result array
#The play_until_winner method will have the following steps:
#While both the attacker and defender have armies left
#Play a round of Risk
#Return the result array
#The play_until_winner method will also have the following attributes:
#attack_army - the number of armies the attacker has
#defence_army - the number of armies the defender has
#result - a numpy array that will store the results of each round of the game
#The play_round method will have the following steps:
#Generate the attack throws
#Sort the attack throws in descending order
#Take the two highest attack throws
#Generate the defence throws
#Sort the defence throws in descending order
#Take the highest defence throw
#Calculate the number of armies lost by the attacker and the defender
#Update the number of armies the attacker and defender have
#Update the result array
#The play_until_winner method will have the following steps:
#While both the attacker and defender have armies left
#Play a round of Risk
#Return the result array
#The play_until_winner method will also have the following attributes:
#attack_army - the number of armies the attacker has
#defence_army - the number of armies the defender has
#result - a numpy array that will store the results of each round of the game
#The play_round method will have the following steps:
#Generate the attack throws
#Sort the attack throws in descending order
#Take the two highest attack throws
#Generate the defence throws
#Sort the defence throws in descending order
#Take the highest defence throw
#Calculate the number of armies lost by the attacker and the defender
#Update the number of armies the attacker and defender have
#Update the result array

    def __init__(self, attack_army, defence_army):
        import numpy as np
        self.attack_army = attack_army
        self.defence_army = defence_army
        self.result = np.array([0, attack_army, defence_army, 0, 0])

    def play_round(self):
        import numpy as np
        from attacker import Attacker as attack
        from defender import Defender as defend

        attacker = attack()
        defender = defend()
