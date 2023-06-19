import React from 'react';
import PropTypes from 'prop-types';
import Style from './Card.module.scss';
import degaultImage from '../../../images/default_product_logo.png';

function Card({ card, setAllChecked, allChecked, scanedCount, allSkuArr }) {
  const urlImage = degaultImage || card.sku_logo_url;
  const oneProduct = {
    sku: '',
    count: '',
  };

  if (scanedCount === card.count) {
    setAllChecked(true);
  } else setAllChecked(false);

  if (card) {
    oneProduct.sku = card.sku;
    oneProduct.count = card.count;
    allSkuArr.push(oneProduct);
    localStorage.setItem('allProductsInfo', JSON.stringify(allSkuArr));
  }

  return (
    <li className={Style.card}>
      <div className={Style.infoContainer}>
        <img className={Style.image} src={urlImage} alt={card.sku_name} />
        <div className={Style.titleContainer}>
          <h3 className={Style.title}>{card.sku_name}</h3>
        </div>
      </div>
      <div className={Style.progressContainer}>
        <progress
          className={Style.progress}
          max={card.count}
          value={scanedCount}
        />
        {allChecked ? (
          <p className={Style.quantity}>{card.count} шт.</p>
        ) : (
          <p className={Style.quantity}>
            {scanedCount} из {card.count} шт.
          </p>
        )}
      </div>
      <p className={Style.barcode}>{card.sku}</p>
    </li>
  );
}

Card.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  card: PropTypes.object,
  setAllChecked: PropTypes.func.isRequired,
  allChecked: PropTypes.bool,
  // eslint-disable-next-line react/forbid-prop-types
  allSkuArr: PropTypes.array,
  scanedCount: PropTypes.string,
};

Card.defaultProps = {
  card: {},
  allChecked: false,
  scanedCount: 0,
  allSkuArr: [],
};

export default Card;
