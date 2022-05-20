#Intake calulator/ Oct 16,2019

#Input

def incalories ():
    cal = int(input('Enter number of calories'))  
    return cal

def incarbohydrate():
    carbs= int(input('Enter number of carbohydrates'))
    b= carbs
    return b

#Process

def procalories(a):
    caloriesFromFat= a * 9
    c=caloriesFromFat
    return c

def procarbohydrate(b):
    caloriesFromCarbs= b*4
    d = caloriesFromCarbs
    return d
    
    
    
#Output
def outPutTotals (c,d):
    print('calories', c)
    print('carbohydrate',d)



    
#main()
x= incalories()
y= incarbohydrate()
x=procalories(x)
y= procarbohydrate(y)
outPutTotals(x,y)

   
    
