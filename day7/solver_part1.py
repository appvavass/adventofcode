import re

fhandle = open('input.txt')
lst_bag = {}

for row in fhandle:
    row = row.split('contain')
    left_pattern = '(^.*) bag*'
    bag = row[0]
    bag_color = re.findall(left_pattern, bag)
    bag_color = bag_color[0]
    row[1] = row[1].rstrip('.\n')
    rule = row[1]
    rule = rule.split(',')
    lst_bag[bag_color] = rule
    
print(lst_bag)

    
    


#print(lst_contain)
