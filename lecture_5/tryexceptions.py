def convert_ab_to_int(a: str, b: str) -> (int, int):
    a,b = int(a), int(b)
    return a,b


def divide (a: int | float, b: int | float) -> float:
    if 3 in [a,b]:
        raise AttributeError ('Я ненавижу тройки!')
    return a/b


while True:
    a, b = input("Введите два числа: ").split()
    try:
        a,b = convert_ab_to_int(a,b)
        division_score = divide(a,b)
    except Exception as e:
        print(f"Ошибка {e}")
        print('Введите нормальные числа!')
        continue
    except ZeroDivisionError as e:
        print('Без нулей!')

    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print()
    print(f"{a}/{b}")

    # except (ZeroDivisionError, ValueError) as e:
    #     print(f"Ошибка {e}")
    #     print('Введите нормальные числа и нули')
    #     continue

#traceback - путь становления ошибки
#valueerror - со значением
#1_000_000 переведётся в миллион
#программа не падает, просто продолжает работу при tryexcept
#finally выполняется всегда после try или exception вне зависимости от того, что произошло
#чаще finally используется после break, немного
#except Exception ловит абсолютно все ошибки, его надо ставить в конец