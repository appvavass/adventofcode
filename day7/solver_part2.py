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
#print('length of rules:',len(lst_bag))
print(lst_bag)
################

def bagcounter(dictionary,color):


    return out_dict  # in form of color:bags to be contained in it