def sumfun(n, m):
    x = [i for i in range(1, m+1) if i % n == 0]
    y = [i for i in range(1, m+1) if i % n != 0]
    return abs(sum(x)-sum(y))


print(sumfun(4, 20))
