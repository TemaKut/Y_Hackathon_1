import React from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import Style from './Final.module.scss';
import Button from '../UI/Button/Button';
import imgSucces from '../../images/succes.png';

function Final({ setOrderData }) {
  const navigate = useNavigate();

  const handleClickBtn = () => {
    navigate('/');
  };

  return (
    <div className={Style.final}>
      <h2 className={Style.final__title}>
        Заказ собран! <br />
        Поставьте коробку на конвейер.{' '}
      </h2>

      <img
        className={Style.final__img}
        src={imgSucces}
        alt="картинка с одобрением"
      />
      <Button
        onClickBtn={handleClickBtn}
        btnPosition="right"
        btnColor="yellow"
        btnSize="big"
        ariaLabelText="Готово"
      >
        Готово
      </Button>
    </div>
  );
}

Final.propTypes = {
  setOrderData: PropTypes.func.isRequired,
};

export default Final;
