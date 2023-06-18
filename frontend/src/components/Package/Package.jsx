import React, { useState, useEffect } from 'react';
import Style from './Package.module.scss';
import data from './packageData';
import Button from '../UI/Button/Button';
import boxIcon from '../../images/carton.svg';
import bagIcon from '../../images/bag.svg';
import boxImage from '../../images/box-ymf.png';
import bagImage from '../../images/bagImage.svg';

function Package() {
  const [packageName, setPackageName] = useState(data.packageResult.m);
  const [packageData, setPackageData] = useState({});

  const suggestBiggerCarton = () => {
    setPackageName(data.packageResult.l);
  };

  const suggestSmallerCarton = () => {
    setPackageName(data.packageResult.s);
  };

  useEffect(() => {
    const filteredData = data.packageData.filter(
      (item) => item.name === packageName
    );
    setPackageData(filteredData[0]);
  }, [packageName]);

  return (
    <section className={Style.package}>
      <div className={Style.buttons}>
        <Button
          onClickBtn={suggestBiggerCarton}
          btnPosition="left"
          btnColor="grey"
          btnSize="small"
          ariaLabelText={
            packageData.type === 'box'
              ? 'Слишком маленькая'
              : 'Слишком маленький'
          }
        >
          {packageData.type === 'box'
            ? 'Слишком маленькая'
            : 'Слишком маленький'}
        </Button>
        <Button
          onClickBtn={suggestSmallerCarton}
          btnPosition="left"
          btnColor="grey"
          btnSize="small"
          ariaLabelText={
            packageData.type === 'box' ? 'Слишком большая' : 'Слишком большой'
          }
        >
          {packageData.type === 'box' ? 'Слишком большая' : 'Слишком большой'}
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
        {packageData.type === 'box' ? ' коробку' : ' пакет'}
      </h2>
      <p
        className={Style.packageName}
        style={{ backgroundColor: packageData.backgroundColor }}
      >
        <img
          className={Style.icon}
          src={packageData.type === 'box' ? boxIcon : bagIcon}
          alt={packageData.type === 'box' ? 'Иконка коробки' : 'Иконка пакета'}
        />
        {packageName}
      </p>
      <img
        className={Style.image}
        src={packageData.type === 'box' ? boxImage : bagImage}
        alt={
          packageData.type === 'box' ? 'Картинка коробки' : 'Картинка пакета'
        }
      />
    </section>
  );
}

export default Package;
