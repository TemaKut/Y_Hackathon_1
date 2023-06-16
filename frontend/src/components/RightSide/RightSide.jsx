import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Style from './RightSide.module.scss';

function RightSide({
  isStart,
  isFinal,
  isProducts,
  isKeyboardOpen,
  rightSideClick,
}) {
  const [rightSideText, setrightSideText] = useState('');

  useEffect(() => {
    if (isStart) {
      setrightSideText('Взять другое задание');
    }
    if (isKeyboardOpen || isFinal) {
      setrightSideText('Готово');
    }
    if (isProducts) {
      setrightSideText('Подобрать упаковку');
    }
  }, [isStart, isKeyboardOpen, isFinal, isProducts]);

  return (
    <button onClick={rightSideClick} type="button" className={Style.package}>
      {rightSideText}
    </button>
  );
}

RightSide.propTypes = {
  isStart: PropTypes.bool,
  isFinal: PropTypes.bool,
  isProducts: PropTypes.bool,
  isKeyboardOpen: PropTypes.bool,
  rightSideClick: PropTypes.func.isRequired,
};

RightSide.defaultProps = {
  isStart: false,
  isFinal: false,
  isProducts: false,
  isKeyboardOpen: false,
};

export default RightSide;
