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
  loading,
}) {
  const [popupText, setPopupText] = useState('');
  useEffect(
    () => {
      if (loading) {
        setPopupText('Данные загружаются');
      } else if (isKeyboardOpen) {
        setPopupText('Некорректная попытка запроса');
      } else if (isPackage) {
        setPopupText('Спасибо за информацию!');
      } else if (
        !isKeyboardOpen &&
        ((!loading && isStart) || (!loading && isProducts))
      ) {
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
  loading: PropTypes.bool.isRequired,
};

Popup.defaultProps = {
  isStart: false,
  isPackage: false,
  isProducts: false,
};

export default Popup;
