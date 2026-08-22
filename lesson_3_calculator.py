print('WELCOME_TO_CALCULATOR','ENTER_NUMBER',sep='\n')
x = float(input())
print('\n','\n','\n','SELECT_OPERATION: + , - , * , / ')
usless_1 = True
while usless_1 is True:
    usless_1 = False
    operation = input(f'{x} ')
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        print('\n','\n','\n','ENTER_NEXT_NUMBER')
        usless_2 = True
        while usless_2 is True:
            y = float(input(f'{x} {operation} '))
            y = round(y,2)
            if y!=0 or operation!='/':
                usless_2 = False
                if operation == '+':
                    z = x+y
                elif operation == '-':
                    z = x-y
                elif operation == '*':
                    z = x*y
                elif operation == '/':
                    z = x/y
                z = round(z,2)
                print('\n','\n','\n','RESULTAT','\n',f'{x} {operation} {y} = {z}')
            else:
                usless_2 = True
                print('\n','\n','\n',f'YOU_CANT {x}/{y} TRY_AGAIN','\n')

    else:
        usless_1 = True
        print('\n','\n','\n','ENTER_CORECT_OPERATION')
  