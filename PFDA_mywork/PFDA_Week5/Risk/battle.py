class Battle:
    #This class will simulate a battle between two armies. The battle will be between an attacker and a defender
    #The battle will have the following attributes:
    #1. The number of attacking armies
    #2. The number of attacking dice (max 3)
    #3. The number of defending armies
    #4. The number of defending dice (max 2)
    #The battle will involve the smallest number of armies put forward by either the attacker or defender
    #The battle can be of infinite army size but the number of dice will be limited to 3 for the attacker and 2 for the defender

    #Author: Michael Curley
    #Date: 24/10/2024

    #import required classes
    from attacker import Attacker as attacker
    from defender import Defender as defender
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #Request army and dice information from user
    attack_armies = int(input("\t Please enter the number of attacking armies "))
    attack_dice = int(input("\t Please enter the number of attacking dice "))
    #Check that the number of attacking dice is less than 3
    while attack_dice < 0 or attack_dice > 3:
        print("The number of attacking dice must be between 1 and 3")
        attack_dice = int(input("\t Please enter the number of attacking dice "))
    defence_armies = int(input("\t Please enter the number of defending armies "))
    defending_dice = int(input("\t Please enter the number of defending dice "))
    #Check that the number of defending dice is less than 2
    while defending_dice < 0 or defending_dice > 2:
        print("The number of defending dice must be between 1 and 2")
        defending_dice = int(input("\t Please enter the number of defending dice "))
   
    #Battles will take the least number of armies put forward by either attack or defence
    if attack_armies < defence_armies:
        defence_armies = attack_armies
    else:
        attack_armies = defence_armies

    #Create an instance of an offence
    offence = attacker(attack_armies, attack_dice)
    #Create an instance of an defence
    defence = defender(defence_armies, defending_dice)

    #Roll the dice for the offence. This will create an numpy array to store the dice rolls for the attack
    offence_dice = offence.roll_dice()
    #Roll the dice for the defence. This will create an numpy array to store the dice rolls for the attack
    defence_dice = defence.roll_dice()

    #RESULTS OF THE BATTLE
    print('\n')
    print('************************************************************************************************')
    print('\t\tRESULTS OF THE BATTLE')
    print('************************************************************************************************')
    print('\n')

    #The number of attacking armies put into the battle
    print(f'The number of attacking armies put into the battle was : {attack_armies*attack_dice}')

    #The number of defending armies put into the battle
    print(f'The number of defending armies put into the battle was : {defence_armies*defending_dice}')


    #Calculate the number of armies lost by the attacker
    offence_armies_lost = offence.calculate_attacker_armies_lost(attack_armies, offence_dice, defence_dice)
    print(f'The number of attaking armies lost in this battle was : {offence_armies_lost}')


    #Calculate the number of armies lost by the defender
    defence_armies_lost = defence.calculate_defender_armies_lost(defence_armies, offence_dice, defence_dice)
    print(f'The number of defending armies lost in this battle was : {defence_armies_lost}')

    #Calculate the number of armies remaining for the attacker
    offence_armies_remaining = offence.armies_remaining_attacker(attack_armies, attack_dice, offence_armies_lost)
    print(f'The number of attaking armies remaining in this battle was : {offence_armies_remaining}')

    #Calculate the number of armies remaining for the defender
    defence_armies_remaining = defence.armies_remaining_defender(defence_armies, defending_dice, defence_armies_lost)
    print(f'The number of defending armies remaining in this battle was : {defence_armies_remaining}')

    print('\n')
    print('************************************************************************************************')

    #Testing 
    #print("The attacking army dice rolls are ")
    #print(offence_dice
    #print("The defending army dice rolls are ")
    #print(defence_dice)

    
    # Create a new matrix to store the results of the battles
    results = np.zeros((attack_armies, len(defence_dice[1])))

    # Loop through the dice rolls and compare the results
    for i in range(attack_armies):
       for j in range(len(defence_dice[1])):
            if defence_dice[i, j] == offence_dice[i, j]:
               results[i, 1] += 1
            elif defence_dice[i, j] > offence_dice[i, j]:
                results[i, 1] += 1
            else:
               results[i, 0] += 1

    #Print the results of the battle 
    #print(results)

    #Convert the results from a numpy float array to an integer array

    results = results.astype(int)
    results

    # Create a pandas dataframe to store the results

    df = pd.DataFrame(results, columns=['Attacker Wins', 'Defender Wins'])
    print(df)


    # Percentage of wins for the 
    attacker_percentage = 0
    for i in range (attack_armies):
        if df['Attacker Wins'][i] == 2:
            attacker_percentage += 1/(attack_armies)
    print(attacker_percentage)


    # Percentage of wins for the defender   
    defender_percentage = 0
    for i in range (attack_armies):
        if df['Defender Wins'][i] == 2:
            defender_percentage += 1/(attack_armies)
    print(defender_percentage)

    # Draw percentage
    draw_percentage = 1 - attacker_percentage - defender_percentage
    print(draw_percentage)

    # Double check the percentages
    draw_percentage_check=0
    for i in range (attack_armies):
        if df['Attacker Wins'][i] == 1 and df['Defender Wins'][i] == 1:
            draw_percentage_check += 1/(attack_armies)

    #print(draw_percentage_check)