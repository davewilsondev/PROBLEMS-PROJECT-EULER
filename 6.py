"""The sum of the squares of the first ten natural numbers is, 
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

list1 = []
list2 = []
length = 100

for i in range(1,length+1):
    a = i**2
    list1.append(a)

for i in range(1,length+1):
    a = i
    list2.append(a)

sq = sum(list1)
sumsq = sum(list2)**2

answer = sumsq - sq
print(answer)