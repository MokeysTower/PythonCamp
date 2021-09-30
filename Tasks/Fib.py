def fib(n):
    n1=0
    n2=1
    n3=0
    for i in range(n-2):
        n3 = n1+ n2
        n1 = n2
        n2 = n3
    return n3
print(fib(7))

def recFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recFib(n-1) + recFib(n-2)

print(recFib(7))