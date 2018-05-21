
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

### need to get to grips with while loops. shouldnt be using for loops to do this. 
final = []

for i in range(125800,130000000):
    print(i)
    if sorted(set(str(i))) == sorted(set(str(i*2))) and sorted(set(str(i))) == sorted(set(str(i*3))) and sorted(set(str(i))) == sorted(set(str(i*4))) and sorted(set(str(i))) == sorted(set(str(i*5))) and sorted(set(str(i))) == sorted(set(str(i*6))):
        final.append(i)
        break
    else:
        continue
    
    

print(final)

        



    