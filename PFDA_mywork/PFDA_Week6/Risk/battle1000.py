class Battle1000:
#This class will simulate 1000 individual battle rounds in Risk and plots the results. The attacker plays 3 dice, and the defender plays 2 dice. 


    #import required classes
    from attacker import Attacker as attacker
    from defender import Defender as defender
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #Request army and dice information from user
    attack_armies = 1000
    attack_dice = 3
    defence_armies = 1000
    defending_dice = 2

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

    # Plot the results as a pie chart

    fig, ax = plt.subplots()

    #Set the font style and size for the title and labels
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Set the title of the pie chart
    ax.set_title('Risk Game Results for 1000 battles', fontdict = font1)

    labels= 'Attacker Wins', 'Defender Wins', 'Draw'
    sizes = [attacker_percentage, defender_percentage, draw_percentage]
    colors = ['blue', 'red', 'green']
    explode = (0.1, 0.1, 0.1)  # explode the slices 

    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    ax.set_xlabel('Percentage of Wins', fontdict = font2)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    #Create a pie chart of the results in the plots folder
    plt.savefig("Plots/battle.png")
    plt.clf()
    plt.close()





 