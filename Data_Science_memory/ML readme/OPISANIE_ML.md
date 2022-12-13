# СОДЕРЖАНИЕ

Образец запроса с описательной информацией
``` python
from sklearn.mixture import GaussianMixture
help(GaussianMixture)
```

## ***РАЗДЕЛЕНИЕ ВЫБОРОК И ВАЛИДАЦИЯ***
* Деление на 3 набора:
    * Тренировочный X_train, y_train (70-80%)
    * Валидационный X_valid, y_valid (10-15%)
    * Тестовый      X_test,  y_test  (10-15%)

* ### HOLD-OUT - "ОТЛОЖЕННАЯ ВЫБОРКА" 
    * Очень простой и понятный
    * Чаще всего применяется на больших датасетов, так как менне ресурсный
    * Можно улучшить стратификацией `stratify=y`
    ``` python
    from sklearn.model_selection import train_test_split
    #разбиваем исходную выборку на тренировочную и валидационную в соотношении 80/20
    X_train, X_valid, y_train, y_valid = model_selection.train_test_split(X, y, test_size=0.2)
    #разбиваем валидационную выборку на валидационную и тестовую в соотношении 50/50
    X_valid, X_test, y_valid, y_test = model_selection.train_test_split(X_valid, y_valid, test_size=0.5)
    ```

* ### K-FOLD - "КРОСС-ВАЛИДАЦИЯ ИЛИ ПЕРЕКРЁСТНЫЙ КОНТРОЛЬ"
    * Исходые данные разбивают на k-фолдов (частей) с отделением тестовых данных
    * Циклично итерируют фолды, при этом один из них по очереди является валидационным
    * Получаем более точный модели, менее чувствительные к выбросам
    * Более ресурсный и медленный, так как число итераций зависит от числа фолдов
    * Если количество фолдов больше 30, можно построить доверительный интервал для среднего значения метрики
    ``` python
    from sklearn import model_selection
    kf = model_selection.KFold() # Обычное разбиение
    skf = model_selection.StratifiedKFold() # Стратифицированное разбиение
    #Считаем метрики на кросс-валидации k-fold
    cv_metrics = model_selection.cross_validate()
    print('Train k-fold mean accuracy: {:.2f}'.format(np.mean(cv_metrics['train_score'])))
    ```

* ### LIVE-ONE-OUT - "ОТЛОЖЕННЫЙ ПРИМЕР ИЛИ ПОЭЛЕМЕНТНАЯ КРОСС-ВАЛИДАЦИЯ"
    * Алгоритм:
        * Повторять n раз:
            * Выбрать один случайный пример для валидации
            * Обучить модель на всех оставшихся  примерах
            * Произвести оценку качества (вычислить метрику) на отложенном примере
        * Усреднить значение метрик на всех примерах
    * Имеет наиболее объективные и надёжные метрики
    * Идеален для небольших данных (порядка 100)
    * Очень ресурсозатратный
    ``` python
    from sklearn import model_selection
    loo = model_selection.LeaveOneOut()
    cv_metrics = model_selection.cross_validate()
    print('Train k-fold mean accuracy: {:.2f}'.format(np.mean(cv_metrics['train_score'])))
    ```
    * Примечание. Метод leave-one-out можно реализовать и без использования специального класса — достаточно просто указать параметр n_split=n в инициализаторе KFold, где n — количество строк в таблице.

* ### БОРЬБА С ДИСБАЛАНСОМ
    * Взвешивание объектов. В функцию ошибки добавляется штраф, прямо пропорциональный количеству объектов каждого класса. 
    * Выбор порога вероятности. Заключается в том, что мы подбираем такой порог вероятности (по умолчанию он равен 0.5 во всех моделях), при котором на валидационной выборке максимизируется целевая метрика.
    * Сэмплирование (sampling) — перебалансировка выборки искусственным путём:  
        * oversampling — искусственное увеличение количества объектов миноритарного класса;
        * undersampling — сокращение количества объектов мажоритарного класса:
            Здесь могут использоваться алгоритмы генерации искусственных данных, такие как NearMiss, SMOTE (Synthetic Minority Oversampling Techniques) и ADASYN (Adaptive Synthetic).
            Мы рассмотрим наиболее популярный алгоритм — SMOTE
        ``` python
        from imblearn.over_sampling import SMOTE
        sm = SMOTE(random_state=42)
        X_train_s, y_train_s = sm.fit_resample(X_train, y_train)
        ```
---

## ***РЕГРЕССИЯ***

* ### АНАЛИТИЧЕСКОЕ РЕШЕНИЕ (NumPy)

* ### АНАЛИТИЧЕСКОЕ РЕШЕНИЕ "Линейная регрессия" (sklearn)
    ``` python
    from sklearn import linear_model    
    lr_model = linear_model.LinearRegression()
    ```

* ### ЧИСЛОВОЕ РЕШЕНИЕ "Градиентный спуск (Gradient descent)" (sklearn)
    ``` python
    from sklearn import linear_model
    sgd_lr_model = linear_model.SGDRegressor()
    ```

* ### ПОЛИНОМИАЛЬНЫЕ ПРИЗНАКИ (Полиномиальная регрессия (Polynomial Regression))
    * Нужно проводить стандартизацию и нормальзацию до этого этапа
    ``` python
    from sklearn import preprocessing
    poly = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
    poly.fit(X_train)
    X_train_poly = poly.transform(X_train)
    ```
    
* ### РЕГУЛЯРИЗАЦИЯ (борьба с разбросом (переобучением)) 
    * L1-регуляризация (Lasso)
        ``` python
        lasso_lr_poly = linear_model.Lasso(alpha=0.1)
        lasso_lr_poly.fit(X_train_scaled_poly, y_train)
        ```
    * L2-регуляризация (Ridge), или регуляризация Тихонова
        ``` python
        ridge_lr_poly = linear_model.Ridge(alpha=10)
        ridge_lr_poly.fit(X_train_scaled_poly, y_train)
        ```

* ### МЕТРИКИ РЕГРЕССИИ 
    ``` python
    from sklearn import metrics
    ```
    * MAE (Mean Absolute Error)             - mean_absolute_error(y, y_pred)
    * MAPE (Mean Absolute Percent Error)    - mean_absolute_percentage_error(y, y_pred)*100
    * MSE (Mean Square Error)               - mean_square_error(y, y_pred)
    * RMSE (Root Mean Squared Error)        - np.sqrt(mean_square_error(y, y_pred))
    * R2 (Коэффициент детерминации)         - r2_score(y, y_pred)

---

## ***КЛАССИФИКАЦИЯ***

* ### ЧИСЛОВОЕ РЕШЕНИЕ "Логистическая регрессия"
    ``` python
    from sklearn import linear_model
    log_reg_model = linear_model.LogisticRegression()
    ```

* ### МУЛЬТИКЛАССОВАЯ КЛАССИФИКАЦИЯ (когда не 2 класса, а больше)
    * Сравнивает класс 0 с классом 1 и 2, потом класс 1 с классами 0 и 2 и т. д.
    ``` python
    from sklearn import linear_model
    log_reg_model = linear_model.LogisticRegression(
        multi_class='multinomial', #мультиклассовая классификация
    )
    ```

* ### ДЕРЕВЬЯ РЕШЕНИЙ (связанный ациклический граф)
    * состоит из корневой вершины, внутренних вершин и листьев
    * Предикаты - критерии находящиеся на вершинах
    ``` python
    from sklearn import tree # Модели деревьев решения
    # Создаём объект класса DecisionTreeClassifier
    dt_clf_model = tree.DecisionTreeClassifier()
    dt_clf_model.get_depth() # Показывает дерево
    ```

* ### АНСАМБЛИ (БЕГГИНГ) "Случайный лес"
    * Много слабых моделей объединяются в одну
    * Виды ансамблей 
        * Бэггинг — параллельно обучаем множество одинаковых моделей, а для предсказания берём среднее по предсказаниям каждой из моделей.
        * Бустинг — последовательно обучаем множество одинаковых моделей, где каждая новая модель концентрируется на тех примерах, где предыдущая допустила ошибку.
        * Стекинг — параллельно обучаем множество разных моделей, отправляем их результаты в финальную модель, и уже она принимает решение.
    ``` python 
    from sklearn import ensemble
    rf_clf_model = ensemble.RandomForestClassifier(
        n_estimators=500, #число деревьев
    )
    ```

* ### МЕТРИКИ КЛАССИФИКАЦИИ 
    ```python
    from sklearn import metrics
    ```
    * Матрица ошибок                        - confusion_matrix(y, y_pred)
    * Accuracy (достоверность)              - accuracy_score(y, y_pred)
        * чем ближе к 1, тем больше угадала
    * Precision (точность) или              - precision_score(y, y_pred)
        * PPV (Positive Predictive Value)
        * чем ближе к 1, тем меньше ошибок
    * Recall (полнота) или                  - recall_score(y, y_pred)
        * TPR (True Positive Rate)
        * чем ближе к 1, тем больше значений 1 класса названо правильно
    * F-мера                                - f1_score(y, y_pred)
        * (это взвешенное среднее гармоническое между precision и recall)
        * чем ближе к 1, тем точнее модель
    * Все ошибки в одном отчете             - classification_report(y, y_pred)

---

## ***КЛАСТЕРИЗАЦИЯ***

* ### ОПРЕДЕЛЕНИЕ ОПТИМАЛЬНОГО КОЛИЧЕСТВА КЛАСТЕРОВ
    * #### МЕТОД ЛОКТЯ - построение графика зависимости инерции от количества кластеров
        ``` python
        model.inertia_ # получение инерции для создания графика
        ```

    * #### КОЭФФИЦИЕНТ СИЛУЭТА - построение графика зависимости коэффициента силуэта от количества кластеров
        * Коэффициент силуэта показывает, насколько объект похож на объекты кластера, в котором он находится, по сравнению с объектами из других кластеров.
        ``` python
        silhouette_score(X, model.labels_)
        ```
* ### EM - АЛГОРИТМЫ КЛАСТЕРИЗАЦИИ
    * В основе данного подхода лежит предположение, что любой объект принадлежит ко всем кластерам, но с разной вероятностью.
    * Представителями являются:
        * K-means кластеризация - например, для кластеризации документов
        * GMM кластеризация - например, для сегментации изображения


* ### КЛАСТЕРИЗАЦИЯ "АЛГОРИТМ K-MEANS"
    * Чувствительна к выбросам
    * K-MEANS - центроиды кластера это средние значения
    * K-MEANS++ - центроиды кластера это средние значения, но первые значения выбираются не случайно
    * K-MEDIANS - центроиды кластера это медианные значения
    * K-MEDOIDS - центроиды кластера это медианные значения, но не расчетное значение, а ближайшая к нему точка
    * FUZZY C-MEANS - каждый объект может принадлежать к разным кластерам с разной вероятностью
    ``` python
    from sklearn.cluster import KMeans
    k_means_model = KMeans(n_clusters=2, init='k-means++', n_init=10, random_state=42)
    ```
* ### КЛАСТЕРИЗАЦИЯ "GMM" - модель гауссовой смеси (Gaussian Mixture Model)
    * Чувствительна к выбросам
    ``` python
    from sklearn.mixture import GaussianMixture
    gm_clst_model = GaussianMixture()
    ```

* ### "ИЕРАРХИЧЕСКАЯ" КЛАСТЕРИЗАЦИЯ
    * Принцип иерархической кластеризации основан на построении дерева (иерархии) вложенных кластеров.
    * Строится дендрограмма - это древовидная диаграмма, которая содержит  уровней. Каждый уровень — это шаг укрупнения кластеров.
    * Методы построения дендрограммы:
        * Агломеративный метод (agglomerative) - объединение мелких кластеров
        * Дивизионный (дивизивный) метод (divisive) - деление крупных кластеров
    * Методы расчета расстояния между кластерами
        * Метод одиночной связи (min расстояние)
        * Метод полной связи    (max расстояние)
        * Метод средней связи   (mean расстояние)
        * Центроидный метод     (расстояние м/ж центрами)
    ``` python
    from sklearn.cluster import AgglomerativeClustering
    agg_clst_model = AgglomerativeClustering()
    ```

* ### **ПОНИЖЕНИЕ РАЗМЕРНОСТИ**
    * #### СПЕКТРАЛЬНАЯ КЛАСТЕРИЗАЦИЯ
        * 
        * Применяется для: 
            * сегментации изображений
        ``` python
        from sklearn.cluster import SpectralClustering
        spectral_clst_model = SpectralClustering()
        ```

    * #### PCA - линейное преобразование
        * Метод главных компонент, или PCA (Principal Components Analysis)
        * это один из базовых способов уменьшения размерности
        * Применяется для:  
            * подавление шума
            * индексация видео
        ``` python
        from sklearn.decomposition import PCA
        pca = PCA()
        ```

    * #### t-SNE - нелинейное преобразование
        * t-SNE (t-distributed Stochastic Neighbor Embedding)
        * «стохастическое вложение соседей с t-распределением»
        * при преобразовании похожие объекты оказываются рядом, а непохожие — далеко друг от друга
        * Применяется для:  
            * уменьшения размерность до 2х или 3х мерного
        ``` python
        from sklearn.manifold import TSNE
        tsne = TSNE()
        ```

* ### КЛАСТЕРИЗАЦИЯ НА ОСНОВЕПЛОТНОСТИ (DBSCAN)
    * DENSITY-BASED SPATIAL CLUSTERING OF APPLICATIONS WITH NOISE
    * В отличие от k-means, не нужно задавать количество кластеров — алгоритм сам определит оптимальное
    * Алгоритм хорошо работает с данными произвольной формы
    * DBSCAN отлично справляется с выбросами в датасетах
    ``` python
    from sklearn.cluster import DBSCAN
    clst_model = DBSCAN()    
    ```
* ### ВИЗУАЛИЗАЦИЯ КЛАСТЕРИЗАЦИЙ
    * диаграмма рассеяния для двухмерного и трёхмерного случаев 
    * Convex Hull, или выпуклая оболочка - провести гарницы
    * дендрограмма 
    * Clustergram - "полосы" - только для иерархических кластеризаций

* ### МЕТРИКИ КЛАСТЕРИЗАЦИИ 
    ``` python
    from sklearn.metrics.cluster import homogeneity_score
    from sklearn.metrics.cluster import completeness_score
    from sklearn.metrics.cluster import v_measure_score
    from sklearn.metrics.cluster import rand_score
    ```
    * Однородность кластеров                - homogeneity_score(y, y_pred)
    * Полнота кластеров                     - completeness_score(y, y_pred)
    * V-мера (комбинация однор. и полн.)    - v_measure_score(y, y_pred)
    * Индекс Ренда                          - rand_score(y, y_pred)

---

