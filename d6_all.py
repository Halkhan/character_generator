
def d6_in_order():
    print("Your results are...\n")
    print('{:->30}'.format('-'))
    print("Name: ",char_name,)
    print('{:->30}'.format('-'))


    for i in range(6):
        stats.insert(i, die_adder())
        mods.insert(i, stat_mods(stats[i]))
        print(f'{attributes[i]:15}{stats[i]}{"   "}{mods[i]}')
