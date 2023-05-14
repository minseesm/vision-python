def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
def mod(a, b):   # modular
    return a%b
def pow(a, b):  # a^b
    return a**b

print(' [1] add \n [2] sub \n [3] mul \n [4] div \n [5] mod \n [6] pow \n [exit] Quit')

def calculate(select):
    num1 = float(input('enter first number: '))
    num2 = float(input('enter second number: '))

    if select == '1':
        print(add(num1, num2))
    elif select == '2':
        print(sub(num1, num2))
    elif select == '3':
        print(mul(num1, num2))
    elif select == '4':
        print(div(num1, num2))
    elif select == '5':
        print(mod(num1, num2))
    elif select == '6':
        print(pow(num1, num2))

    
while True:
    select = input('select calculator mode: ')
    if select == 'exit':
        break
    elif select > 0 and select < 7:
        calculate(select)
    else:
        print('Error, input again')
        continue
    