a: list[int] = [1,2,3,3,5]
b: list[int] = [0,0,1,0,1]
#     answer = [0,0,3,0,5]


def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val*b[i] for i,val in enumerate(a)]


def test_mask_list():
    print('проверяем тест маск лист')
    assert mask_list([1,2,3], [0,1,0] == [0,2,0], "маска работает неправильно")


test_mask_list()

# assert нужен, чтобы никто не поменял функцию. иначе, тест выводит ошибку
# никогда не используйте ассерты прямо в функции
# модульное юнит тестирование, тестируется функционал только одной функции

# answer = mask_list(array=a, mask=b)
# print(answer)

# for i in a:
#     answer.append(i*2)
#
# print(list(enumerate(a)))
