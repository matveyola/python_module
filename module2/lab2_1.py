"""
Скласти програму розкладання натурального числа n, уведеного з клавіатури,  
на прості множники.
"""
n = int(input())
a = 2
factors = []
while n != 1:
    if n % a == 0:
        n /= a
        factors.append(a)
    else:
        a+=1
print(factors)