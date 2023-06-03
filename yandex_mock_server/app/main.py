import csv

from fastapi import FastAPI


app = FastAPI(title='Mock server (Yandex db)')


@app.get('/product/{sku}')
async def get_product(sku: str):
    """ Получить продукт по sku. """

    with open('app/data/sku.csv', 'r') as data_csv:
        reader = csv.DictReader(data_csv)

        for row in reader:

            if row.get('sku') == sku:
                return row

    return None


@app.get('/carton/{cartontype}')
async def get_carton(cartontype: str):
    """Получить коробку по ее типу."""

    with open('app/data/carton.csv') as data_csv:
        reader = csv.DictReader(data_csv)
        for row in reader:
            if row.get('CARTONTYPE') == cartontype:
                return row
    return None


@app.get('/cargotype_info/{cargotype}')
async def get_cargotype(cargotype: str):
    """Получить карготип по ее номеру."""

    with open('app/data/cargotype_info.csv') as data_csv:
        reader = csv.DictReader(data_csv)
        for row in reader:
            if row.get('cargotype') == cargotype:
                return row
    return None


@app.get('/scu_cargotype/{scu}')
async def get_scu_cargotype(scu: str):
    """Получить карготип продукта."""

    # Необходимо положить файл sku_cargotypes.csv в /data
    with open('app/data/sku_cargotypes.csv') as data_csv:
        reader = csv.DictReader(data_csv)
        for row in reader:
            if row.get('scu') == scu:
                return row
    return None
