import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Style from './RightSide.module.scss';

function RightSide({ isStart, isFinal, isKeyboardOpen, rightSideClick }) {
  const [rightSideText, setrightSideText] = useState('');

  useEffect(() => {
    if (isStart) {
      setrightSideText('Взять другое задание');
    }
    if (isKeyboardOpen) {
      setrightSideText('Готово');
    }
    if (isFinal) {
      setrightSideText('Подобрать упаковку');
    }
  }, [isStart, isKeyboardOpen, isFinal]);

  return (
    <button onClick={rightSideClick} type="button" className={Style.package}>
      {rightSideText}
    </button>
  );
}

RightSide.propTypes = {
  isStart: PropTypes.bool,
  isFinal: PropTypes.bool,
  isKeyboardOpen: PropTypes.bool,
  rightSideClick: PropTypes.func.isRequired,
};

RightSide.defaultProps = {
  isStart: false,
  isFinal: false,
  isKeyboardOpen: false,
};

export default RightSide;
