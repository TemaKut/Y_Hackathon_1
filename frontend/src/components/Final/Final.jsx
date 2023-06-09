/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Final.module.scss';
import imgSucces from '../../images/succes.png';


function Package() {

    return (
        <container className={Style.final}>
            <h2 className={Style.final__title}>Заказ собран! <br />Поставьте коробку на конвейер. </h2>

            <img className={Style.final__img} src={imgSucces} alt='картинка с одобрением' />
        </container >
    );
}

export default Package;