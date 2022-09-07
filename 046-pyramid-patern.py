def pyramid_pattern(n):
    a = 2 * n - 2

    for i in range(n):
        for j in range(a):
            print(end=' ')
        a -= 1
        for j in range(i + 1):
            print('*', end=' ')
        print('\r')


pyramid_pattern(10)
