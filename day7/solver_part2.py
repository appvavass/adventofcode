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
    if len(ruleset) == 0:
        ruleset = [(0, 'other bags')]
    #lst_bag[bag_color] = rule
    lst_bag[bag_color] = ruleset
        
print('LIST_BAG',lst_bag)

def bagcounter(dictionary,color,constant):
## This function goes trhough the dictionary and look for the input colors, 
# return what those colors must contain 
    new_colors = []
    return_dict = {}
    value = dictionary.get(color)
    if value == [(0, 'other bags')]:
        return 0
    else:
        for e in value:
            n_bag = e[0]
            color_bags = e[1]
            #if color_bags not in new_colors:
            new_colors.append(color_bags)
            return_dict[color_bags]  = int(n_bag)*constant 
        #print('function out:', return_dict)
        return return_dict

new_clue = [('shiny gold',1)]

def finalcounter(color):
    x = lst_bag.get(color)[0]
    return x

ciao  = finalcounter('shiny gold')
print(ciao)