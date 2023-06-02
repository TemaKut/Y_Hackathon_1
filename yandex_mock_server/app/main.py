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
