import React from 'react';
import Style from './Products.module.scss';
import Button from '../UI/Button/Button';
import Cell from '../Cell/Cell';
import Card from './Card/Card';

function Products() {
  return (
    <section className={Style.products}>
      <Button
        // onClickBtn={handleClickBtn}
        btnPosition="left"
        btnColor="grey"
        btnSize="big"
        ariaLabelText="Есть проблема"
      >
        Есть проблема
      </Button>
      <Cell />
      <div className={Style.productsContainer}>
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
      <Button
        // onClickBtn={handleClickBtn}
        // isHidden will be updated with logic
        isHidden
        btnPosition="right"
        btnColor="yellow"
        btnSize="big"
        isSubmit
        ariaLabelText="Подобрать упаковку"
      >
        Подобрать упаковку
      </Button>
    </section>
  );
}

export default Products;
