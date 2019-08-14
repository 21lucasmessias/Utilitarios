#converte qualquer base até 16 para decimal
while(1):
    result = 0.0
    base = int(input("Base: "))
    binstr = str(input("Numero: "))
    
    if(binstr == "exit"):
        break
    
    binpot = binstr.find('.')

    if(binpot == -1):
        binpot = len(binstr) - 1

        for b in binstr:
            result += int(b) * pow(base, binpot)
            binpot -= 1
        print(result)

    elif(binpot == 0):
        print("?")

    else:
        binpot -= 1
        for b in binstr:
            if b == '.':
                binpot += 1
                b = 0
            if base == 16:
                if b == 'A':
                    b = 10
                elif b == 'B':
                    b = 11
                elif b == 'C':
                    b = 12
                elif b == 'D':
                    b = 13
                elif b == 'E':
                    b = 14
                elif b == 'F':
                    b = 15           
            print(int(b) * pow(base, binpot))
            result += int(b) * pow(base, binpot)
            binpot -= 1
        print(result)
