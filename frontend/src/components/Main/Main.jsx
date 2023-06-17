import React, { useState, useEffect } from 'react';
import Style from './Main.module.scss';
import useAsync from '../../utils/useAsync';
import getOrderCell from '../../utils/getOrderCell';
import Cell from '../Cell/Cell';
import Button from '../UI/Button/Button';

function Main() {
  const [cellName, setCellName] = useState('');
  const { value } = useAsync(getOrderCell);

  useEffect(() => {
    if (value) {
      setCellName(value.cell);
    }
  }, [value]);

  // const handleClickBtn = () => {};

  return (
    <main className={Style.main}>
      <Cell cellName={cellName} />
      <Button
        // onClickBtn={handleClickBtn}
        btnPosition="right"
        btnColor="yellow"
        btnSize="big"
        isSubmit={false}
        ariaLabelText="Взять другое задание"
      >
        Взять другое задание
      </Button>
    </main>
  );
}

export default Main;
