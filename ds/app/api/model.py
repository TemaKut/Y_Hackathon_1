import json
import os
import pandas as pd
import numpy as np
import pickle
from pickle import dump, load
import requests

def predict(x):
    """Функция принимает на вход json запрос, обученную модель,
    выполняет преобразование признаков и предсказание"""    
    
    #загрузка модели
    with open('app/pickle_model/model_lgbm_test1.pcl', 'rb') as fid:
        model = pickle.load(fid)
    
    #названия столбцов из тренировочного датасета
    col = ['type_0.0', 'type_20.0', 'type_40.0', 'type_81.0', 
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
           'type_990.0', 'type_1010.0', 'type_1011.0', 'type_1300.0']

    # преобразование запроса в датафрейм
    skus = []
    counts = []
    size1s = []
    size2s = []
    size3s = []
    weights = []
    types = []

    for item in x['items']:
        for t in item['cargotypes']:
            skus.append(item['sku'])
            counts.append(item['count'])
            size1s.append(item['a'])
            size2s.append(item['b'])
            size3s.append(item['c'])
            weights.append(item['goods_wght'])
            types.append(t)
    
    new_data = pd.DataFrame({'sku': skus,
                             'count': counts,
                             'a': size1s,
                             'b': size2s,
                             'c': size3s,
                             'goods_wght': weights,
                             'cargotypes': types})
    
    #фукция добавляет 1 в соотвествующий товару карготип
    def make_types(df):
        pivoted = pd.pivot_table(df.assign(val=1), values='val',
                                 index=['sku'], columns=['cargotypes'], 
                                 aggfunc=lambda x: 1, fill_value=0)
        pivoted.columns = ['type_' + str(x) if x!='sku' else x for x in pivoted.columns]
        #сбросим индексы
        pivoted_def = pivoted.reset_index()
        return pivoted_def
    
    def merge_data(df):
        pivoted = make_types(df)
        df = pd.merge(df, pivoted, on=['sku'])
        df = df.drop(['cargotypes'], axis=1)
        df = df.drop_duplicates()
        return df
    
    #преобразование признаков x из запроса
    df_for_model = merge_data(new_data)
    
    '''находим отсутствующие признаки 
    (разница между трейном и запросом)'''
    col = [item for item in col if item not in df_for_model.columns]
    
    #датафрейм с нулями в пустых карготипах
    temp = pd.DataFrame(0, index=np.arange(len(df_for_model)), 
                        columns=col)
    #объединие признаков
    x_temp = pd.concat([df_for_model, 
                       temp.reindex(df_for_model.index)], 
                       axis=1)
    #заполнение пропусков
    x_temp = x_temp.fillna(0)
    #создадим идентификатор заказа для группировки
    x_temp['order'] = 1
    #скопируем датафрейм
    x_part_1 = x_temp.copy()
    
    '''создадим промежуточный датафрейм для сохранения 
    статистических данных о sku'''
    temp_features = x_temp.loc[:,['a', 'b', 'c', 'goods_wght']]
    
    #создадим новые признаки в соответствии с обучащими данными
    temp_features = feature_volume(temp_features)
    temp_features = new_group_features(temp_features)
    #заменим признак с объемом каждого товара на общий объем заказа
    temp_features['volume'] = temp_features['volume'].sum()
    #оставим одну строку с данными по одному заказу
    temp_features = (temp_features
                     .drop(['a', 'b', 'c', 'goods_wght'], axis=1)
                     .drop_duplicates())

    #сгруппируем данные об sku для целого заказа
    x = x_part_1.groupby('order').sum()
    x = x.reset_index(drop=True)
    
    '''соединим данные по заказу со статистическими 
    признаками для sku в заказе'''
    x = pd.concat([x, temp_features.reindex(x.index)], 
                  axis=1)
    
    #определим список отсортированных по размеру упаковок
    pack = ['NONPACK', 'STRETCH', 'YML', 'YMX', 
            'YME', 'YMG', 'YMW',  'YMF', 'YMC', 
            'MYE', 'MYD', 'YMA', 'MYC', 'YMV', 
            'YMU', 'MYB', 'MYF', 'MYA']
    
    #вызываем предсказание
    prediction = model.predict(x).tolist()
    
    '''далее подберем несколько вариантов упаковки 
    в дополнение к оптимальному'''
    result = []
    for i in range(len(pack)):
        try:
            if prediction[0] == pack[i]:
                result.append(pack[i-1])
                result.append(pack[i+1])
        except:
            if prediction[0] == 'NONPACK':
                result.append('STRETCH')
            elif prediction[0] == 'MYA':
                result.append('STRETCH')
    
    #соединим все варианты упаковки
    y = prediction + result
    #создадим словарь из результата
    y =  {'s': y[2], 'm': y[0], 'l': y[1]}
              
    return y

def feature_volume(df):
    '''Функция для создания признака объем
    для каждого sku в заказе'''
    
    df['volume'] = df['a'] * df['b'] * df['c']
    
    return df

def new_group_features(df):
    '''создание статистических признаков для 
    sku в заказе'''

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
    '''функция для создания нового признака'''

    def size_ratio(x, y, z):
        '''создание логарифмического признака
        по размеру sku'''
        
        return x * y * z / (x + y + z + 1e-3)

    df['size'] = df.apply(lambda row: size_ratio(row['a'], row['b'], row['c']), axis=1)
    
    return df
