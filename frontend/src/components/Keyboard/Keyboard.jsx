import React from 'react';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Button from '../UI/Button/Button';
import Style from './Keyboard.module.scss';

function Keyboard({ isKeyboardOpen, titleText, children }) {
  if (!isKeyboardOpen) return null;

  return (
    <ReactPortal wrapperId="keyboard-container">
      <section
        className={`${Style.keyboard} ${isKeyboardOpen && Style.keyboard_open}`}
      >
        <div className={Style.inputContainer}>
          <h2 className={Style.title}>{titleText}</h2>
          <form>
            <input className={Style.input} />
            {children}
          </form>
        </div>
        <Button
          // onClickBtn={handleClickBtn}
          btnPosition="right"
          btnColor="yellow"
          btnSize="big"
          isSubmit
          ariaLabelText="Готово"
        >
          Готово
        </Button>
      </section>
    </ReactPortal>
  );
}

Keyboard.propTypes = {
  isKeyboardOpen: PropTypes.bool.isRequired,
  titleText: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};

export default Keyboard;
