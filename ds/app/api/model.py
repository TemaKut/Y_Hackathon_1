from fastapi import APIRouter, Body
import pandas as pd
import numpy as np
import pickle

from app.schemas import ProductToPredict


order_model_router = APIRouter()


@order_model_router.post('/predict')
def predict(x: list[ProductToPredict] = Body()):
    """
    Функция принимает на вход json запрос, обученную модель,
    выполняет преобразование признаков и предсказание.
    """

    # Загрузка модели
    try:
        with open('app/pickle_model/model_lgbm_v4.pcl', 'rb') as fid:
            model = pickle.load(fid)
    except:
        with open('/code/app/pickle_model/model_lgbm_v4.pcl', 'rb') as fid:
            model = pickle.load(fid)

    # Названия столбцов из тренировочного датасета
    col = [
        'type_0.0', 'type_20.0', 'type_40.0', 'type_81.0',
        'type_110.0', 'type_120.0', 'type_130.0', 'type_140.0',
        'type_160.0', 'type_200.0', 'type_210.0', 'type_290.0',
        'type_291.0', 'type_292.0', 'type_300.0', 'type_301.0',
        'type_302.0', 'type_303.0', 'type_305.0', 'type_310.0',
        'type_315.0', 'type_320.0', 'type_330.0', 'type_340.0',
        'type_350.0', 'type_360.0', 'type_400.0', 'type_410.0',
        'type_440.0', 'type_441.0', 'type_460.0', 'type_480.0',
        'type_485.0', 'type_490.0', 'type_510.0', 'type_520.0',
        'type_600.0', 'type_601.0', 'type_610.0', 'type_611.0',
        'type_620.0', 'type_621.0', 'type_622.0', 'type_623.0',
        'type_640.0', 'type_641.0', 'type_670.0', 'type_671.0',
        'type_672.0', 'type_673.0', 'type_690.0', 'type_691.0',
        'type_692.0', 'type_710.0', 'type_720.0', 'type_750.0',
        'type_751.0', 'type_770.0', 'type_780.0', 'type_790.0',
        'type_799.0', 'type_801.0', 'type_900.0', 'type_901.0',
        'type_905.0', 'type_908.0', 'type_910.0', 'type_911.0',
        'type_920.0', 'type_930.0', 'type_931.0', 'type_950.0',
        'type_955.0', 'type_960.0', 'type_970.0', 'type_980.0',
        'type_990.0', 'type_1010.0', 'type_1011.0', 'type_1300.0',
    ]

    # Преобразование запроса в датафрейм
    skus = []
    counts = []
    size1s = []
    size2s = []
    size3s = []
    weights = []
    types = []

    for i in range(len(x)):
        x[i] = x[i].dict()

        for t in x[i]['cargotypes']:
            skus.append(x[i]['sku'])
            counts.append(x[i]['count'])
            size1s.append(x[i]['a'])
            size2s.append(x[i]['b'])
            size3s.append(x[i]['c'])
            weights.append(x[i]['goods_wght'])
            types.append(t)

    new_data = pd.DataFrame(
        {
            'sku': skus,
            'count': counts,
            'a': size1s,
            'b': size2s,
            'c': size3s,
            'goods_wght': weights,
            'cargotypes': types,
        }
    )
    
    def make_types(df):
        '''Фукция добавляет 1 в соотвествующий товару карготип'''
        pivoted = pd.pivot_table(
            df.assign(val=1), values='val',
            index=['sku'], columns=['cargotypes'],
            aggfunc=lambda x: 1, fill_value=0,
        )

        pivoted.columns = [
            'type_' + str(x) if x != 'sku' else x for x in pivoted.columns
        ]

        # Сбросим индексы
        pivoted_def = pivoted.reset_index()

        return pivoted_def

    def merge_data(df):
        '''Объединить данные'''
        pivoted = make_types(df)
        df = pd.merge(df, pivoted, on=['sku'])
        df = df.drop(['cargotypes'], axis=1)
        df = df.drop_duplicates()

        return df

    #заменим тип данных
    new_data['cargotypes'] = new_data['cargotypes'].astype(float)
    # Преобразование признаков x из запроса
    df_for_model = merge_data(new_data)

    # находим отсутствующие признаки (разница между трейном и запросом)
    col = [item for item in col if item not in df_for_model.columns]

    # Датафрейм с нулями в пустых карготипах
    temp = pd.DataFrame(
        0,
        index=np.arange(len(df_for_model)),
        columns=col,
    )
    # Объединие признаков
    x_temp = pd.concat(
        [df_for_model, temp.reindex(df_for_model.index)],
        axis=1,
    )
    # Заполнение пропусков
    x_temp = x_temp.fillna(0)
    # Создадим идентификатор заказа для группировки
    x_temp['order'] = 1
    # Скопируем датафрейм
    x_part_1 = x_temp.copy()

    # Cоздадим промежуточный датафрейм
    # для сохранения статистических данных о sku
    temp_features = x_temp.loc[:, ['a', 'b', 'c', 'goods_wght']]

    def feature_volume(df):
        '''Функция для создания признака объем для каждого sku в заказе'''
        df['volume'] = df['a'] * df['b'] * df['c']

        return df

    def new_group_features(df):
        '''создание статистических признаков для sku в заказе'''
        df['goods_wght_mean'] = df['goods_wght'].mean()
        df['volume_mean'] = df['volume'].mean()
        df['volume_max'] = df['volume'].max()
        df['volume_min'] = df['volume'].min()
        df['a_mean'] = df['a'].mean()
        df['a_max'] = df['a'].max()
        df['a_min'] = df['a'].min()
        df['b_mean'] = df['b'].mean()
        df['b_max'] = df['b'].max()
        df['b_min'] = df['b'].min()
        df['c_mean'] = df['c'].mean()
        df['c_max'] = df['c'].max()
        df['c_min'] = df['c'].min()

        return df
    
    def new_features_log(df):
        '''создание нового признака'''
        
        def size_ratio(x, y, z):
            '''добавление нового признака'''
            
            return x * y * z / (x + y + z + 1e-3)
        
        df['size'] = df.apply(lambda row: size_ratio(row['a'], row['b'], row['c']), axis=1)
        
        return df

    # Cоздадим новые признаки в соответствии с обучащими данными
    temp_features = feature_volume(temp_features)
    temp_features = new_group_features(temp_features)

    # Заменим признак с объемом каждого товара на общий объем заказа
    temp_features['volume'] = temp_features['volume'].sum()

    # Оставим одну строку с данными по одному заказу
    temp_features = (
        temp_features
        .drop(['a', 'b', 'c', 'goods_wght'], axis=1)
        .drop_duplicates()
    )

    # Сгруппируем данные об sku для целого заказа
    x = x_part_1.groupby('order').sum()
    x = x.reset_index(drop=True)

    # соединим данные по заказу со статистическими признаками для sku в заказе
    x = pd.concat([x, temp_features.reindex(x.index)], axis=1)
    
    #добавим новый признак
    x = new_features_log(x)
    
    x = x.drop('sku', axis=1)
    x['count'] = df_for_model['count'].sum()

    # Определим список отсортированных по размеру упаковок
    pack = [
        'NONPACK', 'STRETCH', 'YML', 'YMX',
        'YME', 'YMG', 'YMW',  'YMF', 'YMC',
        'MYE', 'MYD', 'YMA', 'MYC', 'YMV',
        'YMU', 'MYB', 'MYF', 'MYA',
    ]
    
    x.sort_index(axis=1, inplace=True)
     

    # Вызываем предсказание
    prediction = model.predict(x).tolist()

    # Далее подберем несколько вариантов упаковки в дополнение к оптимальному
    result = []

    for i in range(len(pack)):

        try:

            if prediction[0] == pack[i]:
                result.append(pack[i-1])
                result.append(pack[i+1])

        except Exception:

            if prediction[0] == 'NONPACK':
                result.append('STRETCH')

            elif prediction[0] == 'MYA':
                result.append('STRETCH')

    # Соединим все варианты упаковки
    y = prediction + result

    # Создадим словарь из результата
    y = {'s': y[2], 'm': y[0], 'l': y[1]}
    
    return y
