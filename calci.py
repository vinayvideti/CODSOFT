while True:
  print("choose an option")
  print('1-add\n2-subtract\n3-multiplication\n4-division\n5-exit')
  option=int(input("enter a option:"))
  result=0
  if option in [1,2,3,4]:
    num1=int(input('enter a value:'))
    num2=int(input('enter a value:'))
    if option==1:
      result=num1+num2
    elif option==2:
      result=num1-num2
    elif option==3:
      result=num1*num2
    elif option==4:
      result=num1/num2
    print('the result is :',result)
  elif option==5:
    break
  else:
    print("The option was invalid")
 
 
