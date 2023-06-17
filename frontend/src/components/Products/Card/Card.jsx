/* eslint-disable react/destructuring-assignment */
import React from 'react';
import Style from './Card.module.scss';
// import image from '../../../images/s-l400.jpg';

function Products(card) {
  const urlImage =
    'http://localhost:8001/static/default_product_logo.png' ||
    card.card.sku_logo_url;
  return (
    <li className={Style.card}>
      <div className={Style.infoContainer}>
        <img className={Style.image} src={urlImage} alt={card.card.sku_name} />
        <div className={Style.titleContainer}>
          <h3 className={Style.title}>{card.card.sku_name}</h3>
          <p className={`${Style.tag} ${Style.tag__type_package}`}>
            Пузырчатая плёнка
          </p>
        </div>
      </div>
      <p className={Style.quantity}>{card.card.count} шт.</p>
      <p className={Style.barcode}>{card.card.sku}</p>
    </li>
  );
}

export default Products;
