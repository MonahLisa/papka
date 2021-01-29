x = input()
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
