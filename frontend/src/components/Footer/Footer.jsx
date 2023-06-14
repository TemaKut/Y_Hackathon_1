import React from 'react';

import Style from './Footer.module.scss';
import boardLogo from '../../images/board-logo.svg';

// eslint-disable-next-line react/prop-types
function Footer({ isStart, isFinal, keyboardClick, goBack }) {
  const buttonText = isStart ? 'Не сканируется' : 'Назад';

  return (
    <footer className={`${Style.footer} `}>
      <button
        onClick={goBack}
        type="button"
        className={`${Style.footer__button} `}
      >
        {buttonText}
      </button>
      {!isFinal && (
        <button
          onClick={keyboardClick}
          type="button"
          className={Style.container}
        >
          <img
            className={Style.footer__boardlogo}
            src={boardLogo}
            alt="ракета"
          />
          <p className={`${Style.footer__boardtitle} `}>Ввести с клавиатуры</p>
        </button>
      )}
    </footer>
  );
}

export default Footer;
