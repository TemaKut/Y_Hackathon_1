/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './RightSide.module.scss';

// eslint-disable-next-line react/prop-types
function RightSide({ isStart, isFinal, rightSideClick }) {
    // eslint-disable-next-line no-nested-ternary
    const rightSideText = isStart ? 'Взять другое задание' : (isFinal ? 'Готово' : 'Подобрать упаковку');


    return (
        <button onClick={rightSideClick} type='button' className={Style.package}>{rightSideText}</button>
    );
}

export default RightSide;