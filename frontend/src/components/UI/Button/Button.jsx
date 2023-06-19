import React from 'react';
import PropTypes from 'prop-types';
import Style from './Button.module.scss';

function Button({
  onClickBtn,
  isHidden,
  btnPosition,
  btnColor,
  btnSize,
  isSubmit,
  ariaLabelText,
  children,
}) {
  const handleClickBtn = (evt) => {
    evt.preventDefault();
    onClickBtn();
  };

  return (
    <button
      className={`${Style.button} ${isHidden && Style.button_hidden} ${
        Style[`button__position_${btnPosition}`]
      } ${Style[`button__color_${btnColor}`]} ${
        Style[`button__size_${btnSize}`]
      }`}
      type={isSubmit ? 'submit' : 'button'}
      onClick={isSubmit ? null : handleClickBtn}
      aria-label={ariaLabelText}
    >
      {children}
    </button>
  );
}

Button.propTypes = {
  onClickBtn: PropTypes.func.isRequired,
  isHidden: PropTypes.bool,
  btnPosition: PropTypes.string,
  btnColor: PropTypes.string.isRequired,
  btnSize: PropTypes.string.isRequired,
  isSubmit: PropTypes.bool,
  children: PropTypes.node.isRequired,
  ariaLabelText: PropTypes.string.isRequired,
};

Button.defaultProps = {
  isHidden: false,
  btnPosition: '',
  isSubmit: false,
};

export default Button;
