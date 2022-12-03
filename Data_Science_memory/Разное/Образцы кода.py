




if a == 10:
    print('a equals 10') # a равно 10
elif a < 10:
    print('a is less than 10') # a меньше 10
else:
    print('a is more than 10') # a больше 10

				#Исключения
try:
    *код, который может вызвать ту или иную ошибку*
except *ошибка*:
    *код, который выполнится в случае возникновения ошибки*
else:
    *код, который выполнится только в случае, если в try ничего не сломалось*
finally:
    *код, который выполнится в любом случае*

try:
    print("Before exception") # перед исключением
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c) # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e:
    print("After exception") # после исключения
else: # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т. е. не произошло никакого исключения)
    print("Everything's fine!") # всё отлично!
finally: # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally finished!") # наконец-то завершено!
 
print("After After exception") # после после исключения




# Создадим тот же словарь
grades = {'Ivanov': 5, 'Smirnov': 3, 'Kuznetsova': 4, 'Tihonova': 5}
# Только попробуем (try — пробовать) напечатать оценку студента,
# которого нет в словаре
try:
   print(grades['Pavlov'])
# А если возникнет ошибка в ключе (KeyError), скажем,
# что студента нет в словаре
except KeyError:
   print("Student’s mark was not found!")
# Будет напечатано:
# Student’s mark was not found!


	
for value in iterator:
    # Начало блока кода с телом цикла
    ...
    ...
    ...
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла	

#range(начало, конец (число-1), шаг)
print(list(range(1, 10, 2)))
# [1, 3, 5, 7, 9]

while условие:
    # Начало блока кода с телом цикла
    # пока условие истинно, цикл выполняется
    ...
    ...
    ...
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла


import random
num = random.randint(0, 10000)


#Матрицы
for i in range(N): 
    for j in range(M): 
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку

# 0 1 2
# 3 4 5

#min and max

random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value: 
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value: 
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Minimal elements:", min_value_rows) # минимальные элементы
print("Their indices:", min_index_rows) # их индексы
print("Maximal elements:", max_value_rows) # максимальные элементы
print("Their indices:", max_index_rows) # их индексы



list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей, 
# где на первом месте стоит индекс, а затем значение 
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):  
    print("Element index: ", i) # индекс элемента
    print("Element value: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("End of the cycle") # конец цикла


heads = 35  # количество голов
legs = 94  # количество ног

for r in range(heads + 1):  # количество кроликов
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов или ног превышено, переходим на следующий шаг цикла
        if (r + ph) > heads or \
            (r * 4 + ph * 2) > legs: 
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Number of rabbits", r) # количество кроликов
            print("Number of pheasants", ph) # количество фазанов
            print("---")


#Отсортируйте список по алфавиту и подсчитайте количество одинаковых слов. 
#Для этого используйте словарь. Ключом будет являться слово, а значением — число его вхождений в предложение.

sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm'
print(sentence)

#приводим к нижнему регистру
sentence = sentence.lower() 
print(sentence)

#заменяем все запятые на ничего (удаляем запятые)
sentence = sentence.replace(',', '') 
print(sentence)

#разделяем строку на набор слов из строки
sentence = sentence.split(' ')
print(sentence)

#сортируем по алфавиту
sentence.sort() 
print(sentence)

dict1 = {} #создаем словарь

for i, valye in enumerate(sentence):
    chislo_raz = 0 #создаем переменную, для подсчета числа раз в теле цикла, для обнуления значения переменной
    
    for j,valye in enumerate(sentence):
        dict1.update({sentence[i]:chislo_raz})
        if sentence[i] == sentence[j]:
            chislo_raz += 1
            
print(dict1)


#Вывод
A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm
a robot may not injure a human being or, through inaction, allow a human being to come to harm
a robot may not injure a human being or through inaction allow a human being to come to harm
['a', 'robot', 'may', 'not', 'injure', 'a', 'human', 'being', 'or', 'through', 'inaction', 'allow', 'a', 'human', 'being', 'to', 'come', 'to', 'harm']
['a', 'a', 'a', 'allow', 'being', 'being', 'come', 'harm', 'human', 'human', 'inaction', 'injure', 'may', 'not', 'or', 'robot', 'through', 'to', 'to']
{'a': 3, 'inaction': 1, 'allow': 1, 'injure': 1, 'or': 1, 'through': 1, 'come': 1, 'may': 1, 'robot': 1, 'being': 2, 'not': 1, 'harm': 1, 'human': 2, 'to': 1}


			#ФУНКЦИИ
#Функция — это фрагмент программного кода, к которому можно обратиться из другого места программы.
#Аргумент (параметр) — это независимая переменная, значение которой используется функцией для выполнения своего исходного кода.

def first_function():
    print("Hello world!")

def first_function():
    pass #Дает понять интерпретатору, что пока в теле функции ни чего нет, но разработчик про это не забыл.
		 #и интерпретатор не выдаст ошибку

def get_time(distance, speed):
   # Если расстояние или скорость отрицательные, то возвращаем ошибку
   if distance < 0 or speed < 0:
       # Оператор raise возвращает (raise — досл. англ. "поднимать")
       # объект-исключение. В данном случае ValueError (некорректное значение).
       # Дополнительно в скобках после слова ValueError пишем текст сообщения
       # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
       raise ValueError("Distance or speed cannot be below 0!")
   result = distance / speed
   return result


			#print доп функции
#sep='' - Этот аргумент задаёт строку, которая будет разделять позиционные аргументы, переданные на печать (по умолчанию это пробел).
print(25, 125, 625, sep=', ')
# Будет напечатано:
# 25, 125, 625
#end='' - Этот аргумент задаёт символ, которым заканчивается печатаемая строка (по умолчанию это перенос на новую строку — символ \n).

			#Оператор распаковки *
# В массив args будут записаны все переданные
# порядковые аргументы. Он ставится в конце и перед **. Его тип кортеж (tuple).
def mean(*args):
   # Среднее значение — это сумма всех значений,
   # делённая на число этих значений
   # Функция sum — встроенная, она возвращает
   # сумму чисел
   result = sum(args) / len(args)
   return result
 
# Передадим аргументы в функцию через запятую,
# чтобы посчитать их среднее
print(mean(5,4,4,3))
# Будет напечатано
# 4.0

→ Оператор распаковки * можно использовать и для передачи значений из списка в функцию.

Рассмотрим эту возможность на примере функции print. У нас есть список:

langs = ['Python', 'SQL', 'Machine Learning', 'Statistics']
Напечатаем его разными способами. Самый простой:

print(langs)
# Будет напечатано:
# ['Python', 'SQL', 'Machine Learning', 'Statistics']
В данном случае список был напечатан с характерными для него квадратными скобками на границах и кавычками у строк. Так список превращается в строку по умолчанию.

Чтобы напечатать слова в списке langs через пробел, достаточно в функции print перед langs поставить * как оператор распаковки:

print(*langs)
# Будет напечатано:
# Python SQL Machine Learning Statistics

Оператор * удобно использовать для печати списков в более читабельном виде.

Оказывается, можно передавать разное число именованных аргументов с помощью ещё одного оператора распаковки — двух звёздочек подряд (**).

Переменная kwargs — стандартное название для совокупности именованных аргументов в Python (сокр. от англ. keyword arguments — «именованные аргументы»).

Однако вместо kwargs можно использовать любое другое адекватное название переменной.

Напишем функцию schedule, которая будет печатать расписание по дням. Для начала узнаем, что будет храниться в переменной kwargs после использования оператора **:

# В переменную kwargs будут записаны все
# именованные аргументы
def schedule(**kwargs):
   # kwargs — это словарь, проверим это с помощью isinstance:
   print(isinstance(kwargs, dict))
   # Напечатаем объект kwargs
   print(kwargs)
 
schedule(monday='Python', tuesday='SQL', friday='ML')
# Будет напечатано:
# True
# {'monday': 'Python', 'tuesday': 'SQL', 'friday': 'ML'}
Итак, kwargs является словарём, в котором ключами являются имена аргументов, а значениями — переданные аргументам значения.
			
С помощью оператора ** можно передавать в функцию нескольких аргументов. Он используется для передачи именованных аргументов с помощью словаря, 
который в дальнейшем будет распакован. Кроме того, оператор ** является оператором распаковки, только для словарей. 
Ключами словаря выступают названия аргументов, а значениями — те значения аргументов, которые должны быть им присвоены.

			#Стек
Аналогичным образом, когда Python при выполнении одной функции встречает шаг, на котором требуется выполнить другую функцию, 
он кладёт начальную функцию в стэк, пока выполняет вторую. Если и во второй окажется ссылка на другую функцию, вторая задача 
также будет отложена в стэк. Так будет продолжаться до тех пор, пока наконец какая-нибудь функция не вернёт конкретное значение. 
Тогда интерпретатор начнёт свой обратный путь по стэку для выполнения отложенных, ожидающих решения задач. 

			#Рекурсия
def factorial(n):
   # Задаём условия выхода из рекурсии:
   if n==0: return 1
   if n==1: return 1
   # Во всех других случаях возвращаем
   # произведение текущего числа n и функции от n-1
   return factorial(n-1)*n

print(factorial(4))



# Импортируем модуль для работы с системными переменными
import sys
# Увеличим глубину рекурсии
sys.setrecursionlimit(1000000000)
print(len(str(factorial(970))))
# Будет напечатано:
# 2478

			функция Time
from time import time
import sys
sys.setrecursionlimit(1000000000)
 
def factorial(n):
   if n==0: return 1
   if n==1: return 1
   return factorial(n-1)*n
a = time()
for i in range(100):
  factorial(10000)
b = time()
print(b-a)
# Будет напечатано:
# 4.058465242385864

			#ИТЕРАТОРЫ iter()
В Python из многих встроенных структур данных (списков, словарей, множеств) можно получать итераторы. Происходит это с помощью функции iter().
print(isinstance(new_list, list)) - соответствует ли тип переменной new_list list

К любому итератору можно применить функцию next(), которая возвращает следующий элемент из итератора. Сделаем так четыре раза:

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
# Будет напечатано:
# 12
# 14
# 16
# StopIteration:

Однако из-за ошибки прекращается дальнейшая работа программы, что нежелательно. Чтобы программа не ломалась, достаточно добавить обработку исключения StopIteration на каждом шаге получения следующего элемента:

users = ['admin', 'guest', 'root', 'anonymous']
iter_users = iter(users)
 
while True:
   try:
       print(next(iter_users))
   except StopIteration:
       print("User list is over!")
       break
 
# Будет напечатано:
# admin
# guest
# root
# anonymous
# User list is over!
Теперь программа печатает имена пользователей до тех пор, пока не появится исключение StopIteration. 
Когда возникает исключение, ничего фатального также не происходит: 
вместо аварийного завершения программы выводится надпись «Все пользователи напечатаны!», 
и выполнение цикла while прекращается с помощью break.

Стандартным способом работы с итератором является цикл for:

users = ['admin', 'guest', 'root', 'anonymous']
iter_users = iter(users)
 
for user in iter_users:
   print(user)
 
# Будет напечатано:
# admin
# guest
# root
# anonymous
Как видите, работать с итераторами в цикле for предельно просто — даже обрабатывать исключения не потребовалось. 



			#ГЕНЕРАТОРЫ
Вот код генератора:

def deposit(money, interest):
   # Процент по вкладу преобразуем во множитель:
   # делим процент на 100 и прибавляем 1
   interest = interest/100 + 1
   while True:
       # Сумма на вкладе через год — это
       # текущая сумма, домноженная на множитель и
       # округлённая до 2 знаков после запятой
       money = round(interest * money, 2)
       yield money
Как видите, генератор использует ту же сигнатуру, что и функция.

print(next(deposit))
Будет объект функцией или генератором, определяется наличием оператора yield в коде. 
Этот оператор также возвращает следующее за ним значение в исходный код основного скрипта, 
однако интерпретатор запоминает место, на котором он завершил работу с генератором и возвращается 
на то же место при повторном обращении к генератору. В случае с return повторное выполнение функции произошло бы с самого начала. 

В однострочных генераторах можно также использовать условия. Например, посчитаем кубы первых 15 натуральных чисел, которые делятся на 3:

triple_cubes_generator = (x**3 for x in range(1,16) if x % 3 == 0)
print(type(triple_cubes_generator))
print(list(triple_cubes_generator))
# Будет напечатано:
# <class 'generator'>
# [27, 216, 729, 1728, 3375]


			#lambda - функция
Сразу разберём пример. Допустим, мы хотим создать функцию, считающую квадратный корень из числа. Можно сделать это классическим способом:

def root(num):
    # Напоминание: в Python используется оператор **
    # для возведения числа в степень.
    # В математике возведение в степень ½ соответствует
    # вычислению квадратного корня.
    return num ** (1/2)

			
А теперь запишем то же самое с помощью lambda-функции:

root = lambda num: num**(1/2)			

# Для получения корня произвольной степени от числа
# (например, корня степени 4) необходимо возвести исходное
# число в степень, равную единице, делённой на желаемую
# степень корня.
nth_root = lambda num, n: num**(1/n)
print(nth_root(16,4))
# Будет напечатано:
# 2.0
# Напоминание: оператор % используется для получения остатка
# от деления. Если остаток от деления на 2 равен 0, то
# число является чётным.
# Обратный слэш (\) используется в Python для того,
# чтобы перенести одну строку кода на следующую строку.
# Получается, что компьютер интерпретирует записанное ниже
# как одну строку.
is_even = lambda num: "even" if num % 2 == 0 \
    else "odd"


6.3
def logger(name):											#Прописываем наддекоратор, который принимает нужный параметр
    def decorator(func):									#Прописываем декоратор, который принимает декорируемую функцию
    # Вместо pass напишите код декоратора					
        def decorated_func(*args, **kwargs):				#Прописываем параметры декорируемой фунции
            result = func(*args, **kwargs)					#Строка, для сохранения работоспособности фунции
            print(name,': Function root started',sep='')	#Вывод сообщений
            print(name,': Function root finished',sep='')	#Вывод сообщений
            return result									#Возврат результата (не изменённого) декорируемой функции
        return decorated_func								#Возврат продекорированной функции
    return decorator    									#Возврат наддекорируемой фунции (c названиеv, времtytv выполнения...)




@logger('tyt_pishem_name')									#Прием параметра для наддекорирования
def root(val, n=2):											#Прописываем функцию как обычно
   res = val ** (1/n)
   return res
 
print(root(25))												#Обращаемся к функции
# tyt_pishem_name: Function root started
# tyt_pishem_name: Function root finished
# 5.0



#Проверка на високостность
def is_leap(year):
    # Вместо pass напишите тело функции
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) == True:
        return True #год високостный
    else:
        return False#год не високостностный

print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))
# True
# False
# True
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































