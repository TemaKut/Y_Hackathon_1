/* eslint-disable prettier/prettier */
import React from 'react';
import Style from './Footer.module.scss';
import boardLogo from '../../images/board-logo.svg';


function Footer() {
    return (
        <footer className={`${Style.footer} `}>

            <button type='button' className={`${Style.footer__button} `}>Не сканируется</button>
            <container type='button' className={Style.container}>
                <img className={Style.footer__boardlogo} src={boardLogo} alt='ракета' />
                <p className={`${Style.footer__boardtitle} `}>Ввести с клавиатуры</p>
            </container>

        </footer>
    );
}

export default Footer;
