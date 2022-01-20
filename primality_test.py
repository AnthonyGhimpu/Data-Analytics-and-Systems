import math
def sum_primes(M):
    totalSum = 0
    for x in range(2,M + 1):
        if(is_prime(x)):
             totalSum += x

    print("Sum of Primes from 2 to", M, " is", totalSum,"!")



def is_prime(n):
    trial = math.sqrt(n)
    trial = int(trial)
    while(2 <= trial):
     if((n % trial) == 0):
       return False
     elif((n % trial) > 0):
        trial = trial - 1
     else:
        return True
    return True


x = input("Please enter a Number >=2: ")
x = int(x)
while(x < 2):
    x = input("Please enter a number greater than 2: ")
    x = int(x)

if(is_prime(x)):
    print(x," is prime!")
else:
    print(x," is not prime!")

sum_primes(x)