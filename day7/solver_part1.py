import re

fhandle = open('input.txt')
lst_bag = {}
lst_rules = []

########################################################
#divide in bag - rules and create a dictionary {bag color: bag rules (string)}
########################################################

for row in fhandle:
    row = row.split('contain')
    left_pattern = '(^.*) bag.*'
    bag = row[0]
    bag_color = re.findall(left_pattern, bag)
    bag_color = bag_color[0]
    row[1] = row[1].rstrip('.\n')
    rule = row[1]
    right_pattern = '[0-9]+\s([a-z]+\s[a-z]+)' ## two words
    ruleset  = re.findall(right_pattern, rule)
    #rule = rule.split(',')
    #lst_bag[bag_color] = rule
    if len(ruleset) > 0:
        lst_bag[bag_color] = ruleset
#print('length of rules:',len(lst_bag))
#print(lst_bag)
########################################################
#check how many bags can contain directly the shiny gold
########################################################

#define the function that finds which bag can contains the target color

def bagsearcher(dictionary, target):
    output = []
    for color in target:
        #print('searching for color:', color)
        for key, val in dictionary.items():
            #print('looking into bag:', key)
            #print(key, 'bag can contain only:', val)
            if color in val and color not in output:
                output.append(key)
    return output

colortofind = ['shiny gold']
saved_solution = []

while True:
    solution = bagsearcher(lst_bag, colortofind)
    for e in solution:
        if e not in saved_solution:
            saved_solution.append(e)
    colortofind = solution
    if solution == []: break

print('puzzle answer is',len(saved_solution))








    

