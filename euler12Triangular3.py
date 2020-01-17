

def triangularNoSum(a):
    sum = 0.5*a*(a+1)
    return sum

def divisors(n):
    limit = int(n**0.5)
    divisors_list = []
    for i in range(1, limit+1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(int(n/i))
    return len(divisors_list)

def divisibleTriangularNo(n):
    x = 1
    a = 1
    while x < n+1:
        y = triangularNoSum(a)
        x = divisors(y)
        a += 1
    return y


final = divisibleTriangularNo(500)
print(final)