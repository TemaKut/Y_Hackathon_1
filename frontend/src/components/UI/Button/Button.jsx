import React from 'react';
import PropTypes from 'prop-types';
import Style from './Button.module.scss';

function Button({
  onClickBtn,
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
      className={`${Style.button} ${Style[`button__position_${btnPosition}`]} ${
        Style[`button__color_${btnColor}`]
      } ${Style[`button__size_${btnSize}`]}`}
      type={isSubmit ? 'submit' : 'button'}
      onClick={isSubmit ? null : handleClickBtn}
      aria-label={ariaLabelText}
    >
      {children}
    </button>
  );
}

Button.propTypes = {
  btnPosition: PropTypes.string.isRequired,
  btnColor: PropTypes.string.isRequired,
  btnSize: PropTypes.string.isRequired,
  isSubmit: PropTypes.bool,
  children: PropTypes.node.isRequired,
  onClickBtn: PropTypes.func.isRequired,
  ariaLabelText: PropTypes.func.isRequired,
};

Button.defaultProps = {
  isSubmit: false,
};

export default Button;
