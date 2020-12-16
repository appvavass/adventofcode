import re

fhandle = open('input.txt')
lst_bag = {}
lst_rules = []

########################################################
#divide in bag - rules and create a dictionary {bag color: bag rules tuple (number, color)}
########################################################

for row in fhandle:
    row = row.split('contain')
    left_pattern = '(^.*) bag.*'
    bag = row[0]
    bag_color = re.findall(left_pattern, bag)
    bag_color = bag_color[0]
    row[1] = row[1].rstrip('.\n')
    rule = row[1]
    right_pattern = '([0-9]+)\s([a-z]+\s[a-z]+)' ## two words
    ruleset  = re.findall(right_pattern, rule)
    #rule = rule.split(',')
    #lst_bag[bag_color] = rule
    if len(ruleset) > 0:
        lst_bag[bag_color] = ruleset
#print(lst_bag)

def bagcounter(dictionary,colors):
## This function goes trhough the dictionary and look for the input colors, 
# return what those colors must contain 
    new_colors = []
    return_dict = {}
    for color in colors:
        value = dictionary.get(color)
        if value is None: return
        else:
            for e in value:
                n_bag = e[0]
                color_bags = e[1]
                if color_bags not in new_colors:
                    new_colors.append(color_bags)
                    return_dict[color_bags]  = int(n_bag) 
        #print('function out:', return_dict)
        return return_dict

init_clue = ['shiny gold']
tier = 0
solution = []

while True:
    answer = bagcounter(lst_bag,init_clue)
    solution.append((tier, answer))
    tier +=1
    init_clue = []
    #print('solution', solution)
    #print('answer:', answer)
    if answer is not None:
        for k in answer:
            init_clue.append(k)
    else: break

print(solution)
