/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Products.module.scss';
// import imgSucces from '../../images/succes.png';


function Products() {

    return (
        <container className={Style.products}>
            <div className={Style.specs}>
                <span className={`${Style.products__amount} ${Style.spec}`}>6 товаров</span>
                <span className={`${Style.products__delivery} ${Style.spec}`}>Почта России</span>
            </div>
        </container >
    );
}

export default Products;