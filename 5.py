'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
num = 14
cont = []a = 1
while len(cont) != num:    print(a)    for i in range(1, num+1):        if a % i ==0:            cont.append(a)        else:            cont = []    a += 1print(cont)
two = 2three = 6four = 12five = 60six = 60seven = 420eight = 840nine = 2520ten = 2520eleven = 27720twelve = 27720thirteen = 360360fourteen = 360360


