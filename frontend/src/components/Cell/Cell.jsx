/* eslint-disable prettier/prettier */
import React from 'react';
import { useLocation } from 'react-router-dom';
import Style from './Cell.module.scss';

function Cell() {
    const location = useLocation();
    const isStart = ['/'].includes(location.pathname);
    const cellText = isStart ? 'Сканируйте ячейку' : 'Сканируйте товары';
    const cellTitleStyle = isStart ? Style.start : ''

    return (
        <h2 className={`${Style.cellTitle} ${cellTitleStyle}`}>{cellText} <p className={Style.cellNumber}>B-09</p></h2>
    );
}

export default Cell;