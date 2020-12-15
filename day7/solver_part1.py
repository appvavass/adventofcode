import re

fhandle = open('input_test.txt')
lst_bag = {}
lst_rules = []

for row in fhandle:
    #divide in bag - rules and create a dictionary {bag color: bag rules}
    row = row.split('contain')
    left_pattern = '(^.*) bag.*'
    bag = row[0]
    bag_color = re.findall(left_pattern, bag)
    bag_color = bag_color[0]
    row[1] = row[1].rstrip('.\n')
    rule = row[1]
    right_pattern = '([0-9]+\s[a-z]+\s[a-z]+)' ##matching a number and two words
    ruleset  = re.findall(right_pattern, rule)
    #rule = rule.split(',')
    #lst_bag[bag_color] = rule
    if len(ruleset) > 0:
        lst_bag[bag_color] = ruleset
#print(lst_bag)

#check how many bags can contain directly the shiny gold
iterate = True
validbags =  ['.*shiny gold.*']
it = 1
while iterate is True: 
    check1 = validbags
    print('check1:',check1)
    print('valid bags:', validbags)
    validbags_new = validbags
    for key in lst_bag:
        check = lst_bag.get(key)
        for e in check:
            for color in validbags:
                if re.search(color, e):
                    to_append = str(key)
                    to_append = '.*' + to_append + '.*'
                    if to_append not in validbags:
                        print('appending:', to_append)
                        validbags_new.append(to_append)
    print('valid bags:', validbags)
    if check1 == validbags:
        iterate = False
    print(it)
    print('2nd check',check1)
    it = it + 1
    
  
    
print('puzzle answer is',len(validbags)-1)






    

