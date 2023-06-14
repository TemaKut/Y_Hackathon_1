import React from 'react';
// import PropTypes from 'prop-types';
// import ReactPortal from '../ReactPortal/ReactPortal';
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
      <div className={Style.buttons}>
        {buttons.map((button) => (
          <button
            className={`${Style.button} ${Style[`button_${button.name}`]}`}
            key={button.id}
            type="button"
            aria-label={button.name}
          >
            {button.value}
          </button>
        ))}
        <button
          className={`${Style.button} ${Style.button_delete}`}
          type="button"
          aria-label="Удалить символ"
        />
      </div>
    </section>
    // </ReactPortal>
  );
}

// Keyboard.propTypes = {
//   children: PropTypes.node.isRequired,
// };

export default Keyboard;
