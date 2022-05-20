# Pay calulator / OCT 3, 2019

#INPUT
hours = int(input('how many hours were worked for the week? '))


#Process
   
if hours<=40:
    reghours=hours
    regpay= reghours *40.00
    overtime= 0
    totalpay= regpay
    if reghours== 0:
       print('You did not work this week')
else:
   overtime= hours-40
   overpay= overtime*60.00
   reghours=hours-overtime
   regpay= reghours*40.00
   totalpay= regpay+overpay
   if (overtime + reghours)>80:
      print('Take it easy buddy, you are working yourself to an early grave!')
   
    
#output
print('Hours worked:', hours)
print('Total pay:', totalpay)
print('Hours of overtime:',overtime)
print('Reg hours:', reghours)
    
