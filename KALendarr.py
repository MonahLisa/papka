d = int(input())
mon = int(input())
year = int(input())

m=mon

'''if(mon==1):
    m=11
elif(mon==2):
    m=12
else:
    m=mon-2'''

c=year//100

y=(year-c)%100



print((d + ((13*m - 1) // 5) + y + (y // 4 + c // 4 - c*2 + 777))%7)
