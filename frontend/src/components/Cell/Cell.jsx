import React from 'react';
import { useLocation } from 'react-router-dom';
import PropTypes from 'prop-types';
import Style from './Cell.module.scss';

function Cell({ cellName }) {
  const location = useLocation();
  const isStart = ['/'].includes(location.pathname);
  const cellText = isStart ? 'Сканируйте ячейку' : 'Сканируйте товары';

  return cellName ? (
    <h2 className={`${Style.title} ${isStart && Style.start}`}>
      {cellText} <span className={Style.cellName}>{cellName}</span>
    </h2>
  ) : null;
}

Cell.propTypes = {
  cellName: PropTypes.string.isRequired,
};

export default Cell;
