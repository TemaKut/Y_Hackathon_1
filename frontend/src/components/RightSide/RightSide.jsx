/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './RightSide.module.scss';

function RightSide() {

    return (
        <button type='button' className={Style.package}>Подобрать упаковку</button>
    );
}

export default RightSide;