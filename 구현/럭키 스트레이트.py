n = input()
a = n[:(len(n)//2)]
b = n[(len(n)//2):]

suma = 0
sumb = 0

for i in a:
    suma += int(i)

for i in b:
    sumb += int(i)

if suma == sumb:
    print("LUCKY")
else:
    print("READY")
