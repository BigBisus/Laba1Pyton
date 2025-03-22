x,y,z = int(input()), int(input()), int(input())
max=0
if max < x :
    max= x
elif max < y :
    max= y
elif max < z:
    max= z
min = 10^10
if min > x :
    min= x
elif min > y :
    min= y
elif min > z:
    min= z
print('Максимальное = ',max,'\nМинимальное = ',min)

if x == y ==z:
    print('они равны')
else:
    print('они не равны')
