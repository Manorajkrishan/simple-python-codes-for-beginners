i = 0
sum = 0
newmax = 0
#newmin=0

while i < 10:

  mark = float(input("enter the mark"))
  sum = mark + sum
  tem = max(mark, newmax)
  tep=min(mark,tem)
  newmin=tep
  newmax = tem
  i = i + 1
avg =sum/10  
print("The maximum mark is : " ,newmax)
print("The minimum maks is : " ,newmin)
print("The avarage mark of student is : ",avg)

