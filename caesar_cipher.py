# Caesar cipher
# ------------
# Implement a Caesar cipher, both encoding and decoding.
# The key is an integer from 1 to 25.
# This cipher rotates the letters of the alphabet (A to Z).
# The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A).
# So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".
# This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys


def encoding(text, step):
    alph = 'abcdefghijklmnopqrstuvwxyz'     
    cap = alph.upper()                          #Capital letters
    res = ''

    for l in text:
        if l in alph:                           #For lowercase letter
            i = alph.index(l)                   #Find index letter in alphabet
            if 0 > (i + step) >= 25:
                res += alph[25 - i]
            else:
                res += alph[i + step]
        elif l in cap:                          #For capital letter
            i = cap.index(l)
            if 0 > (i + step) >= 25:
                res += cap[25 - i]
            else:
                res += cap[i + step]
        else:
            res += ' '
    
    return res


ans = int(input('If you want encoding message print 0, else print 1: '))
text = input('Enter you message: ')
step = int(input('Enter step of cipher. If you didn`t know step, enter 0, else enter number 1 - 25: '))

if ans == 1:                                    #Encoding Caesar cipher
    if step == 0:                               #Unknown step
        print('Decoding your message:\n')

        for k in range(1, 26):                  #Iterate all valid step values
            print(encoding(text, k))

    else:                                       #Known step
        step = -step
        print('Decoding your message: ', encoding(text, step))

elif ans == 0:                                  #Decoding Caesar cipher
    if step == 0:                               #Unknown step
        print('Decoding your message:\n')

        for k in range(1, 26):                  #Iterate all valid step values
            print(encoding(text, k))

    else:                                       #Known step
        print('Encoding your message: ', encoding(text, step))

else:
    print('Invalid value. Please try again')
