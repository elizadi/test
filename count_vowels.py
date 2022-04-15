# Count Vowels
# Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

def vowels(text):
    text = list(text)

    a = int(text.count('a'))
    e = int(text.count('e'))
    i = text.count('i')
    o = text.count('o')
    u = text.count('u')
    y = text.count('y')
    all_vowels = a + e + i + o + u + y

    return a, e, i, o, u, y, all_vowels

text = input('Enter text: ')
print('In text a - %i, e - %i, i - %i, o - %i, u - %i, y - %i, all vovels - %i' % vowels(text))