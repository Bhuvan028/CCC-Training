n=int(input())
for i in range(n):
    v=int(input())
    l=list()
    b='0'
    l.append(b)
    while(len(l)<=v):
        c2=len(l)
        for i in range(c2):
            if (l[i]=='0'):
                l.append('1')
            elif(l[i]=='1'):
                l.append('0') 
    print(l[v])