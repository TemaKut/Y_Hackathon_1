/* eslint-disable react/jsx-no-bind */
import React, { useState, useEffect } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';
import useAsync from './utils/useAsync';
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
  const [isKeyboardOpen, setIsKeyboardOpen] = useState(false);
  const [isPopupOpen, setIsPopupOpen] = useState(false);
  const [keyboardTitleText, setKeyboardTitleText] = useState('');
  const [cellName, setCellName] = useState('');
  const [orderKey, setOrderKey] = useState('');
  const { value } = useAsync(getOrderCell);

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);

  useEffect(() => {
    if (value) {
      setCellName(value.cell);
      setOrderKey(value.orderkey);
    }
  }, [value]);

  function keyboardClick() {
    if (['/'].includes(location.pathname)) {
      setKeyboardTitleText('Введите код ячейки');
      setIsKeyboardOpen(true);
    } else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    } else if (['/package'].includes(location.pathname)) {
      setIsPopupOpen(true);
      // navigate('/final');
    }
  }

  function goBack() {
    // navigate(-1);
    navigate('/products');
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
                cellName={cellName}
                setCellName={setCellName}
              />
            }
          />
          <Route
            exact
            path="/products"
            element={<Products cellName={cellName} orderKey={orderKey} />}
          />
          <Route exact path="/package" element={<Package />} />
          <Route exact path="/final" element={<Final />} />
        </Routes>
      </main>
      <Keyboard
        isKeyboardOpen={isKeyboardOpen}
        setIsKeyboardOpen={setIsKeyboardOpen}
        orderKey={value.orderkey}
        titleText={keyboardTitleText}
      />
      <Popup isPopupOpen={isPopupOpen} />
      <Footer
        goBack={goBack}
        keyboardClick={keyboardClick}
        isFinal={isFinal}
        isStart={isStart}
      />
    </div>
  );
}

export default App;
