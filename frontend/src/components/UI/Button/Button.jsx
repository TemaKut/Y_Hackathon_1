import React from 'react';
import PropTypes from 'prop-types';
import Style from './Button.module.scss';

function Button({
  onClickBtn,
  btnClassName,
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
      className={`${Style.button} ${Style[btnClassName]}`}
      type={isSubmit ? 'submit' : 'button'}
      onClick={isSubmit ? null : handleClickBtn}
      aria-label={ariaLabelText}
    >
      {children}
    </button>
  );
}

Button.propTypes = {
  btnClassName: PropTypes.string.isRequired,
  isSubmit: PropTypes.bool,
  children: PropTypes.node.isRequired,
  onClickBtn: PropTypes.func.isRequired,
  ariaLabelText: PropTypes.func.isRequired,
};

Button.defaultProps = {
  isSubmit: false,
};

export default Button;
