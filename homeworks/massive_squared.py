
def func(n):
    list_n = []
    for i in range (-n,n+1):
        i = i**2
        list_n.append(i)
    print (list_n)

a = int(input("Введите число: "))

func(a)