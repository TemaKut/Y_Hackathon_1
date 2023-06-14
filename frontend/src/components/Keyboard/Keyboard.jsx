import React from 'react';
import PropTypes from 'prop-types';
// import ReactPortal from '../ReactPortal/ReactPortal';
import Style from './Keyboard.module.scss';
import NumberButtons from './NumberButtons/NumberButtons';

function Keyboard({ children }) {
  // const [isModalOpen, setIsModalOpen] = useState(true);
  // const closeModal = () => setIsModalOpen(false);

  // if (!isModalOpen) return null;

  return (
    // <ReactPortal wrapperId="modal-container">
    // <section className={`${Style.modal} ${isModalOpen && Style.openModal}`}>
    <section className={Style.keyboard}>
      <h2 className={Style.title}>Введите штрихкод товара</h2>
      <input className={Style.input} />
      {children}
      <NumberButtons />
    </section>
    // </ReactPortal>
  );
}

Keyboard.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Keyboard;
