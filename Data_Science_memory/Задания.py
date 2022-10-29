//////////////
///3.2///
////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



//////////////
///5.1-7.12///
////////////
def between_min_max(*nums):
    # Вместо pass напишите тело функции
    if len(nums) == 1:
        return float(nums[0])
    min_num = min(nums)
    #print("min_num = ", min_num)
    max_num = max(nums)
    #print("max_num = ", max_num)
    return (min_num + max_num) / 2



print(between_min_max(10))
print(between_min_max(1,2,3,4,5))
# 10.0
# 3.0
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.1-7.13///
////////////
def best_student(**students):
    # Вместо pass напишите тело функции
    #print(students)
    min_values = min(students.values())
    #print(min_values)
    bad_student = 0
    for name,val in students.items():
        if val == min_values:
            bad_student = name  
            return bad_student

print(best_student(Tom=12, Mike=3))
print(best_student(Tom=12))
print(best_student(Tom=12, Jerry=1, Jane=2))
# Mike
# Tom
# Jerry    
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.1-7.14///
////////////
#is_palindrom = lambda str: if str == str.reverse():\ return yes \ else: \ return no
is_palindrom = lambda str: 'yes' if str == str[::-1] else 'no'

print(is_palindrom('1234'))
print(is_palindrom('12321'))
# no
# yes   
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////







//////////////
///5.1-7.15///
////////////
area = lambda a,b: a*b

print(area(12,5))
# 60
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.1-7.16///
////////////
between_min_max = lambda *nums: (min(nums)+max(nums))/2

print(between_min_max(1,2,3,4,5))
# 3.0
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.1-7.17/// Сдать на проверку
/////////////
def sort_ignore_case(ls):
    ls.sort(key=lambda x: x.lower())
    return ls


print(sort_ignore_case(['abf','Acc', 'abc']))
# ['abc', 'Acc']

#Обычный sort ставит на первое место большие буквы, а нужно без привязки к заглавности букв


#додклать. остановился 29.09.21 в 00:46
def sort_ignore_case(ls):
    # Вместо pass напишите тело функции
    ls_small = ls.copy()
    ls_small.sort()
    print(ls)
    print(ls_small)


print(sort_ignore_case(['abf','Acc', 'abc']))
# ['abc', 'Acc']

#Обычный sort ставит на первое место большие буквы, а нужно без привязки к заглавности букв
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.1-7.18/// Сдать на проверку
/////////////
def exchange(usd = None, rub = None, rate = None):
    # Вместо pass напишите тело функции
    # Задайте аргументы по умолчанию
    if usd != None and rub != None and rate != None:
        raise ValueError('Too many arguments')
    try:
        if usd == None:
            usd = rub / rate
            #print("USD = ")
            return usd
        if rub == None:
            rub = usd * rate
            #print("RUB = ")
            return rub
        if rate == None:
            rate = rub / usd
            #print("Rate = ")
            return rate
    except TypeError as e:
        raise ValueError('Not enough arguments')



#print(exchange(usd=100, rub=8500))
#print(exchange(usd=100, rate=85))
#print(exchange(rub=1000, rate=85))
# 85.0
# 8500
# 11.764705882352942
#print(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments
#print(exchange(rub=1000))
# ValueError: Not enough arguments
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.2-7.7///
////////////
def power(val, n):
    if n==0: return 1
    if n==1: return val
    return power(val, n-1)*val


print(power(25,0))
print(power(-5,4))
# 1
# 625
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.2-7.8///
////////////
def is_leap(year):
    # Вместо pass напишите тело функции
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) == True:
        return True
    else:
        return False

print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))
# True
# False
# True
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///5.2-7.9///
////////////
def is_leap(year):
    # Вместо pass напишите тело функции
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) == True:
        return True #год високостный
    else:
        return False

#Все аргументы должны быть целыми числами (проверить с помощью type(day) is int).
#Годом рождения не может быть год до 1900 и год после 2022.
#День рождения должен находиться между крайними значениями с учётом месяца и високосности года.

def check_date(day, month, year):
    # Вместо pass напишите тело функции
    #Проверяем на тип INT
    #if type(day and month and year) == int: #не работает
    if type(day) == int and type(month) == int and type(year) == int:
        #Проверяем на "долгожителей" и "не родившихся"
        if 1900<year<2022:
            #Проверяем на крайние значения дней
            #28 - невисокостный февраль
            #29 - високостный февраль
            #30 - 4,6,9,11,
            #31 - 1,3,5,7,8,10,12
            if is_leap(year) == True:
                #Для високостного
                if 0<day<30 and month == 2:
                    return True
                elif 0<day<31 and month in (4,6,9,11):
                    return True
                elif 0<day<32 and month in (1,3,5,7,8,10,12):
                    return True
                else:
                    return False
                
            else:    
                #Для невисокостного
                if 0<day<29 and month == 2:
                    return True
                elif 0<day<31 and month in (4,6,9,11):
                    return True
                elif 0<day<32 and month in (1,3,5,7,8,10,12):
                    return True
                else:
                    return False
                
        else:
            return False
    else:
        return False


print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))
# True
# True
# False
# False
# False
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.2-7.10/// Скинуть на проверку
/////////////
def check_date(day, month, year):
    def is_leap(year):
    # Вместо pass напишите тело функции
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) == True:
            return True #год високостный
        else:
            return False
    # Вместо pass напишите тело функции
    #Проверяем на тип INT
    #if type(day and month and year) == int: #не работает
    if type(day) == int and type(month) == int and type(year) == int:
        #Проверяем на "долгожителей" и "не родившихся"
        if 1900<year<2022:
            #Проверяем на крайние значения дней
            #28 - невисокостный февраль
            #29 - високостный февраль
            #30 - 4,6,9,11,
            #31 - 1,3,5,7,8,10,12
            if is_leap(year) == True:
                #Для високостного
                if 0<day<30 and month == 2:
                    return True
                elif 0<day<31 and month in (4,6,9,11):
                    return True
                elif 0<day<32 and month in (1,3,5,7,8,10,12):
                    return True
                else:
                    return False
                
            else:    
                #Для невисокостного
                if 0<day<29 and month == 2:
                    return True
                elif 0<day<31 and month in (4,6,9,11):
                    return True
                elif 0<day<32 and month in (1,3,5,7,8,10,12):
                    return True
                else:
                    return False
                
        else:
            return False
    else:
        return False
        



#Напишите функцию register(surname, name, date, middle_name, registry).

#Эта функция принимает на вход фамилию, имя, дату рождения (в виде кортежа из трёх чисел — день, месяц, год), 
#отчество и список, в который необходимо сохранить полученные аргументы в виде кортежа в следующем порядке:
#фамилия, имя, отчество, день, месяц, год рождения

#Функция возвращает список, в который добавила запись. 

#Указание: сделайте отчество аргументом по умолчанию со значением None, 
#так как отчество может быть не у всех регистрирующихся.

#Также сделайте так, чтобы пустой список создавался в том случае, если он не был передан извне.

#Наконец, проверьте дату на корректность. Если дата неправильная, 
#верните ошибку ValueError("Invalid Date!"). Для этого вам пригодится функция из предыдущего задания.

def register(surname, name, date, middle_name=None, registry = None):
    local_reg = list()
    tpl_people = (surname, name, middle_name, date[0], date[1], date[2])
    if check_date(*date) == False:
        raise ValueError("Invalid Date!")
    if registry is None:
        registry = list()
    registry.append(tpl_people)
    return registry
    
    
 

        


reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)
# [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]
 
reg = register('Ivanov', 'Sergej', (24, 13, 1995))
# ValueError: Invalid Date!
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.2-7.11/// Скинуть на проверку
/////////////
def sort_registry(registry):
    # Вместо pass напишите тело функции
    registry.sort(key=lambda index:
        (index[-1], index[-2], index[-3], index[0], index[1], index[2]))
    return registry

reg = [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003),
      ('Ivanov', 'Sergej', None, 24, 9, 1995),
      ('Smith', 'John', None, 13, 2, 2003)]
 
reg = sort_registry(reg)
print(reg)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.2-7.12/// Скинуть на проверку
/////////////
#Напишите функцию get_strings(registry), которая отбирает из предыдущего списка 
#кортежей только те записи, в которых год 2000 и больше (2001, 2002 и т.д.). 
#Затем возвращается список строк в формате: Фамилия И.О., дд.мм.гггг или Фамилия И., дд.мм.гггг, если нет отчества. 


def get_strings(registry):
    #Вместо pass напишите тело функции
    spisok = list()
    #Преобразуем в нужный формат
    def reform(people):
        surname = str(people[0])
        name = str(people[1][0])
        day = str(people[3]).zfill(2)
        mounth = str(people[4]).zfill(2)
        year = str(people[5]).zfill(4)
        date = day+'.'+mounth+'.'+year
        if people[2] is None:
            return (surname+' '+name+'., '+date)
        else:
            middle_name = str(people[2][0])
            return (surname+' '+name+'.'+middle_name+'., '+date)
    
    #Проверяем условие >= 2000
    after2000 = filter(lambda x: x[-1] >= 2000, registry)
    spisok = map(reform,after2000)
    
    return list(spisok)
    
    #Проверяем условие >= 2000
    #for i in range(len(registry)):
    #    if registry[i][-1] >= 2000:
    #        spisok.append(reform(registry[i]))
    #return spisok    
    
    

reg = [('Ivanov', 'Sergej', None, 24, 9, 1995),
      ('Smith', 'John', None, 13, 2, 2003),
      ('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003)]

print(get_strings(reg))
# ['Smith J., 13.02.2003', 'Petrova M.I., 13.03.2003']
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.2-7.13/// Скинуть на проверку
/////////////
def group_gen(n):
    # Вместо pass напишите тело генератора
    i = 0
    while i < n:
        i += 1
        yield i
        if i == n:
            i = 0
            
    


groups = group_gen(3)
for _ in range(10):
   print(next(groups))
# 1
# 2
# 3
# 1
# 2
# 3
# 1
# 2
# 3
# 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///5.2-7.14/// Скинуть на проверку
/////////////
#Напишите функцию print_students(students, groups), которая принимает список строк из задания 7.12 и число групп, на которое необходимо поделить студентов.

#Используя генератор групп из задания 7.13 (генератор должен быть прописан внутри функции print_students), печатайте на экран:

#<Фамилия И.О., дд.мм.гггг> studies in group <номер группы по порядку>.

#Указание: используйте функцию zip() для одновременной работы с двумя итераторами.



def print_students(students, groups):
    # Вместо pass напишите тело функции
    def group_gen(n):
        i = 0
        while i < n:
            i += 1
            yield i
            if i == n:
                i = 0
    gr = group_gen(groups)       
    for student, gr in zip(students, gr):
        print(student, "studies in group", gr)
    

reg = ['Smith J., 13.02.2003', 'Petrova M.I., 13.03.2003']
print_students(reg, 3)
# Smith J., 13.02.2003 studies in group 1
# Petrova M.I., 13.03.2003 studies in group 2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///6.1.6/// Скинуть на проверку
/////////////
python_string = 'Hello! My name is Python. I will help you to analyze some data'
 
print(python_string[18:24])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///6.1.8/// Скинуть на проверку
/////////////
# Напишите свою функцию password_change, которая должна выводить на экран 
# отформатированную строку в следующем виде: 

# "User user_name changed password to new_password"

# Мы уже сделали заготовку функции вам осталось только задать строку
# Переменные, которые надо использовать, указаны в круглых скобках после имени функции
# user_name - имя пользователя, new_password - новый пароль
# запишите форматированную строку вместо знаков вопроса
# ! обязательное условие - задача должна быть решена с использованием метода format

def change_password(user_name, new_password):
    return ("User {} changed password to {}".format(user_name, new_password))

print(change_password("Lena", "qwerty"))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///6.2.5/// Скинуть на проверку
/////////////
# Напишите функцию get_unique_words(), которая избавляется от знаков препинаний 
# и пробелов в тексте и возвращает упорядоченный список 
# (слова расположены по алфавиту) из уникальных (неповторяющихся) слов.
def get_unique_words(text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    clear_text = list()
    for a in punctuation_list:
        text = text.replace(a,'')
    text = text.lower()
    clear_text = text.split()        
    clear_text = list(set(clear_text))
    clear_text.sort()
    return clear_text


# Текст, который можно использовать в качестве примера:
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
print(get_unique_words(text_example))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.6///
//////////
# Модифицируем предыдущую задачу.
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.
# Для решения можно использовать функцию из предыдущего задания.



#text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

text_example = "a b b c d d d f g h j k l m n o p  q r r r r r  r s t "

def get_most_frequent_word(text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    clear_text = list()
    for a in punctuation_list:
        text = text.replace(a,'')
    text = text.lower()
    clear_text = text.split()        
    
    schetchik = 1
    for i in range(len(clear_text)):
        if clear_text.count(clear_text[i]) > schetchik:
            schetchik = clear_text.count(clear_text[i])
            most_frequent_word = clear_text[i] 
    return most_frequent_word

print(get_most_frequent_word(text_example))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////
# Разработайте функцию holes_count(), которая подсчитывает количество отверстий 
# в заданном числе. Например, в цифре 8 два отверстия, в цифре 9 - одно. 
# В числе 146 - всего два отверстия. 
# Подсказка: используйте словарь для записи количества отверстий в цифрах

def holes_count(number):
    hole_in_num = {'0':1,'4':1,'6':1,'8':2,'9':1}
    str_num = str(number)
    hole = 0
    for i in range(len(str_num)):
        hole += hole_in_num.get(str_num[i],0)
            
    return hole


print(holes_count(123))
print(holes_count(8888))
print(holes_count(4688890))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.3.4///
//////////
# Напишите функция find_min_number(), которая принимает три числа на вход 
# и возвращает наименьшее из них.

# Используйте условия для решения задачи

def find_min_number(a, b, c):
    min = 0
    if a < b:
        min = a
    else:
        min = b
    if min > c:
        min = c
    
    return min

print(find_min_number(1, 2, 3))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.3.5///
//////////
# Напишите функция find_min_number(), которая принимает три числа на вход 
# и возвращает наименьшее из них.

# Используйте условия для решения задачи

def sum_min_numbers(a, b, c):
    min1 = 0
    min2 = 0
    if a < b:
        min1 = a
    else:
        min1 = b
    if b < c:
        min2 = b
    else:
        min2 = c
    
    return min1 + min2

print(sum_min_numbers(1, 2, 3))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.3.6///
//////////
# Напишите функцию is_divided_by_six(), которая проверяет, делится ли число на шесть. 
# При решении воспользуйтесь тернарным оператором!

# Функция должна вернуть True, если число делится на шесть или False в обратном случае.

# Подсказка: число делится на шесть, если оно делится на 2 и на 3

def is_divided_by_six(number):
    return True if number%6 == 0 else False

print(is_divided_by_six(13))
print(is_divided_by_six(12))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.3.7///
//////////
# Напишите функцию check_number_sign(), которая возвращает 1, если число положительное, 
# -1, если число отрицательное, 0, если число - 0.

# Используйте в коде конструкцию if-elif-else.

# Функция принимает на вход одно число.

def check_number_sign(x):
    otvet = 0
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


print(check_number_sign(0))
print(check_number_sign(100))
print(check_number_sign(-1))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.3.8///
//////////
# Напишите функцию def division(), которая осуществляет деление двух чисел. 
# Необходимо реализовать внутри функции отлов исключения ZeroDivisionError, 
# в случае, если пользователь, при вызове функции, пытается поделить на ноль.

# Функция принимает на вход два числа - делимое и делитель.

def division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        print("Delenie na nol'")
        

print(division(1, 0))
print(division(1, 1))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.4.4///
//////////
# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.

# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.

# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    st = 0
    fin = 0
    str_num = str(ticket_number)
    for i in range(3):
        st += int(str_num[i])
    for j in range(3):
        fin += int(str_num[-i])
    #print(st)
    #print(fin)
    if st == fin:
        return True
    else:
        return False     

print(lucky_ticket(111111))
print(lucky_ticket(123456))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.4.5///
//////////
# Числа Фибоначчи. 

# Напишите функцию def fib_number(), которая получается на вход некоторое 
# число n и выводит n-e число Фибоначчи. 
# Задачу можно решить как с помощью цикла for, так и с помощью цикла while

# Примечание: числа Фибоначчи определяются так


# ```
# a0 = 0, a1 = 1, a2 = a1 + a0 = 1, an = a_n-1 + a_n-2
# ```

# Примечание: в модуле по функциям уже было задание на вычисление чисел Фибоначчи 
# с помощью рекурсивных функций. Здесь необходимо реализовать те же вычисления, 
# но без использования рекурсии.

def fib_number(n):
    if n == 0:
        return 0
    an1 = 1
    an2 = 0
    for i in range(n):
        an = an2 + an1
        an1 = an2
        an2 = an
    return an
  
#for i in range(15):
#    print(fib_number(i),end=' ')
#print(fib_number(0))
#print(fib_number(1))
#print(fib_number(7))
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.4.6///
//////////
# Напишите функцию def even_numbers_in_matrix(), 
# которая получает на вход матрицу (список из списков) 
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    chetnye = 0
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] % 2 == 0:
                #print(matrix[i][j])
                chetnye += 1
    
    return chetnye

print(even_numbers_in_matrix(matrix_example))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.4.7///
//////////
# Напишите функцию def matrix_sum(), которая получает на вход две матрицы 
# и возвращает их сумму.

# Примечание: чтобы найти сумму двух матриц, нужно просуммировать 
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры 
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)

# Например:

# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

matrix_example1 = [
          [1, 2, 3],
          [2, 3, 4],
          [5, 6, 7]
]

matrix_example2 = [
          [2, 3, 4],
          [4, 5, 6],
          [4, 3, 2]
]

def matrix_sum(matrix1, matrix2):
    # проверяем размеры матриц - они должны совпадать!
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)): 
            for j in range(len(matrix1[0])): 
                matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
        return matrix1            
    #else:
        #raise ValueError("Matrix ne ravny!!!")
        
    
    

#print(matrix_sum(matrix_example1, matrix_example2))
#print(matrix_sum(matrix_example, matrix_example))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///8.9.1///
//////////
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

predict_number_ls = []

def random_predict(number: int = 50) -> int:
    """Рандомно задаем число и угадываем его по заданному алгоритму

    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    count = 0                   # Обнуляем число попыток
    global predict_number_ls    # Объявляем глобальный список рандомных чисел
    
    predict_number = np.random.randint(1, 101)  # Генерируем "загаданное" число
    predict_number_ls.append(predict_number)    # Добавляем заданное число в список
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
    i = 0
    while i < 1000:#random_array:        
        count_ls.append(random_predict())        
        i += 1  
        
    score = int(np.mean(count_ls)) 
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)

https://lms.skillfactory.ru/courses/course-v1:SkillFactory+DSPR-2.0+14JULY2021/courseware/adcad86c8b6c4e1299c49876a3024181/ad5803aeb7e64f6cad30e22ad68da714/6?activate_block_id=block-v1%3ASkillFactory%2BDSPR-2.0%2B14JULY2021%2Btype%40vertical%2Bblock%406fe30bb5230d4dc1b8f60193cce10060
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.3.2///
//////////
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)]
         
# Напечатайте словарь из температур, отсортированный по уменьшению температуры


#Словарь, который гарантирует сохранение порядка добавления ключей в нём
from collections import OrderedDict

years_temps = OrderedDict(sorted(temps, key=lambda x: x[1],reverse=True))

print(years_temps)


#Пример входа:
#temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

#Пример вывода:
#OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



//////////////////
///9.3.5-9.3.7///
////////////////
from hidden import users
# Пишите здесь команды, который помогут
# найти ответы на вопросы

from collections import deque
dec = deque(users)

#3.5
#Извлеките элемент из начала очереди. Запишите полученное значение элемента в качестве ответа.
print("3.5 :", dec.popleft())

#3.6
#В уже модифицированной очереди переместите пять элементов из начала очереди в её конец. 
#Извлеките последний элемент из очереди. Запишите полученное число в качестве ответа.
i = 0

while i < 5: 
    dec.append(dec.popleft())
    #print(i)
    i += 1
print(dec)
a = dec.pop()
print("3.6 :", a)


#3.7
#Сколько задач с тем номером, что был извлечён в предыдущем задании, 
#осталось в модифицированной очереди? Запишите ответ в числовой форме.
from collections import Counter

count = Counter(dec)
print("3.7 :", count[a])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



////////////
///9.4.3///
//////////
from collections import Counter

def brackets(line):
    # Напишите тело функции
    if line == '':
        return True
    elif line[0] == ')':
        return False
    elif line[-1] == '(':
        return False
    elif Counter(line)['('] != Counter(line)[')']:
        return False
    else:
        return True
        
print(brackets("()()())"))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//////////////////
///9.4.4-9.4.8///
////////////////
from hidden import north, center, south
from collections import Counter
# Пишите здесь команды, которые помогут
# найти ответы на вопросы

print(center)
print(south)
print(north)

flat_list1 = sum(center, [])
flat_list2 = sum(south, [])
flat_list3 = sum(north, [])


print('Transformed list', len(flat_list1))
print('Transformed list', len(flat_list2))
print('Transformed list', len(flat_list3))


center_counter = Counter(flat_list1)
print(center_counter)

south_counter = Counter(flat_list2)
print(south_counter)

north_counter = Counter(flat_list3)
print(north_counter)


print(center_counter+north_counter+south_counter)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



////////////
///9.4.9///
//////////
from collections import OrderedDict

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
         
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
print(ratings)

# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
cafes = OrderedDict(ratings)
#cafes_no_true = OrderedDict(sorted(ratings, key=lambda x: x[1]))
#print(cafes,'\n',cafes_no_true)
print(cafes)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



////////////
///9.4.10///
//////////
from collections import defaultdict
from collections import deque

def task_manager(tasks):
    tasks_of_servers = defaultdict(deque)

    for task, server, priority in tasks:
        if priority == True:
            tasks_of_servers[server].appendleft(task)
        else:
            tasks_of_servers[server].append(task)
    #print(tasks_of_servers)
    return tasks_of_servers


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

 
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})

'''
/У deque есть четыре ключевые метода:
- append (добавить элемент в конец дека);
- appendleft (добавить элемент в начало дека);
- pop (удалить и вернуть элемент из конца дека);
- popleft (удалить и вернуть элемент из начала дека).'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.7.2///
//////////
try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery

import numpy as np
'''
nd_arr = np.array([
               [12, 45, 78, 0, 2],
               [34, 56, 13, 0, 2],
               [12, 98, 76, 0, 2],
               [12, 98, 76, 0, 2]
               ])
 '''              
print(mystery, '\n')
# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]
print("elem_5_3 is", elem_5_3, '\n')

# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]
print("last is", last, '\n')

# В переменную line_4 сохраните строку 4
line_4 = mystery[3, :]
print("line_4 is", line_4, '\n')

# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:, -2]
print("col_2 is", col_2, '\n')

# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
# Результат сохраните в переменную part
part = mystery[1:4, 2:5]
print("part is", part, '\n')

#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[::-1, -1] 
#в первом индексе задаем ::-1 от начала до конца с шагом -1
print("rev is", rev, '\n')

# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()
print("trans is", trans, '\n')

'''
[[-13586  15203  28445 -27117  -1781 -17182 -18049]
 [ 25936 -30968  -1297  -4593   6451  15790   7181]
 [ 13348  28049  28655  -6012  21762  25397   8225]
 [ 13240   7994  32592  20149  13754  11795   -564]
 [-21725  -8681  30305  22260 -17918  12578  29943]
 [-16841 -25392 -17278  11740   5916    -47 -32037]] 
'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.7.4///
//////////
try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery
    
    
import numpy as np
print(mystery,'\n')


# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
print("nans_index is", nans_index, '\n')

# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)
print("n_nan is", n_nan, '\n')

# Заполните пропущенные значения в массиве mystery нулями
mystery[np.isnan(mystery)] = 0
print("mystery is", mystery, '\n')

# Поменяйте тип данных в массиве mystery на int32
print("mystery.dtype is",mystery.dtype,'\n')
mystery = np.int32(mystery)
print("mystery.dtype is",mystery.dtype,'\n')

# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)
print("array is",array,'\n')

# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3), order='F')
print("table is",table,'\n')

#  Сохраните в переменную col средний столбец из table
col = table[:,1]
print("col is",col,'\n')

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.8.4///
//////////
import numpy as np
from hidden import mystery
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы

#сумма длин сонаправленных векторов должна быть равной длине суммы двух векторов
a_norm = np.linalg.norm(a)
print(a_norm)
b_norm = np.linalg.norm(b)
print(b_norm)
c_norm = np.linalg.norm(c)
print(c_norm)

print(a_norm+b_norm)
print(a_norm+c_norm)
print(b_norm+c_norm)
a_b = np.linalg.norm(a+b)
print(a_b)
a_c = np.linalg.norm(a+c)
print(a_c)
b_c = np.linalg.norm(b+c)
print(b_c)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.8.5///
//////////
import numpy as np
from hidden import mystery
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы
print(np.linalg.norm(a-b))
print(np.linalg.norm(a-c))
print(np.linalg.norm(b-c))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///9.8.6///
//////////
import numpy as np
from hidden import mystery
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы

print(np.dot(a,b))
print(np.dot(a,c))
print(np.dot(b,c))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////////
///9.8.7-9.8.10///
/////////////////
from hidden import mystery
# Пишите здесь команды, который помогут
# найти ответы на вопросы

import numpy as np
9.8.7
print(mystery.min())
9.8.8
print(mystery.mean())
9.8.9
print(np.median(mystery))
9.8.10
print(np.std(mystery))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////////
///9.9.6///
//////////
# Не забудьте импортировать numpy и сразу задать seed 2021
import numpy as np
np.random.seed(2021)


# В simple сохранте случайное число в диапазоне от 0 до 1
simple = np.random.rand()
print("simple is ",simple,'\n')

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)
print("randoms is ",randoms,'\n')

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))
print("table is ",table,'\n')

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)
print("even is ",even,'\n')

# Перемешайте числа в так even, чтобы массив even изменился
np.random.shuffle(even)
print("even is ",even,'\n')

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, size=3, replace=False)
print("select is ",select,'\n')

# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
print("triplet is ",triplet,'\n')


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///9.10.5/// 
///////////
from hidden import a, b
# Пишите здесь команды, который помогут
# найти ответы на вопросы
import numpy as np

print(np.int64(a))
print(np.int64(b))
print(np.int64(a)+np.int64(b))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///9.10.6///
///////////
import numpy as np
def get_chess(a):
    # Напишите тело функции
    mass = np.zeros((a,a))
    mass[1::2, ::2] = 1
    mass[::2, 1::2] = 1
    return mass


print(get_chess(1))
# array([[0.]])
print(get_chess(4))
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///9.10.7///
///////////
import numpy as np
def shuffle_seed(array):
    # Напишите тело функции
    a = np.random.randint(0, 2**32)
    np.random.seed(a)
    mass = np.random.permutation(array)
    return (mass, a)




array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# (array([1, 3, 2, 4, 5]), 2332342819)
print(shuffle_seed(array))
# (array([4, 5, 2, 3, 1]), 4155165971)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///9.10.8///
///////////
import numpy as np
def min_max_dist(*vectors):
    
    # Напишите тело функции
    list1 = list()
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            list1.append(np.linalg.norm(vectors[i] - vectors[j]))
    min_dist = min(list1)
    max_dist = max(list1)
    
    return min_dist, max_dist


vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///9.10.9/// 
///////////
import numpy as np

def any_normal(*vectors):
    
    # Напишите тело функции
    list1 = list()
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if np.dot(vectors[i], vectors[j]) == 0:
                return True
    return False

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///9.10.10/// 
////////////
import numpy as np

def get_loto(num):
    
    # Напишите тело функции
    #bilets = 
    return np.random.randint(1, 101, size=(num,5,5))


print(get_loto(3))

'''
Результат:
array([[[ 35,  66,  38,  11,  32],
       [ 32,   7,  37,  83,  42],
       [ 89,  37,  19,  51,  89],
       [ 70, 100,  83,   5,  11],
       [ 20,  13,  60,  26,  41]],
 
      [[ 23,  49,  76,  44,  43],
       [ 59,  63,  99,  92,   2],
       [ 83,   4,  25,  73,  19],
       [ 10,  18,  40,  11,  21],
       [ 58,  45,  73,  93,  61]],
 
      [[100,  88,  70,  34,  51],
       [  5,  35,  36,  85,  88],
       [ 72,  23,  87,  30,  40],
       [ 29,  21,  51,  73,  81],
       [ 91,  19,  87,  60,  27]]])
'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///9.10.11/// 
////////////
import numpy as np

def get_unique_loto(num):
    
    # Напишите тело функции
    bilets_list = list()
    numbers = np.arange(1, 101)
	#Будем использовать цикл, для того, чтобы цифры не повторялись только в матрицах 5х5
	#Если задать без цикла, то цифры не смогут повторяться во всём массиве
	#и тогда мы не сможем сгенерировать 1000 лотарейных билетов
	
    for i in range(num):			
        bilets_list.append(np.random.choice(numbers, size=(5,5), replace=False))
    bilets = np.array(bilets_list)
    return bilets


print(get_unique_loto(3))


'''
Результат:
array([[[26, 91, 73,  7, 16],
       [46, 85, 78, 77, 51],
       [84, 86, 55, 71, 58],
       [17, 61, 50, 30, 97],
       [66, 29, 38, 41, 32]],
 
      [[49, 32,  3, 21, 85],
       [45,  8, 94, 46, 96],
       [41, 38, 58, 37, 98],
       [66, 77, 54, 80, 26],
       [62, 63, 72,  5, 43]],
 
      [[55, 60,  6, 80, 97],
       [23, 69, 94,  9, 24],
       [17, 98, 27, 63, 79],
       [84, 74, 51, 39, 54],
       [77, 30, 48, 75, 85]]])
'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.2.3///
///////////
import pandas as pd

def delete_columns(df, col=[]):
    """
    Напишите функцию delete_columns(df, col=[]), которая удаляет столбцы из DataFrame и возвращает новую таблицу. 
    Если одного из указанных столбцов в таблице не существует, то функция должна возвращать None.
    """
    for i in col:
        if i not in df.columns:
            return None
    return df.drop(col, axis=1)
    


if __name__ == '__main__':
    customer_df = pd.DataFrame({
        'number': [0, 1, 2, 3, 4],
        'cust_id': [128, 1201, 9832, 4392, 7472],
        'cust_age': [13, 21, 19, 21, 60],
        'cust_sale': [0, 0, 0.2, 0.15, 0.3],
        'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
        'cust_order': [1400, 14142, 900, 1240, 8430]
    })
    columns_for_delete= ['number','cust_age'] #выбранные вами столбцы
    new_df = delete_columns(customer_df, columns_for_delete)
    print(new_df)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.4.2///
///////////
import pandas as pd

melb_data = pd.read_csv('C:\Python\melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek

weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
print(weekend_count)

def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else: 
        return 0
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
print(round(melb_df[melb_df['Weekend']==1]['Price'].mean(), 2))

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.4.3///
///////////
import pandas as pd

melb_data = pd.read_csv('C:\Python\melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]

#print(melb_df['SellerG'])
SellerG = melb_df['SellerG']
    #nlargest(n) - возвращяет n самых популярных элементов
#print(SellerG.nunique())

popular_SellerG =SellerG.value_counts().nlargest(49).index
#print(popular_SellerG)

melb_df['popular_SellerG'] = SellerG.apply(lambda x: x if x in popular_SellerG else 'other')
print(melb_df['popular_SellerG'].nunique())


a = melb_df[melb_df['popular_SellerG'] == 'Nelson']['Price'].min() 
b = melb_df[melb_df['popular_SellerG'] == 'other']['Price'].min()
print(round(a/b, 1))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.4.4///
///////////
import pandas as pd

def get_experience(arg):
    """
    Напишите функцию get_experience(arg), аргументом которой является строка столбца с опытом работы. 
    Функция должна возвращать опыт работы в месяцах. Не забудьте привести результат к целому числу.
    """
    year_list = ['лет','года','год']
    month_list = ['месяца','месяцев','месяц']
    arg_list = arg.split(' ')
    month,year = 0, 0
    for i in range(len(arg_list)):
        if arg_list[i] in month_list:
            month = arg_list[i-1]
        if arg_list[i] in year_list:
            year = arg_list[i-1]
    return int(year)*12+int(month)


if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
    print(experience_month)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///11.5.2///
//////////
import pandas as pd

melb_data = pd.read_csv('C:\Python\melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()

#print(melb_df.info())
#2.4 Mb
#print(melb_df['Suburb'].nlargest(119).index)

Suburb = melb_df['Suburb']
#print(Suburb)
popular_Suburb =Suburb.value_counts().nlargest(119).index
#print(popular_Suburb)
melb_df['Suburb'] = Suburb.apply(lambda x: x if x in popular_Suburb else 'other')
print(melb_df['Suburb'].nunique())

melb_df['Suburb'] = melb_df['Suburb'].astype('category')
print(melb_df.info())
#2.3 Mb
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.6.9///
///////////
import pandas as pd

citybike_data = pd.read_csv('C:\Python\citibike-tripdata.csv', sep=',')

citybike_df = citybike_data.copy()

#print(citybike_df.info())
#print(citybike_df['end station name'].mode())
#print(citybike_df['start station id'].value_counts())
#print(citybike_df['start station name'].value_counts())
citybike_df['age'] = 2018-citybike_df['birth year']
citybike_df = citybike_df.drop(['birth year'], axis=1)
#print(citybike_df['age'].max())
print(citybike_df[citybike_df['age']>60]['age'].shape)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////
///11.6.10///
///////////
import pandas as pd

citybike_data = pd.read_csv('C:\Python\citibike-tripdata.csv', sep=',')

citybike_df = citybike_data.copy()

#print(citybike_df.head())
#print(citybike_df.info())

citybike_df['starttime'] = pd.to_datetime(citybike_df['starttime'])
citybike_df['stoptime'] = pd.to_datetime(citybike_df['stoptime'])
citybike_df['trip duration'] = (citybike_df['stoptime'] - citybike_df['starttime']).dt.seconds
print(citybike_df['trip duration'].mean())
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///11.6.11///
////////////
import pandas as pd

citybike_data = pd.read_csv('C:\Python\citibike-tripdata.csv', sep=',')

citybike_df = citybike_data.copy()

#print(citybike_df.head())
#print(citybike_df.info())

citybike_df['starttime'] = pd.to_datetime(citybike_df['starttime'])
weekday = citybike_df['starttime'].dt.dayofweek
citybike_df['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
print(citybike_df['weekend'].sum())
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








//////////////
///11.6.12///
////////////
import pandas as pd

def time_of_day(times):
    if 0<=times<=6:
        return 'night'
    elif 6<times<=12:
        return 'morning'
    elif 12<times<=18:
        return 'day'
    else:
        return 'evening' 

citybike_data = pd.read_csv('C:\Python\citibike-tripdata.csv', sep=',')

citybike_df = citybike_data.copy()

#print(citybike_df.head())
#print(citybike_df.info())

citybike_df['starttime'] = pd.to_datetime(citybike_df['starttime'])

time_day = citybike_df['starttime'].dt.hour
citybike_df['time_of_day'] = time_day.apply(time_of_day)
print(citybike_df['time_of_day'].value_counts())
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///12.2.2///
//////////
import pandas as pd


melb_data = pd.read_csv('C:\Python\melb_data_fe.csv', sep=',')

melb_df = melb_data.copy()

#print(melb_df.head())
#print(melb_df.info())

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
#print(melb_df.info())

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца
#print(melb_df.info())

print(melb_df.sort_values(
    by='AreaRatio', 
    ascending = False, 
    ignore_index = True
    ).loc[1558, 'BuildingArea'])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///12.2.3///
//////////
import pandas as pd


melb_data = pd.read_csv('C:\Python\melb_data_fe.csv', sep=',')

melb_df = melb_data.copy()

#print(melb_df.head())
#print(melb_df.info())

mask1 = melb_df['Rooms'] > 2
mask2 = melb_df['Type'] == 'townhouse'

#print(melb_df.iloc[2])
print(
(melb_df[mask1 & mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True,
    
)['Price'].iloc[18])
)

#print(melb_df['Price'].head(20))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///12.3.1-12.3.2///
//////////
import pandas as pd

melb_data = pd.read_csv('C:\Python\melb_data_fe.csv', sep=',')
melb_df = melb_data.copy()
#print(melb_df.head())
#print(melb_df.info())

3.1
print(
    melb_df.groupby(by='Rooms')['Lattitude'].mean().max()
    )

3.2
print(
    melb_df.groupby(by='Regionname')['Lattitude'].std().sort_values()
    )

3.3
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
melb_df['Date'] = to_datetime(melb_df['Date'])
mask1 = (date1 <= melb_df['Date']) & (melb_df['Date'] <= date2)
print(
    melb_df[mask1].groupby(by='SellerG')['Price'].sum().sort_values()
    )


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////////////
///12.4.2-12.4.3///4.2 - проебал
//////////////////
import pandas as pd
from pandas.core.tools.datetimes import to_datetime

melb_data = pd.read_csv('C:\Python\melb_data_fe.csv', sep=',')
melb_df = melb_data.copy()

print(
    melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='median',
    fill_value=0
)['unit']
)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///12.7.5///
//////////
import pandas as pd

items_df = pd.DataFrame({
'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
})

purchase_df = pd.DataFrame({
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
})

#print(items_df)
#print(purchase_df)

"""
Сформируйте DataFrame merged, в котором в результате объединения
purchase_df и items_df останутся модели, которые учтены на складе и имели продажи. 
"""
merged = purchase_df.merge(
    items_df,
    on='item_id',
    how='inner'
)
#print(merged)


"""
Найдите из таблицы merged суммарную выручку, которую можно было бы получить 
от продажи всех товаров, которые есть на складе. 
Результат занесите в переменную income.
"""
merged['total'] = merged['price'] * merged['stock_count']
income = merged['total'].sum()
#print(merged)
#print(income)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////////////
///12.8.1-12.8.7///
//////////////////
import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import re 

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None


rating_movies_data = pd.read_csv('C:/Python/ratings_movies/ratings_movies.csv', sep=',')

ratings_df = rating_movies_data.copy()
#print(ratings_df)

#12.8.1
ratings_df['year_release'] = ratings_df['title'].apply(get_year_release)
#print(ratings_df.info())

#12.8.2
for_1999 = ratings_df[(ratings_df['year_release'] == 1999)]
ratings_1999 = for_1999.groupby(['title'])['rating'].mean()
#print(ratings_1999.sort_values())

#12.8.3
for_2010 = ratings_df[(ratings_df['year_release'] == 2010)]
ratings_2010 = for_2010.groupby(['genres'])['rating'].mean()
#print(ratings_2010.sort_values())

#12.8.4
user_fan = ratings_df.groupby('userId')['genres'].nunique().sort_values()
#print(user_fan)

#12.8.5
#print(
#    ratings_df.groupby('userId')['rating'].agg(
#        ['count', 'mean']
#    ).sort_values(['count', 'mean'], ascending=[True, False])
#)

#12.8.6
mask = ratings_df['year_release'] == 2018
grouped = ratings_df[mask].groupby('genres')['rating'].agg(
    ['mean', 'count']
)
#print(
#    grouped[grouped['count']>10].sort_values(
#        by=['mean', 'count'],
#        ascending=[False, False]
#    )
#)

#12.8.7
ratings_df['date'] = pd.to_datetime(ratings_df['date'])
ratings_df['year_rating'] = ratings_df['date'].dt.year
pivot = ratings_df.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)
print(pivot['Comedy'])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








/////////////////////
///12.8.8-12.8.10///
///////////////////
from numpy import left_shift
import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import re 

orders_data = pd.read_csv('C:/Python/orders_and_products/orders.csv', sep=';')
products_data = pd.read_csv('C:/Python/orders_and_products/products.csv', sep=';')

orders_df = orders_data.copy()
products_df = products_data.copy()
#print(orders_df)
#print(products_df)

orders_product = orders_df.merge(
    products_df,
    left_on='ID товара',
    right_on='Product_ID',
    how='left'
)
#print(orders_product.sort_values(by='Дата создания'))
#print(orders_product[orders_product['Отменен']=='Да']['ID Покупателя'])
#print(orders_product.sort_values(by='ID Покупателя'))

for i in range(orders_product['ID Покупателя'].max()):
    clients_df = orders_product[orders_product['ID Покупателя'] == i]['Price'].sum()
    print(i,' by on ',clients_df)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///14.4.6///
//////////
import pandas as pd

"""
Ваша задача очистить данную таблицу от пропусков следующим образом:
- Если признак имеет больше 50% пропущенных значений - удалите его
- Если в строке 3 и более пропусков - удалите строку
- Для оставшихся данных: числовые признаки заполните средним значением, а категориальные - модой
"""
df = pd.read_csv('./Root/data/test_data.csv')

#print(df.head(10))

#задаем минимальный порог: вычисляем 50% от числа строк
thresh = df.shape[0]*0.5
#удаляем столбцы, в которых 50% пропусков
df = df.dropna(how='any', thresh=thresh, axis=1)

#print(df.head(10))

#удаляем записи, в которых есть 3 и более пропусков
df = df.dropna(thresh=2, axis=0)

#отображаем результирующую долю пропусков
#print(df.head(10))


df = df.fillna({
    'one' : df['one'].mean(),
    'two' : df['two'].mean(),
    'three' : df['three'].mean(),
    'four' : 'bar'#df['four'].mode() почему-то не работало
}) 

print(df.head(10))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///14.6.4.1///
//////////
import pandas as pd

def outliers_iqr_mod(data, feature):
    """
    Давайте немного модифицируем нашу функцию outliers_iqr(). 
    Добавьте в нее параметры left и right, которые задают число IQR влево и вправо от границ ящика (пусть по умолчанию они равны 1.5).
    Функция, как и раньше должна возвращать потенциальные выбросы и очищенный DataFrame.
    """
    x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    left = 1.5
    right = 1.5
    iqr = quartile_3 - quartile_1
    upper_bound = quartile_3 + (iqr * left)
    lower_bound = quartile_1 - (iqr * right) 
    
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned

    
sber_data = pd.read_csv('./Root/data/test_sber_data.csv')

outliers, cleaned = outliers_iqr_mod(sber_data, 'full_sq')

print('Vibrosi: ',outliers.shape[0])
print('Itogo zapisei: ',cleaned.shape[0])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///14.6.4.3///
//////////
import pandas as pd
import numpy as np

def outliers_z_score_mod(data, feature, log_scale=False, left=3, right=3):
    """
    Давайте расширим правило 3ех сигм, чтобы иметь возможность учитывать ассиметричность данных.
    Добавьте в функцию outliers_z_score() параметры left и right, которые будут задавать число сигм (стандартных отклонений) 
    влево и вправо соответственно, которые определяют границы метода z-отклонения. 
    По умолчанию оба параметры равны 3
    """
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]
    mu = x.mean()                   #Вычислим математическое ожидание (среднее)
    sigma = x.std()                 #Вычислим стандартное отклонение для признака x
    lower_bound = mu - left * sigma    #Вычислим нижнюю границу интервала
    upper_bound = mu + right * sigma    #Вычислим верхнюю границу интервала
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

sber_data = pd.read_csv('./Root/data/test_sber_data.csv')

outliers, cleaned = outliers_z_score_mod(sber_data, 'mkad_km', log_scale=True, left=3, right=3.5)

print('Vibrosi: ',outliers.shape[0])
print('Itogo zapisei: ',cleaned.shape[0])
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///15.5.1///
//////////
class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
        self.dict = {email:password,}
        
    def login(self, email, password):
        if self.dict[email] == password:
            #print(self.dict[email], 'and', password)
            return True
        else:
            #print(self.dict[email], 'and', password)
            return False
    def update_balance(self, count):        
        self.balance += count
        return self.balance
            
            
user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")
# => False
user.login("gosha@roskino.org", "qwerty")
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///15.6.3///
//////////
class Dog():  
    def bark(self):
        return "Bark!"
    def give_paw(self):
        return "Paw"
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////////
///Аттестация 1///
/////////////////
def apply_discounts(products, stocks):
    """
    Напишите функцию apply_discounts(), которая снижает цену продуктов в словаре products на указанный в словаре stocks процент. 
    Функция должна вернуть результирующий словарь, ключи которого — товары, а значения — новые цены.
    Если продукта из словаря stocks нет в словаре products, то его необходимо пропустить. Цены округлите до второго знака после запятой.
    """
    for s in stocks.keys():
        stocks2[s] = round((1-(float(stocks[s].replace('%','')/100)),2))
    new_products = dict()
    for i in products.keys():
        
        if i not in stocks2.keys():
            new_products[i] = products[i]
        else:
            new_products[i] = round((products[i] * stocks2[i]),2)
    return new_products
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////////
///Аттестация 2///
/////////////////
import pandas as pd

bronze_path = './Root/data/bronze_top.csv'
silver_path = './Root/data/silver_top.csv'
"""
Объедините две таблицы по странам таким образом, чтобы в результат вошли данные только о тех странах, которые есть в обоих рейтингах. 
При этом в качестве суффиксов для столбца c числом медалей укажите строки "_bronze" и "_silver", чтобы столбцы можно было различать.
Результат занесите в переменную merged.
"""
bronze_df = pd.read_csv(bronze_path, sep=',')
silver_df = pd.read_csv(silver_path, sep=',')

merged = bronze_df.merge(
    silver_df,
    on='Country',
    how='inner',
    suffixes=('_bronze','_silver')
    )

print(merged)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.3.3///
/////////////
SELECT 
    m.id,
    h.short_name as home_short,
    a.short_name as away_short
    
FROM
    sql.matches m
    JOIN sql.teams h ON m.home_team_api_id = h.api_id
    JOIN sql.teams a ON m.away_team_api_id = a.api_id
    
ORDER BY id ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.4.1///
/////////////
SELECT 
    t.long_name,
    m.home_team_goals as home_goal,
    m.away_team_goals as away_goal
   
    
FROM
    sql.matches m
JOIN sql.teams t ON m.home_team_api_id = t.api_id
WHERE 
    t.short_name = 'GEN'
ORDER BY m.id ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.4.2///
/////////////
SELECT 
    m.id,
    h.short_name as home_short,
    a.short_name as away_short
    
FROM
    sql.matches m
    JOIN sql.teams h ON m.home_team_api_id = h.api_id
    JOIN sql.teams a ON m.away_team_api_id = a.api_id
    
WHERE
    (h.long_name = 'Liverpool' OR a.long_name = 'Liverpool')
    AND 
    m.season = '2011/2012'

ORDER BY id ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.4.3///
/////////////
SELECT
    t.long_name    
FROM sql.matches m
JOIN sql.teams t ON t.api_id = m.away_team_api_id
GROUP BY t.id
HAVING COUNT(*) >= 150
ORDER BY t.long_name ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.5.1///
/////////////
SELECT
  DISTINCT t.long_name
FROM
  sql.teams t
LEFT JOIN sql.matches m ON t.api_id = m.home_team_api_id or t.api_id = m.away_team_api_id
WHERE m.id is not null
ORDER BY t.long_name ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.5.2///
/////////////
SELECT
    t.long_name,
    COUNT(m.id) as matches_cnt
FROM sql.teams as t
LEFT JOIN sql.matches as m ON t.api_id = m.away_team_api_id OR t.api_id = m.home_team_api_id
GROUP BY t.id
ORDER BY matches_cnt ASC, t.long_name ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.5.2///
/////////////
SELECT
    DISTINCT
    t1.short_name as home_team, 
    t2.short_name as away_team
FROM
    sql.teams t1
    CROSS JOIN sql.teams t2
ORDER BY 1, 2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.6.1///
/////////////
/*Напишите запрос, который выведет список уникальных полных названий команд (long_name), игравших в гостях в матчах сезона 2012/2013.
Отсортируйте список в алфавитном порядке.*/

SELECT
    DISTINCT
    a.long_name as long_name
FROM
    sql.teams as a
    INNER JOIN sql.matches as m ON m.away_team_api_id = a.api_id
WHERE
    m.season = '2012/2013'
ORDER BY long_name ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.6.2///
/////////////
/*Напишите запрос, который выведет полное название команды (long_name) и общее количество матчей (matches_cnt), сыгранных c командой Inter в домашних матчах.*/

SELECT
    DISTINCT
    a.long_name as long_name,
    COUNT(*) as matches_cnt
FROM
    sql.matches as m
    JOIN sql.teams as h ON m.home_team_api_id = h.api_id
    JOIN sql.teams as a ON m.away_team_api_id = a.api_id

WHERE
    h.long_name = 'Inter'
    
GROUP BY a.id
ORDER BY long_name ASC
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.6.3///
/////////////
/*Напишите запрос, который выведет ТОП-10 команд (long_name) по суммарному количеству забитых голов в гостевых матчах. 
Во втором столбце запроса выведите суммарное количество голов в гостевых матчах (total_goals).*/

SELECT 
    a.long_name as long_name,
    SUM(away_team_goals) as total_goals
FROM
    sql.teams as a
    JOIN sql.matches as m ON m.away_team_api_id = a.api_id

GROUP BY a.id
ORDER BY total_goals DESC
LIMIT 10
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.6.4///
/////////////
/*Выведите количество матчей между командами Real Madrid CF и FC Barcelona.
В поле ниже введите запрос, с помощью которого вы решили задание.*/

SELECT
    --a.long_name as long_name_a,
    --h.long_name as long_name_h,
    COUNT(*) as total_goals
FROM
    sql.matches as m
    JOIN sql.teams as a ON m.away_team_api_id = a.api_id
    JOIN sql.teams as h ON m.home_team_api_id = h.api_id
WHERE (h.long_name = 'Real Madrid CF' AND a.long_name = 'FC Barcelona')
        OR
      (a.long_name = 'Real Madrid CF' AND h.long_name = 'FC Barcelona') 
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL3.6.5///
/////////////
/*Напишите запрос, который выведет название команды (long_name), сезон (season) и суммарное количество забитых голов в домашних матчах (total_goals).
Оставьте только те строки, в которых суммарное количество голов менее десяти.
Отсортируйте запрос по названию команды, а затем — по сезону.*/

SELECT 
    h.long_name as long_name,
    m.season as season,
    SUM(m.home_team_goals) as total_goals
FROM
    sql.teams as h
    JOIN sql.matches as m ON m.home_team_api_id = h.api_id

GROUP BY long_name, season
HAVING SUM(m.home_team_goals) < 10
ORDER BY long_name, season

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.2.1///
/////////////
/*Напишите запрос, который создаёт уникальный алфавитный справочник всех городов, штатов, имён водителей и производителей грузовиков.
Результатом запроса должны быть два столбца: название и тип объекта (city, state, driver, truck).
Отсортируйте список по названию объекта, а затем — по типу.*/
SELECT
         c.city_name AS "название", 
         'city' AS "тип объекта"
FROM 
         sql.city AS c

UNION

SELECT
         c.state, 
         'state'
FROM 
         sql.city AS c

UNION

SELECT
        d.first_name, 
        'driver'
FROM 
        sql.driver AS d

UNION

SELECT
        t.make, 
        'truck'
FROM 
        sql.truck AS t
        
ORDER BY 1,2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.2.2///
/////////////
/*Напишите запрос, который соберёт имена всех упомянутых городов и штатов с таблицы city.
Результатом запроса должен быть один столбец object_name, отсортированный в алфавитном порядке.*/
SELECT
         c.city_name AS object_name         
FROM 
         sql.city AS c

UNION ALL

SELECT
         c.state
FROM 
         sql.city AS c
ORDER BY object_name
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.2.3///
/////////////
/*Выполнив предыдущий запрос, мы получили города с одинаковыми названиями, но находящиеся в разных штатах, а также большое количество дублирующихся названий штатов.
Перепишите предыдущий запрос так, чтобы остались только уникальные названия городов и штатов.
Результатом запроса должен быть один столбец object_name, отсортированный в алфавитном порядке.*/
SELECT 
        c.city_name AS object_name
FROM 
        sql.city AS c

UNION

SELECT 
        c.state
FROM 
        sql.city AS c
ORDER BY object_name
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.3.1///
/////////////
/*Напишите запрос, который объединит в себе все почтовые индексы водителей и их телефоны в единый столбец-справочник. 
Также добавьте столбец с именем водителя и столбец с типом контакта (phone или zip в зависимости от типа). 
Столбцы к выводу: contact, first_name, contact_type.
Отсортируйте список по столбцу с контактными данными в порядке возрастания, а затем — по имени водителя.*/


/*city, customer, driver, shipment, truck*/
SELECT 
    zip_code::text AS contact,
    first_name,
    'zip' AS object_type
from sql.driver

UNION all

SELECT 
    phone::text,
    first_name,
    'phone'
from sql.driver

ORDER BY contact, first_name
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.4.1///
/////////////
/*Напишите запрос, который выводит общее число доставок total_shipments, а также количество доставок в каждый день. 
Необходимые столбцы: date_period, cnt_shipping.
Не забывайте о единой типизации.
Упорядочьте по убыванию столбца date_period.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    s.ship_date::text AS date_period,
    COUNT(*) AS cnt_shipment
    
FROM sql.shipment AS s
GROUP BY date_period

UNION ALL

SELECT 
    'total_shipment',
    COUNT(*)
from sql.shipment

ORDER BY date_period DESC

/*
SELECT s.ship_date::text date_period, COUNT(*) cnt_shipment
FROM sql.shipment s 
GROUP BY 1
UNION ALL
SELECT 'total_shipments', COUNT(*)
FROM sql.shipment s
ORDER BY 1 desc
*/
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.5.1///
/////////////
/*Напишите запрос, который выведет все города и штаты, в которых они расположены, а также информацию о том, была ли осуществлена доставка в этот город:

        если в город была осуществлена доставка, то выводим 'доставка осуществлялась';
        если нет — выводим 'доставка не осуществлялась'.
Столбцы к выводу: city_name, state, shipping_status.

Отсортируйте в алфавитном порядке по городу, а затем — по штату.*/


/*city, customer, driver, shipment, truck*/
SELECT
    c.city_name as city_name,
    c.state as state,
    'доставка осуществлялась' as shipping_status
    
FROM sql.city AS c
JOIN sql.shipment AS s ON s.city_id = c.city_id
WHERE s.city_id IS NOT NULL

UNION

SELECT
    c.city_name as city_name,
    c.state as state,
    'доставка не осуществлялась' as shipping_status
    
FROM sql.city AS c
LEFT JOIN sql.shipment AS s ON s.city_id = c.city_id
WHERE s.city_id IS NULL

ORDER BY city_name, state
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.5.2///
/////////////
/*Напишите запрос, который выводит два столбца: city_name и shippings_fake. Выведите города, куда совершались доставки.

Пусть первый столбец содержит название города, а второй формируется так:

если в городе было более десяти доставок, вывести количество доставок в этот город как есть;
иначе — вывести количество доставок, увеличенное на пять.
Отсортируйте по убыванию получившегося «нечестного» количества доставок, а затем — по имени в алфавитном порядке.*/


/*city, customer, driver, shipment, truck*/
SELECT
    c.city_name as city_name,
    COUNT(s.city_id) as shippings_fake
    
FROM sql.city AS c
JOIN sql.shipment AS s ON s.city_id = c.city_id
GROUP BY city_name
HAVING COUNT(s.city_id) > 10

UNION

SELECT
    c.city_name,
    (COUNT(s.city_id)+5)
    
FROM sql.city AS c
JOIN sql.shipment AS s ON s.city_id = c.city_id
GROUP BY city_name
HAVING COUNT(s.city_id) <= 10

ORDER BY shippings_fake DESC, city_name
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.6.1///
/////////////
/*Напишите запрос, который выберет наибольшее из значений:

1000000;
541;
-500;
100.*/

SELECT  1000000
UNION ALL
SELECT  541
UNION ALL
SELECT  -500
UNION ALL
SELECT  100
ORDER BY 1 DESC 
LIMIT 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.6.2///
/////////////
/*Мы помним, что сортировка для числовых и строковых типов данных отличается.

Построив запрос по аналогии с примером, приведите значения к текстовому типу данных, сравните и выберите наибольшее из них:

1000000;
541;
-500;
100.*/

SELECT  
    '1000000'
    
UNION ALL

SELECT  
    '541'
    
UNION ALL

SELECT  
    '-500'
    
UNION ALL

SELECT  
    '100'
ORDER BY 1 DESC 
LIMIT 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.6.3///
/////////////
/*Построив запрос по аналогии с примером, найдите самое большое значение из перечисленных операторов:

+ ;
- ;
= ;
/ .*/

SELECT  
    '+'
    
UNION ALL

SELECT  
    '-'
    
UNION ALL

SELECT  
    '='
    
UNION ALL

SELECT  
    '/'
ORDER BY 1 DESC 
LIMIT 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.7.1///
/////////////
/*Выведите список zip-кодов, которые есть в таблице sql.driver, но отсутствуют в таблице sql.customer. 
Отсортируйте по возрастанию, столбец к выводу — zip.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    zip_code
FROM sql.driver AS d

EXCEPT

SELECT 
    zip
FROM sql.customer AS cs

ORDER BY 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.8.1///
/////////////
/*Напишите запрос, который выведет список id городов, в которых есть и клиенты, и доставки, и водители.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    cs.city_id
FROM sql.customer AS cs

INTERSECT

SELECT 
    s.city_id
FROM sql.shipment AS s

INTERSECT

SELECT 
    d.city_id
FROM sql.driver AS d
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.8.2///
/////////////
/*Выведите zip-код, который есть как в таблице с клиентами, так и в таблице с водителями.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    zip_code
FROM sql.driver AS d

INTERSECT

SELECT 
    zip
FROM sql.customer AS cs
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.9.1///
/////////////
/*Выведите города с максимальным и минимальным весом единичной доставки.
Столбцы к выводу — city_name, weight.*/

/*city, customer, driver, shipment, truck*/
(SELECT 
    c.city_name,
    s.weight
FROM sql.shipment AS s
JOIN sql.city as c ON c.city_id = s.city_id
ORDER BY 2 DESC
LIMIT 1)

UNION

(SELECT 
    c.city_name,
    s.weight
FROM sql.shipment AS s
JOIN sql.city as c ON c.city_id = s.city_id
ORDER BY 2
LIMIT 1)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.9.2///
/////////////
/*Выведите идентификационные номера клиентов (cust_id), которые совпадают с идентификационными номерами доставок (ship_id).
Столбец к выводу — mutual_id.
Отсортируйте по возрастанию.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    cs.cust_id AS mutual_id
FROM sql.customer AS cs

INTERSECT

SELECT 
    s.ship_id
FROM sql.shipment AS s
ORDER BY 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL4.9.3///
/////////////
/*Создайте справочник, содержащий уникальные имена клиентов, которые являются производителями (cust_type='manufacturer'), и производителей грузовиков, а также описание объекта — 'КЛИЕНТ' или 'ГРУЗОВИК'.
Столбцы к выводу — object_name, object_description.
Отсортируйте по названию в алфавитном порядке.*/

/*city, customer, driver, shipment, truck*/
SELECT 
    cust_name AS object_name,
    'КЛИЕНТ' AS object_description
FROM sql.customer
WHERE cust_type='manufacturer'

UNION

SELECT 
    make AS object_name,
    'ГРУЗОВИК' AS object_description
FROM sql.truck

ORDER BY 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL5.3.1///
/////////////
/*Давайте узнаем, сколько сейчас времени в другом регионе, например в Лос-Анджелесе.

Напишите запрос, который выведет текущие время и дату в часовом поясе Лос-Анджелеса ("America/Los_Angeles").
Столбец в выдаче — now (время и дата в нужном часовом поясе).*/
SELECT now() at time zone 'America/Los_Angeles' AS now
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








///////////////
///SQL5.3.2///
/////////////
/*Предположим, у нас есть дата и время какого-то события и мы хотим посмотреть, к какой дате оно относится для Москвы и для UTC.
Используйте подзапрос
with x as 
(
select '2018-12-31 21:00:00+00'::timestamp with time zone ts
)
и выведите дату в ts в Московском часовом поясе и в поясе UTC.
Столбцы в выдаче: dt_msk (дата в московском часовом поясе), dt_utc (дата в UTC).*/

WITH x AS 
(
SELECT '2018-12-31 21:00:00+00'::timestamp WITH time zone AS ts
)
SELECT 
        (ts at time zone 'Europe/Moscow')::date dt_msk,
        (ts)::date dt_utc
FROM x
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








////////////
///6.2.7///
//////////






















































































































































































































































































































































































































































































































































































