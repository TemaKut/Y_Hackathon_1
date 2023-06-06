from typing import List

from pydantic import BaseModel


class User(BaseModel):
    username: str


class Order(BaseModel):
    box_num: str
    goods_wght: str
    orderkey: str
    pack_volume: str
    rec_calc_cube: str
    recommended_carton: str
    sel_calc_cube: str
    selected_carton: str
    sku: str
    trackingid: str
    who: str
    whs: str


class Product(BaseModel):
    sku: str
    logo: str
    name: str
    cargotypes: List[int]
    additionalPackaging: str
    userTip: str
