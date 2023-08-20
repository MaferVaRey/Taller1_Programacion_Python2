num1 = int(input('ingrese el primer número: '))
num2 = int(input('ingrese el segundo número: '))
num3 = int(input('ingrese el tercer número: '))
num4 = int(input('ingrese el cuarto número: '))

primer = 0
segundo = 0
tercero = 0
ultimo = 0

if num1 <= num2 and num1 <= num3 and num1 <= num4:
    primer = num1
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    primer = num2
elif num3 <= num2 and num3 <= num1 and num3 <= num4:
    primer = num3
elif num4 <= num2 and num4 <= num3 and num4 <= num1:
    primer = num4

if num1 == primer:
    if num2 <= num3 and num2 <= num4:
        segundo = num2
    elif num3 <= num2 and num3 <= num4:
        segundo = num3
    elif num4 <= num2 and num4 <= num3:
        segundo = num4
if num2 == primer:
    if num1 <= num3 and num1 <= num4:
        segundo = num1
    elif num3 <= num1 and num3 <= num4:
        segundo = num3
    elif num4 <= num1 and num4 <= num3:
        segundo = num4
if num3 == primer:
    if num1 <= num2 and num1 <= num4:
        segundo = num1
    elif num2 <= num1 and num2 <= num4:
        segundo = num2
    elif num4 <= num1 and num4 <= num2:
        segundo = num4
if num4 == primer:
    if num1 <= num3 and num1 <= num2:
        segundo = num1
    elif num3 <= num1 and num3 <= num2:
        segundo = num3
    elif num2 <= num1 and num2 <= num3:
        segundo = num2

if num1 == primer and num2 == segundo or num1 == segundo and num2 == primer:
    if num3 <= num4:
        tercero = num3
    elif num4 <= num3:
        tercero = num4
if num1 == primer and num3 == segundo or num1 == segundo and num3 == primer:
    if num2 <= num4:
        tercero = num2
    elif num4 <= num2:
        tercero = num4
if num1 == primer and num4 == segundo or num1 == segundo and num4 == primer:
    if num3 <= num2:
        tercero = num3
    elif num2 <= num3:
        tercero = num2
if num2 == primer and num3 == segundo or num2 == segundo and num3 == primer:
    if num1 <= num4:
        tercero = num1
    elif num4 <= num1:
        tercero = num4
if num2 == primer and num4 == segundo or num2 == segundo and num4 == primer:
    if num1 <= num3:
        tercero = num1
    elif num3 <= num1:
        tercero = num3
if num3 == primer and num4 == segundo or num3 == segundo and num4 == primer:
    if num2 <= num1:
        tercero = num2
    elif num1 <= num2:
        tercero = num1

if num1 == primer:
    if num2 == segundo and num3 == tercero or num2 == tercero and num3 == segundo:
        ultimo = num4
    if num2 == segundo and num4 == tercero or num2 == tercero and num4 == segundo:
        ultimo = num3
    if num3 == segundo and num4 == tercero or num3 == tercero and num4 == segundo:
        ultimo = num2
if num2 == primer:
    if num1 == segundo and num3 == tercero or num1 == tercero and num3 == segundo:
        ultimo = num4
    if num1 == segundo and num4 == tercero or num1 == tercero and num4 == segundo:
        ultimo = num3
    if num3 == segundo and num4 == tercero or num3 == tercero and num4 == segundo:
        ultimo = num1
if num3 == primer:
    if num2 == segundo and num1 == tercero or num2 == tercero and num1 == segundo:
        ultimo = num4
    if num2 == segundo and num4 == tercero or num2 == tercero and num4 == segundo:
        ultimo = num1
    if num1 == segundo and num4 == tercero or num1 == tercero and num4 == segundo:
        ultimo = num2
if num4 == primer:
    if num2 == segundo and num3 == tercero or num2 == tercero and num3 == segundo:
        ultimo = num1
    if num2 == segundo and num1 == tercero or num2 == tercero and num1 == segundo:
        ultimo = num3
    if num3 == segundo and num1 == tercero or num3 == tercero and num1 == segundo:
        ultimo = num2

print(primer)
print(segundo)
print(tercero)
print(ultimo)
