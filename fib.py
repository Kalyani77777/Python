k = int(input())
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,k):
    n3 = n1+n2
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n1
