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