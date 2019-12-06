from random import randint

N = 1000

def simulate(N):
    K = 0
    ###insert your code here###
    for i in range(N):
        true = randint(1,3)
        guess = randint(1,3)
        if true == guess:
            opendoor = randint(1,3)
            while opendoor == true:
                opendoor = randint(1,3)
            else:
                opendoor = 6 - true - guess
            guess2 = 6 - guess - opendoor
            if guess2 == true:
                K += 1
    return float(K) / float(N)

print simulate(N)