n = int(input())
summ=0
for i in range(n+1):
    print('Число = ',i)
    print('Квадрат = ',i^2,'\n')
    summ+=i
print('Сумма =',summ)