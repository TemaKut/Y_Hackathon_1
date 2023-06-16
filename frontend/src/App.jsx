/* eslint-disable react/jsx-no-bind */
import React, { useState } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';

import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Keyboard from './components/Keyboard/Keyboard';
import Footer from './components/Footer/Footer';
import Products from './components/Products/Products';
import Package from './components/Package/Package';
import Final from './components/Final/Final';

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const [isKeyboardOpen, setIsKeyboardOpen] = useState(false);
  const [keyboardTitleText, setKeyboardTitleText] = useState('');

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);

  function keyboardClick() {
    if (['/'].includes(location.pathname)) {
      setKeyboardTitleText('Введите код ячейки');
      setIsKeyboardOpen(true);
    } else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    } else if (['/package'].includes(location.pathname)) {
      navigate('/final');
    }
  }

  function goBack() {
    navigate(-1);
  }

  return (
    <div className={Style.app}>
      <Header />
      <main className={Style.content}>
        <Routes>
          <Route exact path="/" element={<Main isStart={isStart} />} />
          <Route exact path="/products" element={<Products />} />
          <Route exact path="/package" element={<Package />} />
          <Route exact path="/final" element={<Final />} />
        </Routes>
      </main>
      <Keyboard isKeyboardOpen={isKeyboardOpen} titleText={keyboardTitleText} />
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
