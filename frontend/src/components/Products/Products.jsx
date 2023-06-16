import React from 'react';
import Style from './Products.module.scss';
import Cell from '../Cell/Cell';
import Card from './Card/Card';

function Products() {
  return (
    <>
      <Cell />
      <div className={Style.products}>
        <div className={Style.specs}>
          <span className={`${Style.amount} ${Style.spec}`}>6 товаров</span>
          <span className={`${Style.delivery} ${Style.spec}`}>
            Почта России
          </span>
        </div>
        <ul className={Style.cards}>
          <Card />
        </ul>
      </div>
    </>
  );
}

export default Products;
