import React from 'react';
import Style from './Header.module.scss';
import logoYandex from '../../images/yandex-logo.svg';
import logoMarket from '../../images/market-logo.svg';
import logoService from '../../images/service.svg';
import logoEfficiency from '../../images/Union.svg';

function Header() {
  return (
    <header className={Style.header}>
      <section className={Style.container}>
        <div className={Style.header__hamburger} />
        <img
          className={Style.header__logoYandex}
          src={logoYandex}
          alt="лого Яндекс"
        />
        <img
          className={Style.header__logoMarket}
          src={logoMarket}
          alt="лого Маркет"
        />
        <img
          className={Style.header__logoService}
          src={logoService}
          alt="лого Склад"
        />
      </section>

      <h1 className={Style.header__title}>Упаковка</h1>

      <section className={Style.userStatistics}>
        <div className={Style.info}>
          <p className={Style.info__user}>sof-natgemokee</p>
          <div className={Style.efficiency}>
            <img
              className={Style.efficiency__logo}
              src={logoEfficiency}
              alt="ракета"
            />
            <p className={Style.efficiency__percent}>79%</p>
          </div>
        </div>
        <div className={Style.header__moreButton} />
      </section>
    </header>
  );
}

export default Header;
