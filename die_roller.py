import random
import time
import sys
import os
import d6_all

die_min = 1
die_max = 6


def restart_program():
    """Restarts the current program. Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def roller():
    """Rolls 1d6"""
    roll = random.randint(die_min, die_max)
    return roll


def die_adder():
    """Adding the 3 highest dice of 4d6"""
    dice = []
    dice.insert(0, roller())
    dice.insert(1, roller())
    dice.insert(2, roller())
    dice.insert(3, roller())
    dice.sort()
    total_dice = dice[1] + dice[2] + dice[3]
    if total_dice < 7:
        total_dice = 7
    return total_dice


def stat_mods(mod):
    """Provides stat modifiers"""
    if stats[i] == 7:
        mod = " -2"
    elif stats[i] == 8 or stats[i] == 9:
        mod = " -1"
    elif stats[i] == 10 or stats[i] == 11:
        mod = " 0"
    elif stats[i] == 12 or stats[i] == 13:
        mod = "+1"
    elif stats[i] == 14 or stats[i] == 15:
        mod = "+2"
    elif stats[i] == 16 or stats[i] == 17:
        mod = "+3"
    elif stats[i] == 18 or stats[i] == 19:
        mod = "+4"
    elif stats[i] == 20 or stats[i] == 21:
        mod = "+5"
    return mod

#only used for 3rd option
def stat_evaluator_mod():
    x = selected
    if stats[x] >= 19:
        print("This characteristic cannot go any higher.")
        return 0
    if stats[x] <= 6:
        print("This characteristic cannot go any lower.")
        return 0
    if stats[x] == 18:
        return int(4)
    if stats[x] == 16 or stats[x] == 17:
        return int(3)
    if stats[x] == 14 or stats[x] == 15:
        return int(2)
    if stats[x] >= 8 and stats[x] <= 13:
        return int(1)
    if stats[x] == 7:
        return int(2)


def print_stats():
    for i in range(6):
        mods.insert(i, stat_mods(stats[i]))
        y = 1 + i
        print(f'{"   "}{y}{"      "}{attributes[i]:15}{stats[i]:3}{"     "}{mods[i]:7}{"0"}\n')


def validate_selection():
    while True:
        try:
            selection = int(input("What characteristic would you like to adjust? (1 - 6)"))
            break
        except ValueError:
            print("Invalid entry, try again (1 - 6)")
            validate_selection()
    if 1 <= selection <= 6:
        return selection
    else:
        print("That is an invalid entry, try again (1 - 6)")
        validate_selection()


attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"] #sets names of characteristics
stats = [] #used for changing values of stats
mods = []  #user for changing values of modifiers


while True:
    # Create character start
    char_create = input("Would you like to create a character? (y/n)\n")
    # Insert a clear screen command?
    if char_create == "yes" or char_create == "y":
        print("Generating character...\n\n")
        break

    elif char_create == "no" or char_create == "n": #may not need to be used, modify else...
        print("Don't waste my time!")
        restart_program()
    else:
        print("Use yes or no.")
        restart_program()


char_name = input("What is your characters name?\n ")
print("How would you like to generate stats?\n")
print("1: Roll 4d6 minus the lowest die in order - Str, Dex, Con, Int, Wis, Chr\n")
print("15: Roll 4d6 minus the lowest die in order - Str, Dex, Con, Int, Wis, Chr\n")
print("2: Roll 4d6 minus the lowest die, selecting where results go?\n")
print("3: Distribute points from a pool?\n")
print("35: Distribute points from a pool?\n")
create_choice = input()

if create_choice == "15":
    d6_all.d6_in_order()

#Generation 1 option - 4d6 minus lowest die in order
if create_choice == "1":
    print("Your results are...\n")
    print('{:->30}'.format('-'))
    print("Name: ",char_name,)
    print('{:->30}'.format('-'))


    for i in range(6):
         stats.insert(i, die_adder())
         mods.insert(i, stat_mods(stats[i]))
         print(f'{attributes[i]:15}{stats[i]}{"   "}{mods[i]}')


#Generation 2 option - 4d6 minus lowest die selecting placement
elif create_choice == "2":

    def stat_check(): #validates that the value selected is in the list
        try_again = stat_select
        while try_again not in set_stats:
            print("Invalid Option")
            print(*set_stats)
            try_again = int(input("Try again"))
        return try_again


    set_stats = [] #Rolls the dice for stats
    for i in range(6):
        set_stats.insert(i, die_adder())


    for i in range(6):
        print('{:->30}'.format('-'))
        print("Available selections:", "\n", *set_stats)
        print('{:->30}'.format('-'))
        print("You need to select a stat for", attributes[i])
        stat_select = int(input("Type the value want to use: \n"))
        stat_check()
        set_stats.remove(stat_select)
        stats.insert(i, stat_select)

    print("\n\n")
    print('{:->30}'.format('-'))
    print("Name: ",char_name,)
    print('{:->30}'.format('-'))

    for i in range(6):
        mods.insert(i, stat_mods(stats[i]))
        print(f'{attributes[i]:15}{stats[i]}{"   "}{mods[i]}')


#Generation Option 3, Using a Stat Pool------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
if create_choice == "3":

    def print_stats():
        for i in range(6):
            mods.insert(i, stat_mods(stats[i]))
            y = 1 + i
            print(f'{"   "}{y}{"      "}{attributes[i]:15}{stats[i]:3}{"     "}{mods[i]:7}{"0"}\n')


    def validate_selection():
        while True:
            try:
                selection = int(input("What characteristic would you like to adjust? (1 - 6)"))
                break
            except ValueError:
                print("Invalid entry, try again (1 - 6)")
                validate_selection()
        if 1 <= selection <= 6:
            return selection
        else:
            print("That is an invalid entry, try again (1 - 6)")
            validate_selection()


    def print_selection(selection, attributes):
        y = int(selection) - 1
        print("You selected,", attributes[y])


    def pool_check():
        add_subed = input("Add or Subtract? ('a' for add, 's' for subtract)")
        if add_subed == "a":
            stat_cost()
            return "a"
        elif add_subed == "s":
            return "s"
        else:
            print("Invalid entry, try again (`a` to add and `s` to subtract)")
            pool_check()


    def stat_cost():
        if stat_pool - stat_evaluator_mod() < 0:
            print("invalid selection, not enough points")
            validate_selection()
        else:
            return


    def add_modify_stats(stats):
        stats[selected] = stats[selected] + 1
        return stats


    def sub_modify_stats(stats):
        legal = 0
        while legal == 0:
            if stats[selected] -1 < 7:
                print("Invalid selection, characteristic cannot go any lower.")
                break
            else:
                stats[selected] = stats[selected] - 1
                legal = 1
                return stats


    def modify_pool():
        stat_evaluator_mod()
        #print(stat_evaluator_mod())
        return stat_evaluator_mod()


    def pool_zero():
        if stat_pool == 0:
            #print(print_stats)
            #print(stat_pool)
            answer_pool = input("Are you done creating your character? (y/n)")
            if answer_pool == "n":
                return 1
            elif answer_pool == "y":
                print("Congradulations, you are done!")
                return 0
            else:
                print("Invalid selection, try again. (y/n)")
                pool_zero()
        else:
            return 1


    stat_pool = 20
    stats = [10] * 6
    phantom_pool = 1
    while phantom_pool == 1:
        for i in range(6):
            mods.insert(i, stat_mods(stats[i]))
        print('{:->45}'.format('-'))
        print_stats()
        print("Remaining points:", stat_pool)
        selected = validate_selection() - 1
        print("You selected:a ", attributes[selected])
        add_sub = pool_check()
        if add_sub == "a":
            print("Adding a point to", attributes[selected])
            add_modify_stats(stats)
            stat_pool = stat_pool - stat_evaluator_mod()
        elif add_sub == "s":
            print("Subtracting a point from", attributes[selected])
            sub_modify_stats(stats)
            if stats[selected] > 7:
                stat_pool = stat_pool + stat_evaluator_mod()
            else:
                stat_pool = stat_pool
        else:
            print("ummmmmm")
        modify_pool()
        print("Points remaining:", stat_pool)
        print('{:->45}'.format('-'))
        print(f'{"(Number)":2}{"(Characteristic)":16}{"(Stat)":5}{"(+Cost)":7}{"(-Return)"}')
        phantom_pool = pool_zero()
    print("\n")
    print('{:->30}'.format('-'))
    print("Name: ", char_name, )
    print('{:->30}'.format('-'))
    for i in range(6):
        mods.insert(i, stat_mods(stats[i]))
        print(f'{attributes[i]:15}{stats[i]}{"   "}{mods[i]}')



if create_choice == "35":
    stat_pool = 20
    stats = [10] * 6
    selected = validate_selection()

    #test
    print("Stat Pool:", stat_pool)
    print("Stats:", stats)
    # for i in range(6):
    #     #     print_stats()

    #input("Select a characteristic to modify", validate_selection())
