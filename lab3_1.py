def is_square(x):
    return (int(x ** 0.5)) ** 2 == x


def prime_number(n):
    a = 2
    while n % a != 0:
        a += 1
    return a == n
def calc1(n):
    if prime_number(n):
        return  '1 ' + str(n)
    if n <= 1:
        return 'Число має бути більше 0'
    if n % 2 == 0:
        return 'Число має бути непарне'
    if is_square(n):
        return str(int(n ** 0.5)) + ' ' + str(int(n ** 0.5))
    x = int(n ** 0.5) + 1
    while not is_square(x * x - n):
        x += 1
    y = int((x * x - n) ** 0.5)
    a, b = x - y, x + y
    return str(a)+' '+str(b)