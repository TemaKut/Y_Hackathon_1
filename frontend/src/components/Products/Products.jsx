/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Products.module.scss';
import Cell from '../Cell/Cell';

function Products() {

    return (
        <>
            <Cell />
            <container className={Style.products}>
                <div className={Style.specs}>
                    <span className={`${Style.products__amount} ${Style.spec}`}>6 товаров</span>
                    <span className={`${Style.products__delivery} ${Style.spec}`}>Почта России</span>
                </div>
            </container >
        </>
    );
}

export default Products;