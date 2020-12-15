import re

fhandle = open('input.txt')
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
#print('length of rules:',len(lst_bag))

#check how many bags can contain directly the shiny gold
iterate = True
validbags =  ['.*shiny gold.*']
it = 1
bag_to_skip = []
list_len = {}
while iterate is True: 
    iterator_key = validbags
    #print('check1:',check1)
    #print('valid bags:', validbags)
    validbags_new = []
    for key in lst_bag:
        check = lst_bag.get(key)
        for e in check:
            for color in validbags:
                if re.search(color, e):
                    to_append = str(key)
                    to_append = '.*' + to_append + '.*'
                    if to_append not in validbags_new and to_append not in bag_to_skip:
                        validbags_new.append(to_append)
                        #print('iteration {}, found this colors {}'.format(it, validbags_new))
    bag_to_skip  = bag_to_skip + validbags

    #print('bags to skip:', bag_to_skip)
    #print('new valid bags:', validbags_new)
    validbags = validbags_new
    if iterator_key == validbags:
        iterate = False
    #print('2nd check',check1)
    list_len[it] = len(validbags_new)
    it = it + 1
    #print(list_len)
    #input('enter................')

bag_to_skip.sort()
#print(bag_to_skip)
print(list_len)   
print('puzzle answer is',len(bag_to_skip)-1)







    

