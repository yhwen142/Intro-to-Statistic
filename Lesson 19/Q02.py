#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
def median(data):
    #Insert your code here
    data = sorted(data)
    n = len(data)
    x = int(n//2)
    if n % 2 == 0:
        return (data[x] + data[x - 1])/2
    else:
        return data[x]

print(median(data1))