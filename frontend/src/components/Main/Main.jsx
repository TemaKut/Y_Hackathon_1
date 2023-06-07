/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Main.module.scss';
import LeftSide from '../LeftSide/LeftSide';
import RightSide from '../RightSide/RightSide';

function Main() {

    return (
        <main className={Style.main}>
            <LeftSide />
            <RightSide />
        </main>
    );
}

export default Main;