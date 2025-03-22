n = int(input())
Fak=1
print('\n')
while n > 0:
    print(n)
    Fak*=n
    n-=1
print('Факториал = ',Fak)