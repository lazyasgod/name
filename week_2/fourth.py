def fibo(n):
    f1=f2=1
    i = 2
    while i < n:
        fsum = f2 + f1
        f1 = f2
        f2 = fsum
        i += 1
    return fsum

print (fibo(10))
