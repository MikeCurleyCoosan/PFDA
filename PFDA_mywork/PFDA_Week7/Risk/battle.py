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

    def __init__(self):
        pass
  
    #import required classes
    from attacker import Attacker as attacker
    from defender import Defender as defender
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    
    attack_dice = 3
    defending_dice = 2
    attack_armies = int(input("\t Please enter the number of attacking armies "))
    defence_armies = int(input("\t Please enter the number of defending armies "))
    
    #Battles will take the least number of armies put forward by either attack or defence
    if attack_armies < defence_armies:
        defence_armies = attack_armies
    else:
        attack_armies = defence_armies


    attackerLosses = [attack_armies*attack_dice]
    defenderLosses = [defence_armies*defending_dice]
    attacker_remaining = attack_armies*attack_dice
    defender_remaining = defence_armies*defending_dice
    roundNumber = 1


    while attacker_remaining >= 0 and defender_remaining >=0:

        #Create an instance of a n offence
        offence = attacker(attack_armies, attack_dice)
        #Create an instance of an defence
        defence = defender(defence_armies, defending_dice)
        #Roll the dice for the offence. This will create an numpy array to store the dice rolls for the attack
        offence_dice = offence.roll_dice()
        #Roll the dice for the defence. This will create an numpy array to store the dice rolls for the attack
        defence_dice = defence.roll_dice()


        #The number of attacking armies put into the battle
        print(f'\t Round {roundNumber} : The number of attacking soldiers put into the battle was : {attacker_remaining}')
        #The number of defending armies put into the battle
        print(f'\t Round {roundNumber} : The number of defending soldiers put into the battle was : {defender_remaining}')
        battle_loss_attacker = offence.calculate_attacker_armies_lost(attack_armies, offence_dice, defence_dice)      
        battle_loss_defender = defence.calculate_defender_armies_lost(defence_armies, offence_dice, defence_dice)
        attacker_remaining -= battle_loss_attacker
        defender_remaining -= battle_loss_defender
        attackerLosses.append(battle_loss_attacker)
        print(f'\t Round {roundNumber} : Attacker losses: {battle_loss_attacker} Defender losses: {battle_loss_defender}')
        defenderLosses.append(battle_loss_defender)
        print(f'\t Round {roundNumber} : Attacker armies remaining: {attacker_remaining} Defender armies remaining: {defender_remaining}')

        attack_armies = attacker_remaining
        defence_armies = defender_remaining

        if attack_armies < defence_armies:
            defence_armies = attack_armies
        else:
            attack_armies = defence_armies
        
        roundNumber += 1
        
        
        
        
        
        


    print(attackerLosses)
    print(defenderLosses)


'''
    #RESULTS OF THE BATTLE
    print('\n')
    print('************************************************************************************************')
    print('\t\tRESULTS OF THE BATTLE')
    print('************************************************************************************************')
    print('\n')

    #The number of attacking armies put into the battle
    print(f'The number of attacking soldiers put into the battle was : {attack_armies*attack_dice}')

    #The number of defending armies put into the battle
    print(f'The number of defending soldiers put into the battle was : {defence_armies*defending_dice}')


    #Calculate the number of armies lost by the attacker
    offence_armies_lost = offence.calculate_attacker_armies_lost(attack_armies, offence_dice, defence_dice)
    print(f'The number of attaking soldiers lost in this battle was : {offence_armies_lost}')


    #Calculate the number of armies lost by the defender
    defence_armies_lost = defence.calculate_defender_armies_lost(defence_armies, offence_dice, defence_dice)
    print(f'The number of defending soldiers lost in this battle was : {defence_armies_lost}')

    #Calculate the number of armies remaining for the attacker
    offence_armies_remaining = offence.armies_remaining_attacker(attack_armies, attack_dice, offence_armies_lost)
    print(f'The number of attaking soldiers remaining in this battle was : {offence_armies_remaining}')

    #Calculate the number of armies remaining for the defender
    defence_armies_remaining = defence.armies_remaining_defender(defence_armies, defending_dice, defence_armies_lost)
    print(f'The number of defending soldiers remaining in this battle was : {defence_armies_remaining}')

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
    #print(attacker_percentage)


    # Percentage of wins for the defender   
    defender_percentage = 0
    for i in range (attack_armies):
        if df['Defender Wins'][i] == 2:
            defender_percentage += 1/(attack_armies)
    #print(defender_percentage)

    # Draw percentage
    draw_percentage = 1 - attacker_percentage - defender_percentage
    #print(draw_percentage)

    # Double check the percentages
    draw_percentage_check=0
    for i in range (attack_armies):
        if df['Attacker Wins'][i] == 1 and df['Defender Wins'][i] == 1:
            draw_percentage_check += 1/(attack_armies)

'''
    
    
    

    
    
    
    

