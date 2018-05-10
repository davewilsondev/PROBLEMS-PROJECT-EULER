'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
num = 14
cont = []
a = 1
while len(cont) != num:    
  print(a)    
  for i in range(1, num+1):        
    if a % i ==0:            
      cont.append(a)        
    else:            
      cont = []    
  a += 1
print(cont)

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
