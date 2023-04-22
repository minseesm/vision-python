def input_numbers() :
    x = float(input("first number : "))
    y = float(input("second number : "))
    z = add(x, y)
    return z

def add(a, b) :
    return a + b

result = input_numbers()

print(result)
