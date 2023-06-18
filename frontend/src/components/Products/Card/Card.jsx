import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Style from './Card.module.scss';

function Products({ card, setAllChecked, allChecked }) {
  const [scanedCount, setScanedCount] = useState(0);
  const urlImage =
    'http://localhost:8001/static/default_product_logo.png' ||
    card.sku_logo_url;
  const handleScanSku = () => setScanedCount(scanedCount + 1);
  if (scanedCount === card.count) {
    setAllChecked(true);
  } else setAllChecked(false);

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
      <button onClick={handleScanSku} type="button" className={Style.barcode}>
        {card.sku}
      </button>
    </li>
  );
}

Products.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  card: PropTypes.object,
  setAllChecked: PropTypes.func.isRequired,
  allChecked: PropTypes.bool,
};

Products.defaultProps = {
  card: {},
  allChecked: false,
};

export default Products;
