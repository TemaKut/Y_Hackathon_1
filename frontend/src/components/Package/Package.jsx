import React from 'react';
import Style from './Package.module.scss';
import logoCarton from '../../images/carton.svg';
import imgYMF from '../../images/box-ymf.png';

function Package() {
  return (
    <section className={Style.package}>
      <h2 className={Style.package__title}>
        Упакуйте товары <br />и сканируйте коробку{' '}
      </h2>
      <p className={Style.package__number}>
        <img
          className={Style.package__logo}
          src={logoCarton}
          alt="лого Яндекс"
        />
        YMF
      </p>
      <img
        className={Style.package__img}
        src={imgYMF}
        alt="картинка упаковки"
      />
    </section>
  );
}

export default Package;
