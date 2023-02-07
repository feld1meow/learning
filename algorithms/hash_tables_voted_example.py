voted = {}


def check_voter(name):
    if voted.get(name):  # функция get возвращает значение, если ключ 'tom' есть в хеш-таблице
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')


print(voted)
check_voter('Tom')
check_voter('Dave')
print(voted)
check_voter('Tom')
