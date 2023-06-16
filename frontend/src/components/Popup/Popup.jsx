import React from 'react';
import PropTypes from 'prop-types';
// import ReactPortal from '../ReactPortal/ReactPortal';
import Style from './Popup.module.scss';
import happycarton from '../../images/happycarton.png';

function Popup({ isPopupOpen }) {
  if (!isPopupOpen) return null;

  return (
    // <ReactPortal wrapperId="Popup-container">
    <div className={`${Style.popup} ${isPopupOpen}`}>
      <section className={Style.container}>
        <h2 className={Style.title}>Спасибо за информацию!</h2>
        <p className={Style.text}>Подбираю другой вариант упаковки</p>
        <img
          className={Style.image}
          src={happycarton}
          alt="рисунок позитивной коробки"
        />
        {/* <form>
          <input className={Style.input} />
          {children}
        </form> */}
      </section>
    </div>
    // </ReactPortal>
  );
}

Popup.propTypes = {
  isPopupOpen: PropTypes.bool.isRequired,
};

export default Popup;
