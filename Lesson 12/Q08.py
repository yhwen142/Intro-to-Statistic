#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads

def f(p0,p1,p2):
#Insert your code here
    return p0*p1 + (1-p0)*p2

print(f(0.1,0.9,0.8))