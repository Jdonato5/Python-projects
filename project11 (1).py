#project11/Johnny Donato/ November 20,2019

#class
class Employee:
    def __init__(self,name,pay,hours):
        self.name = name
        self.hours = hours 
        self.pay= 0
#Assessor methods
    #Set method
    def setname(self):
        self.name= n
    def setpay (self):
        self.pay=p
    def sethours (self):
        self.hours= h
        
    #get method                
    def getname (self):
        return self.name
    def getpay (self):
        return self.pay
    def gethours(self):
        return self.hours
    
    def emppay():
        pay=houres*80.00
        return pay
    
class Newemp(Employee):
    #constructor
    def __init__(self,name,pay,hours,payrate):
        Employee.__init__(self,name,pay,hours)
        self.payrate = payrate
        
    #set
    def setpayrate(self,pr):
        self.payrate = pr
    def getpayrate(self):
        return self.payrate
  
    def newemppay(self,hours,payrate):
        self.pay = self.hours * self.payrate
        return self.pay

