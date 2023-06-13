import React from 'react';
// import PropTypes from 'prop-types';
// import ReactPortal from '../ReactPortal/ReactPortal';
// import closeIcon from '../../images/close-icon.svg';
import buttons from './buttons';
import Style from './Keyboard.module.scss';

function Keyboard() {
  // const [isModalOpen, setIsModalOpen] = useState(true);
  // const closeModal = () => setIsModalOpen(false);

  // if (!isModalOpen) return null;

  return (
    // <ReactPortal wrapperId="modal-container">
    // <section className={`${Style.modal} ${isModalOpen && Style.openModal}`}>
    <section className={Style.keyboard}>
      {/* <div className={Style.content}>{children}</div> */}
      <h2 className={Style.title}>Введите штрихкод товара</h2>
      <input className={Style.input} />
      <ul className={Style.buttons}>
        {buttons.map((item) => (
          <li className={Style.buttonContainer}>
            <button className={Style.button} type="button" aria-label={item}>
              {item}
            </button>
          </li>
        ))}
        <li className={Style.buttonContainer}>
          <button
            className={Style.button}
            type="button"
            aria-label="Удалить символ"
          />
        </li>
      </ul>
    </section>
    // </ReactPortal>
  );
}

// Keyboard.propTypes = {
//   children: PropTypes.node.isRequired,
// };

export default Keyboard;
