#Задача номер 1
print("Задание номер 1")
print("Введите координаты клада(x, y) на разных строчках")
xx=int(input())
yy=int(input())
print("Теперь вводите ходы")

slovo=''
k=0
slova=[]

ss='север'

while slovo != 'стоп':
    slovo=str(input())
    if((slovo=='направо')or(slovo=='налево')or(slovo=='разворот')or(slovo=='стоп')):
        k=0
    else:
        k=int(input())
    slova.append([slovo, k])

x=0
y=0
sc=0
for i in range(len(slova)):
    if((x==xx)and(yy==y)):
        break
    else:
        if(slova[i][0]!='вперёд'):
            
            if(slova[i][0]=='направо'):
                if(ss=='север'):
                    ss='восток'
                elif(ss=='юг'):
                    ss='запад'
                elif(ss=='восток'):
                    ss='юг'
                elif(ss=='запад'):
                    ss='север'
            
            elif(slova[i][0]=='налево'):
                if(ss=='север'):
                    ss='запад'
                elif(ss=='юг'):
                    ss='восток'
                elif(ss=='восток'):
                    ss='север'
                elif(ss=='запад'):
                    ss='юг'

            elif(slova[i][0]=='разворот'):
                if(ss=='север'):
                    ss='юг'
                elif(ss=='юг'):
                    ss='север'
                elif(ss=='восток'):
                    ss='запад'
                elif(ss=='запад'):
                    ss='восток'
            sc=sc+1

        else:
            if(ss=='север'):
                y=y+slova[i][1]
            elif(ss=='юг'):
                y=y-slova[i][1]
            elif(ss=='восток'):
                x=x+slova[i][1]
            elif(ss=='запад'):
                x=x-slova[i][1]
            sc=sc+1


print()
print("Минимальное количество ходов до клада: ", sc)
print("Направление: ", ss)
print()







#Задача номер 2
print("Задание номер 2")
print("Введите день, месяц и год на разных строчках")
d = int(input())
m = int(input())
year = int(input())

c=year//100

y=(year-c)%100


print()
print((d + ((13*m - 1) // 5) + y + (y // 4 + c // 4 - c*2 + 777))%7)
print()





#Задача номер 3
print("Задание номер 3")
print("Введите строку")
x = input()
print()
print(x[2])
print(x[len(x)-2])
print(x[0:5])
print(x[0:len(x)-2])
s=''
for i in range(len(x)):
    if(i%2==0):
        s=s+x[i]
print(s)
s=''
for i in range(1,len(x)):
    if(i%2!=0):
        s=s+x[i]
print(s)
ss=x[::-1]
print(ss)

s=''
for i in range(0, len(x), 2):
    s=s+ss[i]
print(s)
print(len(x))
