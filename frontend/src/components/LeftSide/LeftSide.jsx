import React from 'react';
import PropTypes from 'prop-types';
import Style from './LeftSide.module.scss';

function LeftSide({ isPackage }) {
  return (
    <div className={Style.leftSide}>
      {isPackage ? (
        <section className={Style.container}>
          <button type="button" className={Style.package}>
            Слишком маленькая
          </button>
          <button type="button" className={Style.package}>
            Слишком большая
          </button>
          <button type="button" className={Style.package}>
            Нет
            <br />в наличии
          </button>
        </section>
      ) : (
        <button type="button" className={Style.problem}>
          Есть проблема
        </button>
      )}
    </div>
  );
}

LeftSide.propTypes = {
  isPackage: PropTypes.bool,
};

LeftSide.defaultProps = {
  isPackage: false,
};

export default LeftSide;
