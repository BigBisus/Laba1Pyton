print ('Введите колличество элементов в списке:')
n = int(input())
print ('\n')
list = []
for i in range(n):
    list.append(int(input()))

print(list)

mx=0
mn=10^10
sm=0
for i in range(len(list)):
    if mx < list[i]:
        mx=list[i]
    if mn > list[i]:
        mn = list[i]
    sm+=list[i]
print('Минимальное =',mx,'\nМаксимальное =',mn)

list.sort()
print('Отсортированный список =',list)