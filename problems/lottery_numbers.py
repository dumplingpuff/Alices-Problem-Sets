from random import choice

def get_winning_combo(possibilities):
    """rondomly select two items from possibilities list and return winning_combo """
    winning_combo=[]

    while len(winning_combo) < combo_size:
        pulled_item=choice(possibilities)
        if pulled_item not in winning_combo:
            winning_combo.append(pulled_item)

    return winning_combo


def get_random_combo(possibilities):
    """rondomly select two items from possibilities list and return random_combo"""
    
    random_combo=[]

    while len(winning_combo) < combo_size:
        pulled_item=choice(possibilities)
        if pulled_item not in random_combo:
            random_combo.append(pulled_item)

    return random_combo

def get_exact_match(ramdon_combo,winning_combo):
    "check ramdon_combo agaist winning_combo, and find exact match"
    matches=0

    for r_item in ramdon_combo:
        for w_item in winning_combo:
            if r_item == w_item:
                matches += 1 
    
    return matches == combo_size

won=False
plays=0
max_tries=1000
matches=0
possibilities=[1,2,3,4,5]
combo_size=2
winning_combo=get_winning_combo(possibilities)

while not won:
    random_combo=get_random_combo(possibilities)
    won=get_exact_match(random_combo,winning_combo)
    if won == True:
        break
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("Congrats! We got a winner!")
    print(f"Your combo is {random_combo}")
    print(f"The winning combo is {winning_combo}")
    print(f"Tried {plays} to win")

else:
    print(f"Tried {plays} times without a winner :(")


    


