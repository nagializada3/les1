n = int(input())
m = n
cnt = 0
if len(str(n)) == 1:
    print(1)
else:
    while n > 0:
        s = n % 10
        m-=s
        n //= 10
        if n == 0:
            n = m
            cnt+=1
print(cnt)
   