#to make a calculator 
enter=input("what you want to do + - * /  power pleace enter ")
match enter:
    case "+":
        a=int(input("enter first digit"))
        b=int(input("enter second digit"))
        c=a+b
        print('the addition of',a,'and',b,'is',c)
    case "-":
        a=int(input("enter first digit"))
        b=int(input("enter second digit"))
        c=a-b
        print('the sub of',a,'and',b,'is',c)
    case "*":
        a=int(input("enter first digit"))
        b=int(input("enter second digit"))
        c=a*b
        print('the multiplication of',a,'and',b,'is',c)
    case "/":
        a=int(input("enter first digit"))
        b=int(input("enter second digit"))
        c=a/b
        print('the division of',a,'and',b,'is',c)
    case 'power':
        a=int(input("enter first digit"))
        b=int(input("enter power digit"))
        c=a**b
        print('the power value of',a,'is',b,'is hance soln is',c)
    case _:
        print("error ........  ")# miniproject-
