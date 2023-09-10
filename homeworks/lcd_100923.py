def nod(a: int, b: int):
    c = 0
    while True:
        c = a - b
        if c < b:
            print(c)
            break
        a = b
        b = c

if __name__ == '__main__':
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    nod(x,y)