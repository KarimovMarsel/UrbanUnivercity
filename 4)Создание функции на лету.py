first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y:x.lower() == y.lower(), first, second)))

def get_advanced_writer(file_name):
    if not isinstance(file_name, str):
        file_name = str(file_name) + '.txt'
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for i in data_set:
                file.write(f'{i}\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        from random import choice
        return choice(self.words)

from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())