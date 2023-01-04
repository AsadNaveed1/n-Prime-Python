inp = int(input())
count = 0
for u in range(2, inp):
    checkPrime = True
    target = u
    for i in range(2, int(target/2)+1):
        x = i
        tt = target
        while(tt != 0):
            temp = x
            x = tt
            tt = temp%tt
        gg = x
        if(gg!= 1):
            checkPrime = False
    x2 = inp
    tt2 = u
    while(tt2 != 0):
        temp = x2
        x2 = tt2
        tt2 = temp%tt2
    gg2 = x2       
    if (checkPrime and gg2 == 1):
        count+=1
print(count)
