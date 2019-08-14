#Calcula os dias entre duas datas, considerando a ideia de anos bissextos e meses com mais ou menos dias
di = 14
mi = 8
ai = 2018
df = 12
mf = 8
af = 2019
cont = ai

def dias(d, m, a):
    dt = 0
    if bissexto(a):
        lm = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        lm = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for i in range(1, m):
        dt += lm[i]
    dt += d
    return dt


def bissexto(a):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        return True
    else:
        return False


if af < ai:
    print('ano final < ano inicial')
elif ai == af:
    dd = dias(df, mf, af) - dias(di, mi, ai)
else:
    dd = 0
    while True:
        if cont == af:
            dd += dias(df, mf, af)
            break
        elif cont == ai:
            if bissexto(cont):
                dd += 366 - dias(di, mi, ai)
            else:
                dd += 365 - dias(di, mi, ai)
        elif cont < af:
            if bissexto(cont):
                dd += 366
            else:
                dd += 365
        cont += 1

print(dd)
