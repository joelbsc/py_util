# Given a integer n, returns the nth term of the fibonacci sequence
def fibonacci (x):
    try:
        if x > 1:
            fibo = fibonacci(x-1) + fibonacci(x-2)
        elif x == 1:
            fibo = 1
        else:
            fibo = 0

        return fibo 
    except:
        return 0

# Encode a given string with ceaser cipher method, in which each letter in the realtext is replaced 
# by a letter some fixed number of positions (steps) down the alphabet.
def caesar_encrypt(realText, step):
    try:
        if type(realText) != str or type(step) != int:
            raise TypeError

        ucase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lcase= ucase.lower()

        cipherText = ''

        for c in realText:
            if c.isalpha():
                if c in ucase:
                    cipherText += ucase[(ucase.index(c)+step)%26]
                else:
                    cipherText += lcase[(lcase.index(c)+step)%26]
            else:
                cipherText += c

        return cipherText

    except TypeError:
        print('Parâmetros inválidos: realText deve ser string e step inteiro')