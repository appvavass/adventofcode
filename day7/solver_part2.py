import re

fhandle = open('input_test.txt')
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
    sum_of_bags = 0
    new_colors = []
    return_dict = {}
    for color in colors:
        value = dictionary.get(color)
        for e in value:
            n_bag = e[0]
            color_bags = e[1]
            if color_bags not in new_colors:
                new_colors.append(color_bags)
                return_dict[color_bags]  = int(n_bag)
 
    return return_dict

init_clue = ['shiny gold']
totalbags = 0


answer = bagcounter(lst_bag,init_clue)
    

print(answer)
