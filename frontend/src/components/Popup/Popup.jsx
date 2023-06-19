import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Style from './Popup.module.scss';

function Popup({
  isStart,
  isPackage,
  isProducts,
  isPopupOpen,
  isKeyboardOpen,
}) {
  const [popupText, setPopupText] = useState('');
  useEffect(
    () => {
      console.log(isKeyboardOpen);
      if (isKeyboardOpen) {
        setPopupText('Некорректная попытка запроса');
      } else if (isPackage) {
        setPopupText('Спасибо за информацию!');
      } else if (!isKeyboardOpen && (isStart || isProducts)) {
        setPopupText('Скоро придут Вам помочь');
      }
    },
    [isStart],
    [isProducts],
    [isPackage],
    [isKeyboardOpen]
  );
  if (!isPopupOpen) return null;

  return (
    <ReactPortal wrapperId="Popup-container">
      <section className={`${Style.popup} ${isPopupOpen}`}>
        <div className={Style.container}>
          <h2 className={Style.title}>{popupText}</h2>
          {isPackage && (
            <p className={Style.text}>Подбираю другой вариант упаковки</p>
          )}
          <div className={Style.image} />
        </div>
      </section>
    </ReactPortal>
  );
}

Popup.propTypes = {
  isPopupOpen: PropTypes.bool.isRequired,
  isKeyboardOpen: PropTypes.bool.isRequired,
  isStart: PropTypes.bool,
  isPackage: PropTypes.bool,
  isProducts: PropTypes.bool,
};

Popup.defaultProps = {
  isStart: false,
  isPackage: false,
  isProducts: false,
};

export default Popup;
