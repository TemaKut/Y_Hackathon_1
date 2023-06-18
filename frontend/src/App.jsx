/* eslint-disable no-alert */
/* eslint-disable react/jsx-no-bind */
import React, { useState, useEffect } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';
import getOrderCell from './utils/getOrderCell';
import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Keyboard from './components/Keyboard/Keyboard';
import Popup from './components/Popup/Popup';
import Footer from './components/Footer/Footer';
import Products from './components/Products/Products';
import Package from './components/Package/Package';
import Final from './components/Final/Final';

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  // eslint-disable-next-line no-unused-vars
  const [loading, setLoading] = useState(false);
  // eslint-disable-next-line no-unused-vars
  const [error, setError] = useState(false);
  const [isKeyboardOpen, setIsKeyboardOpen] = useState(false);
  const [isPopupOpen, setIsPopupOpen] = useState(false);
  const [keyboardTitleText, setKeyboardTitleText] = useState('');
  const [orderData, setOrderData] = useState({
    cell: '',
    orderkey: '',
    suggestedPackage: '',
    chosenPackage: '',
  });

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);

  useEffect(() => {
    getOrderCell()
      .then((response) => setOrderData(response))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  function keyboardClick() {
    if (['/'].includes(location.pathname)) {
      setKeyboardTitleText('Введите код ячейки');
      setIsKeyboardOpen(true);
    } else if (['/products'].includes(location.pathname)) {
      setKeyboardTitleText('Введите код товара');
      setIsKeyboardOpen(true);
    } else if (['/package'].includes(location.pathname)) {
      navigate('/final');
    } else if (['/final'].includes(location.pathname)) {
      setIsPopupOpen(true);
    }
  }

  function footerButtonClick() {
    if (isStart) {
      alert('Скоро придут Вам помочь');
    } else {
      navigate(-1);
    }
  }

  return (
    <div className={Style.app}>
      <Header />
      <main className={Style.content}>
        <Routes>
          <Route
            exact
            path="/"
            element={
              <Main
                isStart={isStart}
                cellName={orderData.cell}
                setOrderData={setOrderData}
              />
            }
          />
          <Route
            exact
            path="/products"
            element={<Products cellName={orderData.cell} />}
          />
          <Route exact path="/package" element={<Package />} />
          <Route exact path="/final" element={<Final />} />
        </Routes>
      </main>
      <Keyboard
        isKeyboardOpen={isKeyboardOpen}
        setIsKeyboardOpen={setIsKeyboardOpen}
        orderKey={orderData.orderkey}
        titleText={keyboardTitleText}
      />
      <Popup isPopupOpen={isPopupOpen} />
      <Footer
        goBack={footerButtonClick}
        keyboardClick={keyboardClick}
        isFinal={isFinal}
        isStart={isStart}
      />
    </div>
  );
}

export default App;
