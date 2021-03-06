# Проект 3. Оформить

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
В данном проекте были проанализированны вакансии размещенные на площадке hh.ru.
Код программы лежит в файле Project_1.ipynb

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Какой кейс решаем?    
Нужно проанализиорвать собранную о вакансиях информацию, переработать таблицу для выделения ключевой информации, изучить графики зависимостей и распределения основных параметров и произвести очистку данных для корректного построения будующей модели. 

**Метрика качества**     
Результаты оцениваются по логичности построенных графиков, а также признакам найденных выбросов.

**Что практикуем**     
Учимся работать с DataFrame, преобразовывать данные, выделяя необходимые признаки, исследовать DataFrame по графикам и производить очистку данных.


### Краткая информация о данных
Данные содержат в себе информацию о поле, возрасте, городе, уровне образования, желаемой зарплате, готовности к переездам и командировкаи, а также информацию о желаемых режимах работы соискателей.

Файл с исходными данными лежит по адресу https://drive.google.com/file/d/1Kb78mAWYKcYlellTGhIjPI-bCcKbGuTn/view.
При чтении использовать ';' как разделитель.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
- Исследование структуры данных.
- Преобразование данных.
- Исследование зависимостей.
- Очистка данных.


:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
В результате были удалены ненужные признаки с выделением из них интересующей информации о соискателях. Проанализированны зависимости и произведена очистка от пропусков и выбросов в данных.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
В ходе проделанной работы я понял алгоритм обработки данных для будующего построения моделей на их основе.

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами


hotel_address — адрес отеля;
review_date — дата, когда рецензент разместил соответствующий отзыв;
average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
hotel_name — название отеля;
reviewer_nationality — страна рецензента;
negative_review — отрицательный отзыв, который рецензент дал отелю;
review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
positive_review — положительный отзыв, который рецензент дал отелю;
review_total_positive_word_counts — общее количество слов в положительном отзыве.
reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
total_number_of_reviews — общее количество действительных отзывов об отеле;
tags — теги, которые рецензент дал отелю;
days_since_review — количество дней между датой проверки и датой очистки;
additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
lat — географическая широта отеля;
lng — географическая долгота отеля.