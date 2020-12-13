import re
##cleaning the input file, note that you need to add an extra \n at the end of the input.txt in order to make this work for now...

passport = open('input.txt')
plist = []
bufferrow = []

#Här lägger jag till en rad

for row in passport:
    if row != '\n':
        row = row.rstrip('\n')
        lst =  row.split()
        for e in lst:
            bufferrow.append(e)
    else:
        plist.append(bufferrow)
        bufferrow = []

#print(plist)
scanlist = []

for entry in plist:
    #pdata = {'byr':None,'iyr':None,'eyr':None,'hgt':None,'hcl':None,'ecl':None,'pid':None,'cid':None}
    pdata = {}
    for voice in entry:
        voice = voice.split(':')
        up = {voice[0]:voice[1]}
        pdata.update(up)
    scanlist.append(pdata)

## not we have a list of dictionaries, one for each passport

#print(scanlist[len(scanlist)-1])
validp_counter = 0

#creating the checking functions according to given criterias

def byr_check(p):
    x = p.get('byr')
    x = int(x)
    if x < 2003 and x >1919:
        print('valid birthday')
        return 1
def iyr_check(p):
    x = p.get('iyr')
    x = int(x)
    if x < 2021 and x > 2009:
        print('valid issue year')
        return 1
def eyr_check(p):
    x = p.get('eyr')
    x = int(x)
    if x < 2031 and x > 2019:
        print('valid expiration year')
        return 1
def hgt_check(p):
    x = p.get('hgt')
    if re.search('in$',x):
        hgt = x[:2]
        hgt = int(hgt)
        if hgt > 58 and hgt <77:
            print('valid height in inches')
            return 1
    if re.search('cm$',x):
        hgt = x[:3]
        hgt = int(hgt)
        if hgt < 194 and hgt > 149:
            print('valid height in cm')
            return 1
def hcl_check(p):
    x = p.get('hcl')
    if re.search('#[a-f0-9]{6}', x):
        print('valid hair color')
        return 1
def eye_check(p):
    col = ['amb','blu','brn','gry','grn','hzl','oth']
    if p['ecl'] in col:
        print('valid eye color')
        return 1
def pnm_check(p):
    x = p.get('pid')
    x = int(x)
    if x < 1000000000:
        print('valid ID nmr')
        return 1        

#now run the check for each passport


for p in scanlist:
    print(p)
    scan_out = []
    try:
        scan_out.append(pnm_check(p))
        scan_out.append(eye_check(p))
        scan_out.append(hcl_check(p))
        scan_out.append(hgt_check(p))
        scan_out.append(eyr_check(p))
        scan_out.append(iyr_check(p))
        scan_out.append(byr_check(p))
        
        ### if something does not pass the check, it will give a Nan in the scan_out, and therefore no SUM operation will be performed, therefore no valid passport
        
        total_score = sum(scan_out)
        print('valid passport')
        validp_counter += 1
    except:
        print('invalid passport')
    
    #input('enter to continue with passport {}'.format(it))
#print(digits_list)


print('there are {} valid passports'.format(validp_counter))

##Still i get the wrong number of valid passports    



    

    






