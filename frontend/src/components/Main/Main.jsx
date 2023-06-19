import React from 'react';
import PropTypes from 'prop-types';
import Style from './Main.module.scss';
import Cell from '../Cell/Cell';
import Button from '../UI/Button/Button';
import Keyboard from '../Keyboard/Keyboard';

function Main({
  cellName,
  isKeyboardOpen,
  setIsKeyboardOpen,
  orderKey,
  handleClickBtn,
  setIsPopupOpen,
}) {
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
          setIsPopupOpen={setIsPopupOpen}
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
        setIsPopupOpen={setIsPopupOpen}
      />
    </>
  );
}

Main.propTypes = {
  cellName: PropTypes.string,
  handleClickBtn: PropTypes.func.isRequired,
  isKeyboardOpen: PropTypes.bool.isRequired,
  setIsKeyboardOpen: PropTypes.func.isRequired,
  orderKey: PropTypes.string.isRequired,
  setIsPopupOpen: PropTypes.func.isRequired,
};

Main.defaultProps = {
  cellName: '',
};

export default Main;
