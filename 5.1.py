'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

num = 23


cont = []
a = 5354228880 

while len(cont) != num:
    print(a)
    for i in range(1, num+1):
        if a % i ==0:
            cont.append(a)
        else:
            cont = []
    a += 1
print(cont)

one = 1
two = 2
three = 6
four = 12
five = 60
six = 60
seven = 420
eight = 840
nine = 2520
ten = 2520
eleven = 27720
twelve = 27720
thirteen = 360360
fourteen = 360360
fifteen = 360360
sixteen = 720720
seventeen = 12252240
eighteen = 12252240
nineteen = 232792560
twenty = 232792560
twentyone = 232792560
twentytwo = 232792560
twentythree = 5354228880 
