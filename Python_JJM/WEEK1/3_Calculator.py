def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modular(a, b):
    return a % b

print("[1] Add")
print("[2] Sub")
print("[3] Mul")
print("[4] div\n[5] modular")
print("[exit] Quit Program")

select = '0'
while select != 'exit':
    select = input("Enter your choice (1/2/3/4/5/exit) : ")

    num1 = float(input("input first number : "))
    num2 = float(input("input second number : "))

    if select == '1' :
        print(add(num1, num2))
    elif select == '2':
        print(sub(num1, num2))
    elif select == '3':
        print(mul(num1, num2))
    elif select == '4':
        print(div(num1, num2))
    elif select == '5':
        print(modular(num1, num2))
    elif select == 'exit':
        break
    else:
        print('Error, plz input in range 1 to 5')
        continue

    