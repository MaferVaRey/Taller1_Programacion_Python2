num1 = int(input('ingrese el primer número: '))
num2 = int(input('ingrese el segundo número: '))
num3 = int(input('ingrese el tercer número: '))
num4 = int(input('ingrese el cuarto número: '))

if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux
if num1 > num3:
    aux = num3
    num3 = num1
    num1 = aux
if num1 > num4:
    aux = num4
    num4 = num1
    num1 = aux
if num2 > num3:
    aux = num3
    num3 = num2
    num2 = aux
if num2 > num4:
    aux = num4
    num4 = num2
    num2 = aux
if num3 > num4:
    aux = num4
    num4 = num3
    num3 = aux

print(num1)
print(num2)
print(num3)
print(num4)
