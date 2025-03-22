from random import randint

num=[]
chet=[]
div3=[]
sm=0

for i in range(20):
    num.append(randint(1,100))
for i in range(len(num)):
    if (num[i] % 2) == 0:
        chet.append(num[i])
    if (num[i] % 3) == 0:
        div3.append(num[i])
    sm+=num[i]

print('Чётные =',chet,'\nКратные трём =',div3,'\nСреднее арифметическое',(sm//len(num)))