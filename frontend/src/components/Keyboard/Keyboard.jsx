import React from 'react';
import PropTypes from 'prop-types';
import ReactPortal from '../ReactPortal/ReactPortal';
import Style from './Keyboard.module.scss';

function Keyboard({ isKeyboardOpen, titleText, children }) {
  if (!isKeyboardOpen) return null;

  return (
    <ReactPortal wrapperId="keyboard-container">
      <section
        className={`${Style.keyboard} ${isKeyboardOpen && Style.keyboard_open}`}
      >
        <h2 className={Style.title}>{titleText}</h2>
        <form>
          <input className={Style.input} />
          {children}
        </form>
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
