import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Style from './Package.module.scss';
import packagePropertiesData from './packageData';
import getOrderPackage from '../../utils/getPackage';
import Button from '../UI/Button/Button';
import Keyboard from '../Keyboard/Keyboard';
import boxIcon from '../../images/carton.svg';
import bagIcon from '../../images/bag.svg';
import boxImage from '../../images/box-ymf.png';
import bagImage from '../../images/bagImage.svg';

function Package({
  orderKey,
  setOrderData,
  setError,
  setLoading,
  isKeyboardOpen,
  setIsKeyboardOpen,
}) {
  const [packageData, setPackageData] = useState({
    s: '',
    m: '',
    l: '',
  });
  const [packageName, setPackageName] = useState('');
  const [packageProperties, setPackageProperties] = useState({
    name: '',
    type: '',
    backgroundColor: '',
  });

  const getPackageData = () => {
    if (orderKey) {
      setLoading(true);
      getOrderPackage(orderKey)
        .then((response) => {
          setPackageData(response);
          setPackageName(response.m);
        })
        .catch((err) => setError(err))
        .finally(() => setLoading(false));
    }
  };

  const suggestBiggerCarton = () => {
    setPackageName(packageData.l);
  };

  const suggestSmallerCarton = () => {
    setPackageName(packageData.s);
  };

  useEffect(() => {
    const filteredData = packagePropertiesData.filter(
      (item) => item.name === packageName
    );
    if (filteredData.length > 0) {
      setPackageProperties(filteredData[0]);
    } else {
      setPackageProperties({
        name: packageName,
        type: packageName.substring(0, 1) === 'Y' ? 'box' : 'none',
        backgroundColor: '#FF0000',
      });
    }
  }, [packageName]);

  useEffect(() => {
    getPackageData();
  }, [orderKey]);

  useEffect(() => {
    setOrderData(packageName);
  }, [packageName]);

  return packageData && packageName && packageProperties ? (
    <>
      <section className={Style.package}>
        <div className={Style.buttons}>
          <Button
            onClickBtn={suggestBiggerCarton}
            btnPosition="left"
            btnColor="grey"
            btnSize="small"
            ariaLabelText={
              packageProperties.type === 'box'
                ? 'Слишком маленькая'
                : 'Слишком маленький'
            }
          >
            {packageProperties.type === 'box'
              ? 'Слишком маленькая'
              : 'Слишком маленький'}
          </Button>
          <Button
            onClickBtn={suggestSmallerCarton}
            btnPosition="left"
            btnColor="grey"
            btnSize="small"
            ariaLabelText={
              packageProperties.type === 'box'
                ? 'Слишком большая'
                : 'Слишком большой'
            }
          >
            {packageProperties.type === 'box'
              ? 'Слишком большая'
              : 'Слишком большой'}
          </Button>
          <Button
            onClickBtn={suggestBiggerCarton}
            btnPosition="left"
            btnColor="grey"
            btnSize="small"
            ariaLabelText="Нет в наличии"
          >
            Нет
            <br />в наличии
          </Button>
        </div>
        <h2 className={Style.title}>
          Упакуйте товары <br />и сканируйте
          {packageProperties.type === 'box' ? ' коробку' : ' пакет'}
        </h2>
        <p
          className={Style.packageName}
          style={{ backgroundColor: packageProperties.backgroundColor }}
        >
          <img
            className={Style.icon}
            src={packageProperties.type === 'box' ? boxIcon : bagIcon}
            alt={
              packageProperties.type === 'box'
                ? 'Иконка коробки'
                : 'Иконка пакета'
            }
          />
          {packageName}
        </p>
        <img
          className={Style.image}
          src={packageProperties.type === 'box' ? boxImage : bagImage}
          alt={
            packageProperties.type === 'box'
              ? 'Картинка коробки'
              : 'Картинка пакета'
          }
        />
      </section>
      <Keyboard
        isKeyboardOpen={isKeyboardOpen}
        setIsKeyboardOpen={setIsKeyboardOpen}
        orderKey={orderKey}
        titleText="Введите код упаковки"
        isPackage
      />
    </>
  ) : null;
}

Package.propTypes = {
  orderKey: PropTypes.string.isRequired,
  setOrderData: PropTypes.func.isRequired,
  setError: PropTypes.func.isRequired,
  setLoading: PropTypes.func.isRequired,
  isKeyboardOpen: PropTypes.bool.isRequired,
  setIsKeyboardOpen: PropTypes.func.isRequired,
};

export default Package;
