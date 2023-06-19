import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import Style from './Products.module.scss';
import Button from '../UI/Button/Button';
import Cell from '../Cell/Cell';
import Card from './Card/Card';
import Keyboard from '../Keyboard/Keyboard';

function Products({
  cellName,
  productsCell,
  setIsPopupOpen,
  isKeyboardOpen,
  setIsKeyboardOpen,
}) {
  const navigate = useNavigate();
  const [allChecked, setAllChecked] = useState(false);
  let allProductsCount = 0;

  if (productsCell) {
    for (let i = 0; i < productsCell.length; i += 1) {
      allProductsCount += productsCell[i].count;
    }
  }
  const handleClickBtn = () => {
    navigate('/package');
  };

  const handleClickProblem = () => {
    setIsPopupOpen(true);
    setTimeout(setIsPopupOpen, 2000, false);
  };

  return productsCell ? (
    <>
      <section className={Style.products}>
        <Button
          onClickBtn={handleClickProblem}
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
            <span className={`${Style.amount} ${Style.spec}`}>
              {allProductsCount} товар
            </span>
            <span className={`${Style.delivery} ${Style.spec}`}>
              Почта России
            </span>
          </div>
          <ul className={Style.cards}>
            {productsCell.map(({ ...card }) => (
              <Card
                key={card.sku}
                card={card}
                setAllChecked={setAllChecked}
                allChecked={allChecked}
              />
            ))}
          </ul>
        </div>
        <Button
          onClickBtn={handleClickBtn}
          // isHidden will be updated with logic
          isHidden
          allChecked={allChecked}
          btnPosition="right"
          btnColor="yellow"
          btnSize="big"
          // isSubmit
          ariaLabelText="Подобрать упаковку"
        >
          Подобрать упаковку
        </Button>
      </section>
      <Keyboard
        isKeyboardOpen={isKeyboardOpen}
        setIsKeyboardOpen={setIsKeyboardOpen}
        // will be updated with validation sku logic
        compareData="data"
        nextRoute="/package"
        titleText="Введите код товара"
      />
    </>
  ) : null;
}

Products.propTypes = {
  cellName: PropTypes.string,
  isKeyboardOpen: PropTypes.bool.isRequired,
  setIsKeyboardOpen: PropTypes.func.isRequired,
  // eslint-disable-next-line react/forbid-prop-types
  productsCell: PropTypes.array.isRequired,
  setIsPopupOpen: PropTypes.func.isRequired,
};

Products.defaultProps = {
  cellName: '',
};

export default Products;
