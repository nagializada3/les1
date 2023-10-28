# n = int(input())
# m = n
# cnt = 0
# if len(str(n)) == 1:
#     print(1)
# else:
#     while n > 0:
#         s = n % 10
#         m-=s
#         n //= 10
#         if n == 0:
#             n = m
#             cnt+=1
# print(cnt)


n = int(input())
l = []
a = 0
while len(l) < n:
    if a % 2 != 0 and a % 3 != 0 and a % 5 != 0:
        l.append(a)
    a +=1
for i in l:
    print(i,end=' ')

   