"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

predict_number_ls = [] # Создание списка с рандомными значениями каждой из 1000 итерациЙ

def random_predict(number: int = 50) -> int:
    """Рандомно задаем число и угадываем его по заданному алгоритму

    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    count = 0                   # Обнуляем число попыток
    global predict_number_ls    # Объявляем глобальный список
    
    predict_number = np.random.randint(1, 101)  # Генерируем "загаданное" число
    predict_number_ls.append(predict_number)
    # Основа задания
    while True:
        count += 1
        if number == predict_number:
            break  # Выход из цикла если угадали
        elif number < predict_number:   # От 50 до 100
            if predict_number == 75:
                break
            elif predict_number < 75:
                number += 1
            elif predict_number>75 and number<75:
                number = 76
            else:
                number += 1                
        else:                           # От 0 до 50
            if predict_number == 25:
                break
            elif predict_number > 25:
                number -= 1
            elif predict_number<25 and number>25:
                number = 24
            else:
                number -= 1
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    dict_of_numbers = {}
    i = 0
    while i < 1000:#random_array:        
        count_ls.append(random_predict())
        dict_of_numbers.update({predict_number_ls[i]:count_ls[i]})
        i += 1  
    
    print(f"Соотношение загаданного значения и числа попыток отгадать его: {dict_of_numbers}")
    score = int(np.mean(count_ls)) #Среднее число попыток отгадать загаданное значение
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
