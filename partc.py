
#1 Create a program to input five marks of a student and display the grades. 

#• Mark > 75 – A 

#• Mark 65 to 75 – B 

#• Mark 55 to 64 – C 

#• Mark 45 to 54 – S 

#• Mark < 45 – F 


i=1
while i <= 5:
  mark = float(input("enter the mark " + str(i)))
  if mark >= 75:
    print("you have got an A pass for mark ", i)
  elif 75 > mark >= 65:
    print("you got a B pass for mark ", i)
  elif 65 > mark >= 55:
    print("you got a C pass for mark ", i)
  elif 55 > mark >= 45:
    print("you got a S pass for mark ", i)
  else:
    print("you got an F pass for mark ", i)
  i += 1

