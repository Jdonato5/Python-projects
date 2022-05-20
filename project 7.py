#Weather Channel/October 30,2019
import time
def high(dt):
    m=max(dt)
    return m

def low(dt):
    m=min(dt)
    return m

def average(x):
    a=round(sum(x)/len(x))
    
    return a

def printme(x,y):
    index=0
    while (index<len(y)):
        print(x[index],y[index])
        index+=1
#main()
days = ['Monday','Tuesday','Wendsday','Thursday','Friday','Saturday','Sunday']
temp=[42,45,86,75,43,73,29]

roster = printme(days,temp)
lowTemp = low(temp)
highTemp = high(temp)
avgTemp = average(temp)

print('Lowest temperature is', lowTemp)
print('Highest temperature is', highTemp)
print('Average temperature is', avgTemp)

#input

#process

#output
