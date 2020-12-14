import re

fhandle = open('input.txt')
lst_bag = []

for row in fhandle:
    row = row.split('contain')
    left_pattern = '(^.*) bag*'
    bag = row[0]
    bag_color = re.findall(left_pattern, bag)
    
    row[1] = row[1].rstrip('.\n')
    rule = row[1]


    lst_bag.append(bag_color[0])
    


#print(lst_contain)
