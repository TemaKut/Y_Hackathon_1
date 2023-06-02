import sqlalchemy as sa

from app.database.connection import Base


class Order(Base):
    """ Модель БД. Заказ. """
    __tablename__ = 'orders'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment='ID заказа.'
    )


class Product(Base):
    __tablename__ = 'products'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment='ID продукта.'
    )