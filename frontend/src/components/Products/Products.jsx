// import React from 'react';
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import useAsync from '../../utils/useAsync';
import getOrderProducts from '../../utils/getOrderProducts';
import Style from './Products.module.scss';
import Button from '../UI/Button/Button';
import Cell from '../Cell/Cell';
import Card from './Card/Card';

function Products({ cellName, orderKey }) {
  const [productsCell, setProductsCell] = useState([]);
  console.log(orderKey);
  console.log(cellName);
  if (productsCell) {
    console.log(productsCell);
  }
  const { value } = useAsync(getOrderProducts, orderKey);
  useEffect(() => {
    if (value) {
      setProductsCell(value);
    }
  }, [value]);
  return setProductsCell ? (
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
      <Cell cellName={cellName} />
      <div className={Style.productsContainer}>
        <div className={Style.specs}>
          <span className={`${Style.amount} ${Style.spec}`}>6 товаров</span>
          <span className={`${Style.delivery} ${Style.spec}`}>
            Почта России
          </span>
        </div>
        <ul className={Style.cards}>
          {productsCell.map(({ ...card }) => (
            <Card card={card} />
          ))}
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
  ) : null;
}

Products.propTypes = {
  cellName: PropTypes.string,
  orderKey: PropTypes.string,
};

Products.defaultProps = {
  cellName: '',
  orderKey: '',
};

export default Products;
