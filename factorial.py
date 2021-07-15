import math

def factor(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factor(n-1)

def lastNDigits(number, position):
    power = math.pow(10, position)
    return math.fmod(number, power)

def powerOfTwo(x):
    return ((x & (x-1))  == 0);

for i in range(0,5):
    f = factor(i)
    print("factorial of ",i," is ", f)

n = 12345
p = lastNDigits(n, 3)
print("lastNDigits of (", n, ",","3) is ", p)
print("powerOfTwo (",4,") = ",powerOfTwo(4))
print("powerOfTwo (",4,") = ",powerOfTwo(6))