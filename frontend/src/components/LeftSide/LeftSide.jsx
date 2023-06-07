/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './LeftSide.module.scss';

function LeftSide() {

    return (
        <button type='button' className={Style.problem}>Есть проблема</button>
    );
}

export default LeftSide;