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

def caesar_encrypt(realText, step):
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