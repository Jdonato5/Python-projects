#project5/Johnny Donato/ Oct 16,2019

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
    caloriesFomFat= a * 9
    c=caloriesFomFat
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

   
    
