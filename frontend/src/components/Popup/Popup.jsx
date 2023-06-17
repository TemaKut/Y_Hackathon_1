import React from 'react';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Style from './Popup.module.scss';

function Popup({ isPopupOpen }) {
  if (!isPopupOpen) return null;

  return (
    <ReactPortal wrapperId="Popup-container">
      <section className={`${Style.popup} ${isPopupOpen}`}>
        <div className={Style.container}>
          <h2 className={Style.title}>Спасибо за информацию!</h2>
          <p className={Style.text}>Подбираю другой вариант упаковки</p>
          <div className={Style.image} />
        </div>
      </section>
    </ReactPortal>
  );
}

Popup.propTypes = {
  isPopupOpen: PropTypes.bool.isRequired,
};

export default Popup;
