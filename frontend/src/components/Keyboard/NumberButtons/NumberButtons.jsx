import React from 'react';
import buttons from './buttons';
import Style from './NumberButtons.module.scss';

function NumberButtons() {
  return (
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
  );
}

export default NumberButtons;
