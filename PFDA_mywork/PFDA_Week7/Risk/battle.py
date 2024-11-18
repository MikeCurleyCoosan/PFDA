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
    import seaborn as sns   

    
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
    startingCountAttack = (attack_armies*attack_dice)
    startingCountDefence = (defence_armies*defending_dice)
    attacker_remaining = attack_armies*attack_dice
    defender_remaining = defence_armies*defending_dice
    roundNumber = 1


    while attacker_remaining >= 3 and defender_remaining >=2:

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
        attackerLosses.append(attacker_remaining)
        print(f'\t Round {roundNumber} : Attacker losses: {battle_loss_attacker} Defender losses: {battle_loss_defender}')
        defenderLosses.append(defender_remaining)
        print(f'\t Round {roundNumber} : Attacker armies remaining: {attacker_remaining} Defender armies remaining: {defender_remaining}')

        attack_armies = int(attacker_remaining/3)
        defence_armies = int(defender_remaining/2)

        if attack_armies < defence_armies:
            defence_armies = attack_armies
        else:
            attack_armies = defence_armies
        
        roundNumber += 1


    print(attackerLosses)
    print(defenderLosses)



    #RESULTS OF THE ROUNDS OF BATTLES
    print('\n')
    print('************************************************************************************************')
    print('\t\tRESULTS OF THE ROUNDS OF BATTLES')
    print('************************************************************************************************')
    print('\n')

    #The number of attacking armies put into the battle
    print(f'The number of attacking soldiers put into the battle was : {startingCountAttack}')

    #The number of defending armies put into the battle
    print(f'The number of defending soldiers put into the battle was : {startingCountDefence}')


    #Calculate the number of armies lost by the attacker
    offence_armies_lost = (startingCountAttack) - attackerLosses[-1]
    print(f'The number of attaking soldiers lost in this battle was : {offence_armies_lost}')


    #Calculate the number of armies lost by the defendeer
    defence_armies_lost = (startingCountDefence) - defenderLosses[-1]
    print(f'The number of defending soldiers lost in this battle was : {defence_armies_lost}')

    #Calculate the number of armies remaining for the attacker
    offence_armies_remaining = attackerLosses[-1]
    print(f'The number of attaking soldiers remaining in this battle was : {offence_armies_remaining}')

    #Calculate the number of armies remaining for the defender
    defence_armies_remaining = defenderLosses[-1]
    print(f'The number of defending soldiers remaining in this battle was : {defence_armies_remaining}')

    print('\n')
    print('************************************************************************************************')

    #Plot the results of the battle

    #Create a dataframe to store the results of the battle
    results = pd.DataFrame({'Attacker Remaining': attackerLosses, 'Defender Remaining': defenderLosses})

    print(results)

    #Plot the results of the battle# Plot the results as a pie chart
    fig, ax = plt.subplots()
    #Set the font style and size for the title and labels
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Set the colors for the plot
    colors = ['blue', 'red', 'green']
    sns.lineplot(y=results['Attacker Remaining'], x=results.index, color='blue', label='Attacker Remaining')
    sns.lineplot(y=results['Defender Remaining'], x=results.index, color='red', label='Defender Remaining')
    #Set the title of the plot
    plt.title('Results of the Mulit-Battle', fontdict = font1)
    #Set the x-axis label
    plt.xlabel('Number of rounds', fontdict = font2)
    #Set the y-axis label
    plt.ylabel('Number of Armies Remaining', fontdict = font2)

    #Add a grid
    ax.grid(True, which='both', linestyle='--', linewidth=0.4)


    #Save the plot as a png file
    plt.savefig("Plots/Multi-battle.png")
    plt.clf()
    plt.close()

