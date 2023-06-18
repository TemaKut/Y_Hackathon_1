import React from 'react';
import PropTypes from 'prop-types';
import Style from './Main.module.scss';
import getOrderCell from '../../utils/getOrderCell';
import Cell from '../Cell/Cell';
import Button from '../UI/Button/Button';
import Keyboard from '../Keyboard/Keyboard';

function Main({
  cellName,
  setOrderData,
  isKeyboardOpen,
  setIsKeyboardOpen,
  orderKey,
}) {
  const handleClickBtn = async () => {
    const newValue = await getOrderCell();

    setOrderData(newValue.cell);
  };

  return (
    <>
      <section className={Style.main}>
        <Cell cellName={cellName} />
        <Button
          onClickBtn={handleClickBtn}
          btnPosition="right"
          btnColor="yellow"
          btnSize="big"
          isSubmit={false}
          ariaLabelText="Взять другое задание"
        >
          Взять другое задание
        </Button>
      </section>
      <Keyboard
        isKeyboardOpen={isKeyboardOpen}
        setIsKeyboardOpen={setIsKeyboardOpen}
        compareData={orderKey}
        nextRoute="/products"
        titleText="Введите код ячейки"
      />
    </>
  );
}

Main.propTypes = {
  cellName: PropTypes.string,
  setOrderData: PropTypes.func.isRequired,
  isKeyboardOpen: PropTypes.bool.isRequired,
  setIsKeyboardOpen: PropTypes.func.isRequired,
  orderKey: PropTypes.string.isRequired,
};

Main.defaultProps = {
  cellName: '',
};

export default Main;
