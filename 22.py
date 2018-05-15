"""Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

import string
a1 = dict(zip(string.ascii_uppercase, range(1,27)))
final = []
overall = []

# open the file 
f = open(r"C:\Users\DDWN\Desktop\22.txt","r")
a = f.read()
b = a.replace('"','')

#convert the contents of the file into a list 
c = b.split(",")
d = len(c)
c1 = sorted(c)

#sort the list into a dictionary 
dicts = {}
keys = range(1,d)

for i in keys:
    dicts[i] = c1[i]
    
#work out the score for each
for i in keys:
    k = 0
    for j in dicts[i]:   
        l = a1[j]
        k = k + l
    final.append(k)

final = [49]+final

s = 1
for x in final:    
    y = x * s
    overall.append(y)
    s = s + 1

   
print(sum(overall))
             




#work out the total score 

