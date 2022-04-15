def factorial(num, res, count):
    if num <= 1:
        return 1
    while count <= num:
        return factorial(num, res * count, count + 1)
    else:
        return res

r = 1
c = 1
n = int(input('Print number: '))
print('Factorial %d = ' %n, factorial(n, r, c))