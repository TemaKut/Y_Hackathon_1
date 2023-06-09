/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Main.module.scss';
import Cell from '../Cell/Cell';
import Products from '../Products/Products';
// import Package from '../Package/Package';
// import Final from '../Final/Final';
import LeftSide from '../LeftSide/LeftSide';
import RightSide from '../RightSide/RightSide';

function Main() {

    return (
        <main className={Style.main}>
            <LeftSide />
            <Cell />
            <Products />
            {/* <Package /> */}
            {/* <Final /> */}
            <RightSide />
        </main>
    );
}

export default Main;