#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
data2=[88.63, 37.64, 60.34, 9.6, 46.7, 9.6, 35.07, 20.47, 29.06, 12.37, 9.6, 8.34, 30.28, 91.66, 55.7, 10.93, 87.22, 92.5, 4.37, 81.42, 10.65, 51.54, 34.46, 87.42, 90.01, 80.53, 99.01, 39.01, 5.73, 94.78, 36.36, 18.08, 87.96]
def mode(data):
    #Insert your code here
    highest_count = 0
    for i in range(len(data)):
        count = data.count(data[i])
        if count > highest_count:
            highest_count = count
            mode = data[i]
    return mode