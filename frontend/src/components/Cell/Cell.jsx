/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Cell.module.scss';

function Cell() {

    return (
        <h2 className={Style.cellTitle}>Сканируйте товары <p className={Style.cellNumber}>B-09</p></h2>
    );
}

export default Cell;