import React from 'react';
import PropTypes from 'prop-types';
import Style from './Main.module.scss';
import getOrderCell from '../../utils/getOrderCell';
import Cell from '../Cell/Cell';
import Button from '../UI/Button/Button';

function Main({ cellName, setOrderData }) {
  const handleClickBtn = async () => {
    const newValue = await getOrderCell();

    setOrderData(newValue.cell);
  };

  return (
    <section className={Style.main}>
      <Cell cellName={cellName} />
      <Button
        onClickBtn={handleClickBtn}
        btnPosition="right"
        btnColor="yellow"
        btnSize="big"
        isSubmit={false}
        ariaLabelText="Взять другое задание"
      >
        Взять другое задание
      </Button>
    </section>
  );
}

Main.propTypes = {
  cellName: PropTypes.string,
  setOrderData: PropTypes.func.isRequired,
};

Main.defaultProps = {
  cellName: '',
};

export default Main;
