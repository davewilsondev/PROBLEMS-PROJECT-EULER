'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

# work out the factors 

numFact = 600851475143
facts = []


for i in range(numFact):
    x = numFact/(i+1)
    if x % 1 == 0:
        facts.append(x)
        print(x)
        
print(facts)
largestPrimeFact = facts[-1]
print(largestPrimeFact)
        
