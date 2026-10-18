while True:
 year = int(input("Please Enter a year(press 0 to close the program)= "))
 if year==0:
    print("Thank You. \nGoodbye!")
    break
 
 if year % 400 == 0:
    print("year" ,year ,"is Leap")
 elif year % 100 == 0:
     print("year" ,year,"is not leap")
 elif year % 4 == 0:
     print("year" ,year,"is Leap")
 else:
     print("year" ,year,"is not Leap")

 print("_"*20)