import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Style from './Footer.module.scss';
import boardLogo from '../../images/board-logo.svg';

function Footer({ isStart, isFinal, keyboardClick, goBack }) {
  const [buttonText, setButtonText] = useState('');
  useEffect(() => {
    if (isStart) {
      setButtonText('Не сканируется');
      return;
    }
    setButtonText('Назад');
  }, [isStart, isFinal]);

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

Footer.propTypes = {
  isStart: PropTypes.bool,
  isFinal: PropTypes.bool,
  goBack: PropTypes.func.isRequired,
  keyboardClick: PropTypes.func.isRequired,
};

Footer.defaultProps = {
  isStart: false,
  isFinal: false,
};

export default Footer;
