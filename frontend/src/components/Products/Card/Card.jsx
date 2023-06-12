import React from 'react';
import Style from './Card.module.scss';
import image from '../../../images/s-l400.jpg';

function Products() {
  return (
    <li className={Style.card}>
      <div className={Style.infoContainer}>
        <img className={Style.image} src={image} alt="Колонка Алиса" />
        <div className={Style.titleContainer}>
          <h3 className={Style.title}>
            Умная колонка Яндекс Станция Лайт, ультрафиолет
          </h3>
          <p className={`${Style.tag} ${Style.tag__type_package}`}>
            Пузырчатая плёнка
          </p>
        </div>
      </div>
      <p className={Style.quantity}>1 шт.</p>
      <p className={Style.barcode}>9234 5678 234 32</p>
    </li>
  );
}

export default Products;
