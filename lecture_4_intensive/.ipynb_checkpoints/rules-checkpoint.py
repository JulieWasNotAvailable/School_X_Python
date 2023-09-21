#переменные маленькими буквами, с подчёркиваниями
#капсом - константы
AGE_OF_CONSENT: int = 16


def do_stuff(x: int) -> str: #если пничего не возвращает, писать none
    return 'nothing'


if __name__ == "__main__":
    do_stuff(str(x=AGE_OF_CONSENT))