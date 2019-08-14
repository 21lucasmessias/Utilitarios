def pp(primo, cont):
    for i in range(1, int(primo/2+1)):
        if primo % i == 0:
            cont += 1
    if cont == 1:
        return primo
    else:
        return pp(primo+1, 0)


def fatorar(a, b, primo):
    if primo > min(a, b):
        return 1
    if a % primo == 0 and b % primo == 0:
        return primo
    return fatorar(a, b, pp(primo + 1, 0))


a = int(input('A: '))
b = int(input('B: '))
primo = 0

while(a != 0 and b != 0):
    primo = 0
    while primo != 1:
        primo = 0
        primo = fatorar(a, b, 2)
        print(f'Primo: {primo}\n{a} {b}')
        a = int(a/primo)
        b = int(b/primo)
    a = int(input('A: '))
    b = int(input('B: '))
