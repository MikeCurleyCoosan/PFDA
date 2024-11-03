# Filename: risky.py


# References:
#  PFDA Topic 5 lecture videos (Andrew Beatty) - https://vlegalwaymayo.atu.ie/course/view.php?id=10462
#  https://www.w3schools.com/python/numpy/default.asp for NumPy
#  https://www.w3schools.com/python/numpy/numpy_random.asp for random integer generation
#  https://www.w3schools.com/python/matplotlib_pie_charts.asp for pie charts
#  https://www.geeksforgeeks.org/python-ways-to-add-row-columns-in-numpy-array/ to add rows to a 2D array
#  https://stackoverflow.com/questions/4001067/sum-one-row-of-a-numpy-array to sum a row in a 2D array

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

def do_menu():
    print("\nEnter one of the following:")
    print("1 to specify the number of rounds to play, with unlimited attackers and defenders")
    print("2 to generate a random number of attackers and defenders, and play until one is depleted ")
    print("0 to quit")

    # Ask for a value and check that it is an integer - handle range checking in the main program
    try:
        choice = int(input("\nEnter your choice: "))
    # Handle non-integer entries gracefully
    except ValueError:
        print("Invalid entry, not an integer")
        choice = 0
    return choice

def do_sub_menu():
    # Ask for a value and check that it is an integer - handle range checking in the main program
    try:
        choice = int(input("\nEnter the number of rounds, between 1 and 100K (0 to quit): "))
    # Handle non-integer entries gracefully
    except ValueError:
        print("Invalid entry, not an integer")
        choice = 0
    return choice

def play_specified_rounds():
    total = do_sub_menu()

    if total > 100000:
        print("Be reasonable")

    elif total > 0:
        rounds = 1
        defence_losses = 0
        attack_losses = 0
        while rounds <= total:
            attack = np.random.randint(1, 7, (1,3))
            # order descending and slice the leftmost 2 columns (best results)
            attack[:,::-1].sort()
            print("attack throws for round",rounds,"=",attack)
            attack = attack[:,0:2]
            defence = np.random.randint(1, 7, (1,2))
            # order descending
            defence[:,::-1].sort()
            print("defence throws for round",rounds,"=",defence)
            defender_losses = (attack > defence).sum()
            print("defender losses ",defender_losses)
            attacker_losses = 2-defender_losses
            print("attacker losses ",attacker_losses)

            # Finish it off
            defence_losses += defender_losses
            attack_losses += attacker_losses
            rounds += 1
            #print ("new result = ", result[count])
        rounds -= 1
        print("Attack losses after",rounds,"rounds =",attack_losses)
        print("Defence losses after",rounds,"rounds =",defence_losses)

        # Draw a pie chart of the results
        risk_result = [attack_losses,defence_losses]
        # Add totals to the legend, pie chart shows percentages
        risk_labels = ["Attack Loss: " + str(attack_losses),"Defence Loss: " + str(defence_losses)]
        explode=[0.05, 0.05]
        plt.pie(risk_result, labels = None, autopct='%1.1f%%', explode=explode)
        risk_title = "Risk results for " + str(rounds) + " rounds"
        plt.title(risk_title)
        plt.legend(bbox_to_anchor=(1.0, 0.6), loc='upper left', labels=risk_labels)
        plt.subplots_adjust(right=0.6)
        plt.show()
    return

def play_until_winner():

    attack_army = np.random.randint(100, 10000)
    defence_army = np.random.randint(100, 10000)
    print("Attack army is",attack_army)
    print("Defence army is",defence_army)

    count = 0
    result = np.array([count,attack_army,defence_army, 0, 0])

    while ((attack_army > 0) and (defence_army > 0)):
        attack = np.random.randint(1, 7, (1,3))
        # order each row descending and slice the leftmost 2 columns (best results)
        attack[:,::-1].sort()
        attack = attack[:,0:2]
        defence = np.random.randint(1, 7, (1,2))
        # order each row descending
        defence[:,::-1].sort()
        defender_losses = (attack > defence).sum()
        #print("defender losses ",defender_losses)
        attacker_losses = 2-defender_losses
        #print("attacker losses ",attacker_losses)

        # Finish it off
        defence_army -= defender_losses
        if defence_army < 0:
            defence_army = 0
        attack_army -= attacker_losses
        if attack_army < 0:
            attack_army = 0
        count+=1
        new_row=np.array([count, attack_army, defence_army, attacker_losses, defender_losses])
        result = np.vstack((result, new_row))
        #print ("new result = ", result[count])

    print("Remaining attackers after",count,"rounds =",attack_army)
    print("Remaining defenders after",count,"rounds =",defence_army)

    print (result)
    plt.plot(result[0:count+3, 1])
    plt.plot(result[0:count+3, 2])

    # Adjust the x-scale
    plt.xlim([0, max(result[0:count,0])])
    max1 = max(result[0:count,1])
    max2 = max(result[0:count,2])

    # adjust the y-scale
    maxx = max1
    if max2 > maxx:
        maxx = max2
    maxx = maxx*1.1
    plt.ylim([0, maxx])

    if attack_army > defence_army:
        title_str = "Result: Defence loses"
    else:
        title_str = "Result: Attack loses"

    risk_title = "Risk Results for " + str(count) + " rounds"
    risk_labels = ["Attack","Defence"]
    plt.suptitle(risk_title, fontsize=14)
    plt.title(title_str, loc='left')
    plt.legend(bbox_to_anchor=(1.02, 1.15), loc='upper right', labels=risk_labels)
    plt.show()
    return

# ***************** Main Program *****************

choice = do_menu()

match choice:

    case 0:
        # Exit the program
        print("Exiting...")
        run = False

    case 1:
        # call the function which implements option 1 (play for a specified number of rounds)
        play_specified_rounds()

    case 2:
        # call the function which implements option 2 (play until one side is out of resources)
        play_until_winner()

    case _:
        # Catch-all for entries other than the ones listed above
        print("Invalid entry, exiting...")

