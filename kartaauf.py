
xx=int(input())
yy=int(input())

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


print(slova)

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



print(sc)
print(ss)
