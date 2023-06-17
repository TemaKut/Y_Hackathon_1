import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import useAsync from '../../utils/useAsync';
import getOrderCell from '../../utils/getOrderCell';
import Style from './Cell.module.scss';

function Cell() {
  const location = useLocation();
  const isStart = ['/'].includes(location.pathname);
  const cellText = isStart ? 'Сканируйте ячейку' : 'Сканируйте товары';
  const [cellName, setCellName] = useState('');
  const { value } = useAsync(getOrderCell);

  useEffect(() => {
    if (value) {
      setCellName(value.cell);
    }
  }, [value]);

  return cellName ? (
    <h2 className={`${Style.title} ${isStart && Style.start}`}>
      {cellText} <span className={Style.cellName}>{cellName}</span>
    </h2>
  ) : null;
}

export default Cell;
