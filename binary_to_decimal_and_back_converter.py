var = int(input('If you want convert binary to decimal enter 0 else if you want convert decimal to binary enter 1: '))

#convert binary to decimal  
if var == 0:
    num = input('Enter the number you want to convert: ')
    num = num[::-1]     #reverse string
    res = 0
    degr = 1
    for n in num:
        n = int(n)
        res += + n * degr
        degr *= 2   #2 to the degree equal to the index n
    print(res)

#convert decimal to binary
elif var == 1:
    num = int(input('Enter the number you want to convert: '))
    num = bin(num)
    res = str(num)
    res = num[2::]
    print(res)

else:
    print('There is no such option, try again')
