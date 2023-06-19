import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Button from '../UI/Button/Button';
import Style from './Keyboard.module.scss';

function Keyboard({
  isKeyboardOpen,
  setIsKeyboardOpen,
  compareData,
  nextRoute,
  titleText,
  isPackage,
  setIsPopupOpen,
  handleScanSku,
}) {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState('');
  if (!isKeyboardOpen) return null;

  const handleChange = (e) => {
    setInputValue(() => e.target.value);
  };
  const allProductsInfo = JSON.parse(localStorage.getItem('allProductsInfo'));

  const handleClickBtn = () => {
    if (isPackage) {
      navigate(nextRoute);
    }
    if (inputValue === compareData) {
      navigate(nextRoute);
      setIsKeyboardOpen(false);
    } else if (inputValue === '') {
      setIsPopupOpen(true);
      setTimeout(setIsPopupOpen, 2000, false);
    } else if (inputValue === allProductsInfo[0].sku) {
      console.log('товар смэтчен');
      handleScanSku();
      setIsKeyboardOpen(false);
    } else {
      setIsPopupOpen(true);
      setTimeout(setIsPopupOpen, 2000, false);
    }
  };

  return (
    <ReactPortal wrapperId="keyboard-container">
      <section
        className={`${Style.keyboard} ${isKeyboardOpen && Style.keyboard_open}`}
      >
        <div className={Style.inputContainer}>
          <h2 className={Style.title}>{titleText}</h2>
          <input
            className={Style.input}
            type="text"
            value={inputValue}
            onChange={handleChange}
          />
        </div>
        <Button
          onClickBtn={handleClickBtn}
          btnPosition="right"
          btnColor="yellow"
          btnSize="big"
          ariaLabelText="Готово"
        >
          Готово
        </Button>
      </section>
    </ReactPortal>
  );
}

Keyboard.propTypes = {
  isKeyboardOpen: PropTypes.bool.isRequired,
  setIsKeyboardOpen: PropTypes.func.isRequired,
  compareData: PropTypes.string.isRequired,
  nextRoute: PropTypes.string.isRequired,
  titleText: PropTypes.string.isRequired,
  isPackage: PropTypes.bool,
  setIsPopupOpen: PropTypes.func.isRequired,
  handleScanSku: PropTypes.func.isRequired,
};

Keyboard.defaultProps = {
  isPackage: false,
};

export default Keyboard;
