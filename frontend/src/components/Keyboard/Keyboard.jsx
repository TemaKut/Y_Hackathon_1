/* eslint-disable no-alert */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Button from '../UI/Button/Button';
import Style from './Keyboard.module.scss';

function Keyboard({ isKeyboardOpen, setIsKeyboardOpen, orderKey, titleText }) {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState('');
  if (!isKeyboardOpen) return null;

  const handleChange = (e) => {
    setInputValue(() => e.target.value);
  };

  const handleClickBtn = () => {
    if (inputValue === orderKey) {
      navigate('/products');
      setIsKeyboardOpen(false);
    } else if (inputValue === '') {
      alert('Введите номер заказа');
    } else {
      alert('Введен неверный номер заказа');
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
            name="orderKey"
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
  orderKey: PropTypes.string.isRequired,
  titleText: PropTypes.string.isRequired,
};

export default Keyboard;
